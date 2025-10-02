from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_iam as iam,
    aws_logs as logs,
    aws_cloudwatch as cloudwatch,
    aws_cloudwatch_actions as cw_actions,
    aws_sns as sns,
    Duration,
    CfnOutput
)
from constructs import Construct
import os
import aws_cdk as cdk



class ApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        vpc = ec2.Vpc(
            self, "InfluxDBVPC",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ]
        )

        # Security Groups
        influxdb_sg = ec2.SecurityGroup(
            self, "InfluxDBSG",
            vpc=vpc,
            description="Security group for InfluxDB",
            allow_all_outbound=True
        )

        crud_sg = ec2.SecurityGroup(
            self, "APISG",
            vpc=vpc,
            description="Security group for CRUD API",
            allow_all_outbound=True
        )

        # Security Group rule: CRUD to InfluxDB
        influxdb_sg.add_ingress_rule(
            peer=crud_sg,
            connection=ec2.Port.tcp(8086),
            description="Allow CRUD service to connect to InfluxDB"
        )

        user_data = ec2.UserData.for_linux()
        user_data.add_commands(
            "sudo yum update -y",
            "sudo amazon-linux-extras install docker -y",
            "sudo service docker start",
            "sudo usermod -a -G docker ec2-user",
            "docker run -d -p 8086:8086 --name influxdb influxdb:2.7"
        )

        # InfluxDB EC2 instance (private subnet)
        influxdb_instance = ec2.Instance(
            self, "InfluxDBInstance",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            security_group=influxdb_sg,
            user_data=user_data
        )

        # ECS Cluster + Fargate CRUD API
        cluster = ecs.Cluster(
            self,
            "CRUDCluster",
            vpc=vpc,
            container_insights = True)

        # Task roles
        task_execution_role = iam.Role(
            self, "TaskExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AmazonECSTaskExecutionRolePolicy"
                )
            ]
        )

        task_role = iam.Role(
            self, "TaskRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com")
        )
        task_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                resources=["*"]
            )
        )

        task_definition = ecs.FargateTaskDefinition(
            self, "CRUDTaskDefinition",
            memory_limit_mib=512,
            cpu=256,
            execution_role=task_execution_role,
            task_role=task_role
        )

        container = task_definition.add_container(
            "CRUDContainer",
            image=ecs.ContainerImage.from_asset("./crud_service"),
            logging=ecs.LogDriver.aws_logs(
                stream_prefix="crud-api",
                log_retention=logs.RetentionDays.ONE_WEEK
            ),
            environment={
                "INFLUXDB_URL": os.getenv("INFLUXDB_URL"),
                "INFLUXDB_TOKEN": os.getenv("INFLUXDB_TOKEN"),
                "INFLUXDB_ORG": os.getenv("INFLUXDB_ORG"),
                "INFLUXDB_BUCKET": os.getenv("INFLUXDB_BUCKET")
            },

            health_check=ecs.HealthCheck(
                command=["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"],
                interval=Duration.seconds(30),
                timeout=Duration.seconds(5),
                retries=3,
                start_period=Duration.seconds(60)
            )
        )
        container.add_port_mappings(ecs.PortMapping(container_port=8080))

        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "CRUDService",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=2,
            public_load_balancer=True,
            listener_port=80,
            task_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            health_check_grace_period=Duration.seconds(60)
        )

        # Auto Scaling
        scaling = fargate_service.service.auto_scale_task_count(min_capacity=2, max_capacity=10)
        scaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=70,
            scale_in_cooldown=Duration.seconds(60),
            scale_out_cooldown=Duration.seconds(60)
        )

        # CloudWatch Alarms
        alarm_topic = sns.Topic(self, "AlarmTopic", display_name="CRUD API Alarms")

        cpu_alarm = cloudwatch.Alarm(
            self, "HighCPUAlarm",
            metric=fargate_service.service.metric_cpu_utilization(),
            threshold=80,
            evaluation_periods=2,
            datapoints_to_alarm=2,
            treat_missing_data=cloudwatch.TreatMissingData.NOT_BREACHING
        )
        cpu_alarm.add_alarm_action(cw_actions.SnsAction(alarm_topic))

        memory_alarm = cloudwatch.Alarm(
            self, "HighMemoryAlarm",
            metric=fargate_service.service.metric_memory_utilization(),
            threshold=80,
            evaluation_periods=2,
            datapoints_to_alarm=2,
            treat_missing_data=cloudwatch.TreatMissingData.NOT_BREACHING
        )
        memory_alarm.add_alarm_action(cw_actions.SnsAction(alarm_topic))

        # Outputs
        CfnOutput(self, "LoadBalancerDNS", value=fargate_service.load_balancer.load_balancer_dns_name)
        CfnOutput(self, "ServiceURL", value=f"http://{fargate_service.load_balancer.load_balancer_dns_name}")
        CfnOutput(self, "AlarmTopicArn", value=alarm_topic.topic_arn)
        CfnOutput(self, "InfluxDBPrivateIP", value=influxdb_instance.instance_private_ip)

app = cdk.App()

ApiStack(app, "ApiStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
    )
)

app.synth()