'''
# AWS::EntityResolution Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_entityresolution as entityresolution
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EntityResolution construct libraries](https://constructs.dev/search?q=entityresolution)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EntityResolution resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EntityResolution.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EntityResolution](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EntityResolution.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnMatchingWorkflow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflow",
):
    '''Creates a ``MatchingWorkflow`` object which stores the configuration of the data processing job to be run.

    It is important to note that there should not be a pre-existing ``MatchingWorkflow`` with the same name. To modify an existing workflow, utilize the ``UpdateMatchingWorkflow`` API.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html
    :cloudformationResource: AWS::EntityResolution::MatchingWorkflow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_entityresolution as entityresolution
        
        cfn_matching_workflow = entityresolution.CfnMatchingWorkflow(self, "MyCfnMatchingWorkflow",
            input_source_config=[entityresolution.CfnMatchingWorkflow.InputSourceProperty(
                input_source_arn="inputSourceArn",
                schema_arn="schemaArn",
        
                # the properties below are optional
                apply_normalization=False
            )],
            output_source_config=[entityresolution.CfnMatchingWorkflow.OutputSourceProperty(
                output=[entityresolution.CfnMatchingWorkflow.OutputAttributeProperty(
                    name="name",
        
                    # the properties below are optional
                    hashed=False
                )],
                output_s3_path="outputS3Path",
        
                # the properties below are optional
                apply_normalization=False,
                kms_arn="kmsArn"
            )],
            resolution_techniques=entityresolution.CfnMatchingWorkflow.ResolutionTechniquesProperty(
                resolution_type="resolutionType",
                rule_based_properties=entityresolution.CfnMatchingWorkflow.RuleBasedPropertiesProperty(
                    attribute_matching_model="attributeMatchingModel",
                    rules=[entityresolution.CfnMatchingWorkflow.RuleProperty(
                        matching_keys=["matchingKeys"],
                        rule_name="ruleName"
                    )]
                )
            ),
            role_arn="roleArn",
            workflow_name="workflowName",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        input_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchingWorkflow.InputSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        output_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchingWorkflow.OutputSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        resolution_techniques: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchingWorkflow.ResolutionTechniquesProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        workflow_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param input_source_config: A list of ``InputSource`` objects, which have the fields ``InputSourceARN`` and ``SchemaName`` .
        :param output_source_config: A list of ``OutputSource`` objects, each of which contains fields ``OutputS3Path`` , ``ApplyNormalization`` , and ``Output`` .
        :param resolution_techniques: An object which defines the ``resolutionType`` and the ``ruleBasedProperties`` .
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
        :param workflow_name: The name of the workflow. There cannot be multiple ``DataIntegrationWorkflows`` with the same name.
        :param description: A description of the workflow.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c9e9b620b89ac2aae774eb42384e0472b5a13eeb28983708b164b2400ebcd39)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMatchingWorkflowProps(
            input_source_config=input_source_config,
            output_source_config=output_source_config,
            resolution_techniques=resolution_techniques,
            role_arn=role_arn,
            workflow_name=workflow_name,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a2bf1cfd69ad77cafcf7b6d5e0508159e0ece5385e2b3a0808436e336abbfcc)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83843fc5000b4b7c1f325390bceaadeeec20658b2de2de2143a3d987e3c49953)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time of this MatchingWorkflow got created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The time of this MatchingWorkflow got last updated at.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkflowArn")
    def attr_workflow_arn(self) -> builtins.str:
        '''The default MatchingWorkflow arn.

        :cloudformationAttribute: WorkflowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkflowArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="inputSourceConfig")
    def input_source_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.InputSourceProperty"]]]:
        '''A list of ``InputSource`` objects, which have the fields ``InputSourceARN`` and ``SchemaName`` .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.InputSourceProperty"]]], jsii.get(self, "inputSourceConfig"))

    @input_source_config.setter
    def input_source_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.InputSourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46336e1b290b62290456cef0086653d1bf7bde247391e85b7b88570883b249d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputSourceConfig", value)

    @builtins.property
    @jsii.member(jsii_name="outputSourceConfig")
    def output_source_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.OutputSourceProperty"]]]:
        '''A list of ``OutputSource`` objects, each of which contains fields ``OutputS3Path`` , ``ApplyNormalization`` , and ``Output`` .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.OutputSourceProperty"]]], jsii.get(self, "outputSourceConfig"))

    @output_source_config.setter
    def output_source_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.OutputSourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6752620fe10a272a45c22eb2493e5e30fcac8bb82fcc95b6f46271727dadc72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputSourceConfig", value)

    @builtins.property
    @jsii.member(jsii_name="resolutionTechniques")
    def resolution_techniques(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.ResolutionTechniquesProperty"]:
        '''An object which defines the ``resolutionType`` and the ``ruleBasedProperties`` .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.ResolutionTechniquesProperty"], jsii.get(self, "resolutionTechniques"))

    @resolution_techniques.setter
    def resolution_techniques(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.ResolutionTechniquesProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfbb583351458ecc2896a0f04d4bae86260e8762b28c2687fe570562260a9a48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolutionTechniques", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68dfd5a70e354a050b7085c6c4cc4520862c51d487a8a8e920928f222fa1894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="workflowName")
    def workflow_name(self) -> builtins.str:
        '''The name of the workflow.'''
        return typing.cast(builtins.str, jsii.get(self, "workflowName"))

    @workflow_name.setter
    def workflow_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e33fb06ce08c9c2af24c4cb3e68018f92d9bc69c0f62bc965ba1640232fd73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146028c4441df7c65ea8aba2981fe23a6e2fda2af137f4c78d1c5c84d63a3b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a7896d7bea53a4e2ffc9445d9a42b8864f5ac9a6cf43c3b27fe3c77bd39a83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflow.InputSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_source_arn": "inputSourceArn",
            "schema_arn": "schemaArn",
            "apply_normalization": "applyNormalization",
        },
    )
    class InputSourceProperty:
        def __init__(
            self,
            *,
            input_source_arn: builtins.str,
            schema_arn: builtins.str,
            apply_normalization: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''An object containing ``InputSourceARN`` , ``SchemaName`` , and ``ApplyNormalization`` .

            :param input_source_arn: An object containing ``InputSourceARN`` , ``SchemaName`` , and ``ApplyNormalization`` .
            :param schema_arn: The name of the schema.
            :param apply_normalization: Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an ``AttributeType`` of ``PHONE_NUMBER`` , and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_entityresolution as entityresolution
                
                input_source_property = entityresolution.CfnMatchingWorkflow.InputSourceProperty(
                    input_source_arn="inputSourceArn",
                    schema_arn="schemaArn",
                
                    # the properties below are optional
                    apply_normalization=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a18bfef9ee8ade2fff3913e22cf37d98f5880893c2204caa684a7f3831327af)
                check_type(argname="argument input_source_arn", value=input_source_arn, expected_type=type_hints["input_source_arn"])
                check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
                check_type(argname="argument apply_normalization", value=apply_normalization, expected_type=type_hints["apply_normalization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_source_arn": input_source_arn,
                "schema_arn": schema_arn,
            }
            if apply_normalization is not None:
                self._values["apply_normalization"] = apply_normalization

        @builtins.property
        def input_source_arn(self) -> builtins.str:
            '''An object containing ``InputSourceARN`` , ``SchemaName`` , and ``ApplyNormalization`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html#cfn-entityresolution-matchingworkflow-inputsource-inputsourcearn
            '''
            result = self._values.get("input_source_arn")
            assert result is not None, "Required property 'input_source_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def schema_arn(self) -> builtins.str:
            '''The name of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html#cfn-entityresolution-matchingworkflow-inputsource-schemaarn
            '''
            result = self._values.get("schema_arn")
            assert result is not None, "Required property 'schema_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def apply_normalization(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Normalizes the attributes defined in the schema in the input data.

            For example, if an attribute has an ``AttributeType`` of ``PHONE_NUMBER`` , and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html#cfn-entityresolution-matchingworkflow-inputsource-applynormalization
            '''
            result = self._values.get("apply_normalization")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflow.OutputAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "hashed": "hashed"},
    )
    class OutputAttributeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            hashed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A list of ``OutputAttribute`` objects, each of which have the fields ``Name`` and ``Hashed`` .

            Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

            :param name: A name of a column to be written to the output. This must be an ``InputField`` name in the schema mapping.
            :param hashed: Enables the ability to hash the column values in the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_entityresolution as entityresolution
                
                output_attribute_property = entityresolution.CfnMatchingWorkflow.OutputAttributeProperty(
                    name="name",
                
                    # the properties below are optional
                    hashed=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__006a3c9280759d8123ca560d0c7cfef20e64f8703bb04be12b8a7e08728768e5)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument hashed", value=hashed, expected_type=type_hints["hashed"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if hashed is not None:
                self._values["hashed"] = hashed

        @builtins.property
        def name(self) -> builtins.str:
            '''A name of a column to be written to the output.

            This must be an ``InputField`` name in the schema mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputattribute.html#cfn-entityresolution-matchingworkflow-outputattribute-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hashed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables the ability to hash the column values in the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputattribute.html#cfn-entityresolution-matchingworkflow-outputattribute-hashed
            '''
            result = self._values.get("hashed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflow.OutputSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output": "output",
            "output_s3_path": "outputS3Path",
            "apply_normalization": "applyNormalization",
            "kms_arn": "kmsArn",
        },
    )
    class OutputSourceProperty:
        def __init__(
            self,
            *,
            output: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchingWorkflow.OutputAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]],
            output_s3_path: builtins.str,
            apply_normalization: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            kms_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A list of ``OutputAttribute`` objects, each of which have the fields ``Name`` and ``Hashed`` .

            Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

            :param output: A list of ``OutputAttribute`` objects, each of which have the fields ``Name`` and ``Hashed`` . Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.
            :param output_s3_path: The S3 path to which AWS Entity Resolution will write the output table.
            :param apply_normalization: Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an ``AttributeType`` of ``PHONE_NUMBER`` , and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.
            :param kms_arn: Customer KMS ARN for encryption at rest. If not provided, system will use an AWS Entity Resolution managed KMS key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_entityresolution as entityresolution
                
                output_source_property = entityresolution.CfnMatchingWorkflow.OutputSourceProperty(
                    output=[entityresolution.CfnMatchingWorkflow.OutputAttributeProperty(
                        name="name",
                
                        # the properties below are optional
                        hashed=False
                    )],
                    output_s3_path="outputS3Path",
                
                    # the properties below are optional
                    apply_normalization=False,
                    kms_arn="kmsArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__92bb2dc25f018fe0017c7ab79f29b2fdfb4238d6fb1293a9cd606b9f93976df8)
                check_type(argname="argument output", value=output, expected_type=type_hints["output"])
                check_type(argname="argument output_s3_path", value=output_s3_path, expected_type=type_hints["output_s3_path"])
                check_type(argname="argument apply_normalization", value=apply_normalization, expected_type=type_hints["apply_normalization"])
                check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "output": output,
                "output_s3_path": output_s3_path,
            }
            if apply_normalization is not None:
                self._values["apply_normalization"] = apply_normalization
            if kms_arn is not None:
                self._values["kms_arn"] = kms_arn

        @builtins.property
        def output(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.OutputAttributeProperty"]]]:
            '''A list of ``OutputAttribute`` objects, each of which have the fields ``Name`` and ``Hashed`` .

            Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-output
            '''
            result = self._values.get("output")
            assert result is not None, "Required property 'output' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.OutputAttributeProperty"]]], result)

        @builtins.property
        def output_s3_path(self) -> builtins.str:
            '''The S3 path to which AWS Entity Resolution will write the output table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-outputs3path
            '''
            result = self._values.get("output_s3_path")
            assert result is not None, "Required property 'output_s3_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def apply_normalization(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Normalizes the attributes defined in the schema in the input data.

            For example, if an attribute has an ``AttributeType`` of ``PHONE_NUMBER`` , and the data in the input table is in a format of 1234567890, AWS Entity Resolution will normalize this field in the output to (123)-456-7890.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-applynormalization
            '''
            result = self._values.get("apply_normalization")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def kms_arn(self) -> typing.Optional[builtins.str]:
            '''Customer KMS ARN for encryption at rest.

            If not provided, system will use an AWS Entity Resolution managed KMS key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-kmsarn
            '''
            result = self._values.get("kms_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflow.ResolutionTechniquesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resolution_type": "resolutionType",
            "rule_based_properties": "ruleBasedProperties",
        },
    )
    class ResolutionTechniquesProperty:
        def __init__(
            self,
            *,
            resolution_type: typing.Optional[builtins.str] = None,
            rule_based_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchingWorkflow.RuleBasedPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object which defines the ``resolutionType`` and the ``ruleBasedProperties`` .

            :param resolution_type: The type of matching. There are two types of matching: ``RULE_MATCHING`` and ``ML_MATCHING`` .
            :param rule_based_properties: An object which defines the list of matching rules to run and has a field ``Rules`` , which is a list of rule objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_entityresolution as entityresolution
                
                resolution_techniques_property = entityresolution.CfnMatchingWorkflow.ResolutionTechniquesProperty(
                    resolution_type="resolutionType",
                    rule_based_properties=entityresolution.CfnMatchingWorkflow.RuleBasedPropertiesProperty(
                        attribute_matching_model="attributeMatchingModel",
                        rules=[entityresolution.CfnMatchingWorkflow.RuleProperty(
                            matching_keys=["matchingKeys"],
                            rule_name="ruleName"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1c6ea89cbe5bb10bb721c60f7c5951a6a56729058a7b00d3dd16b091aa63ab9)
                check_type(argname="argument resolution_type", value=resolution_type, expected_type=type_hints["resolution_type"])
                check_type(argname="argument rule_based_properties", value=rule_based_properties, expected_type=type_hints["rule_based_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if resolution_type is not None:
                self._values["resolution_type"] = resolution_type
            if rule_based_properties is not None:
                self._values["rule_based_properties"] = rule_based_properties

        @builtins.property
        def resolution_type(self) -> typing.Optional[builtins.str]:
            '''The type of matching.

            There are two types of matching: ``RULE_MATCHING`` and ``ML_MATCHING`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html#cfn-entityresolution-matchingworkflow-resolutiontechniques-resolutiontype
            '''
            result = self._values.get("resolution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_based_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.RuleBasedPropertiesProperty"]]:
            '''An object which defines the list of matching rules to run and has a field ``Rules`` , which is a list of rule objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html#cfn-entityresolution-matchingworkflow-resolutiontechniques-rulebasedproperties
            '''
            result = self._values.get("rule_based_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.RuleBasedPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResolutionTechniquesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflow.RuleBasedPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_matching_model": "attributeMatchingModel",
            "rules": "rules",
        },
    )
    class RuleBasedPropertiesProperty:
        def __init__(
            self,
            *,
            attribute_matching_model: builtins.str,
            rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchingWorkflow.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''An object which defines the list of matching rules to run and has a field ``Rules`` , which is a list of rule objects.

            :param attribute_matching_model: The comparison type. You can either choose ``ONE_TO_ONE`` or ``MANY_TO_MANY`` as the AttributeMatchingModel. When choosing ``MANY_TO_MANY`` , the system can match attributes across the sub-types of an attribute type. For example, if the value of the ``Email`` field of Profile A and the value of ``BusinessEmail`` field of Profile B matches, the two profiles are matched on the ``Email`` type. When choosing ``ONE_TO_ONE`` ,the system can only match if the sub-types are exact matches. For example, only when the value of the ``Email`` field of Profile A and the value of the ``Email`` field of Profile B matches, the two profiles are matched on the ``Email`` type.
            :param rules: A list of ``Rule`` objects, each of which have fields ``RuleName`` and ``MatchingKeys`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_entityresolution as entityresolution
                
                rule_based_properties_property = entityresolution.CfnMatchingWorkflow.RuleBasedPropertiesProperty(
                    attribute_matching_model="attributeMatchingModel",
                    rules=[entityresolution.CfnMatchingWorkflow.RuleProperty(
                        matching_keys=["matchingKeys"],
                        rule_name="ruleName"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96d1f97c0110dea5fb9a8413e199ae25878eedad10521ad056ca772f31ddb8ba)
                check_type(argname="argument attribute_matching_model", value=attribute_matching_model, expected_type=type_hints["attribute_matching_model"])
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_matching_model": attribute_matching_model,
                "rules": rules,
            }

        @builtins.property
        def attribute_matching_model(self) -> builtins.str:
            '''The comparison type.

            You can either choose ``ONE_TO_ONE`` or ``MANY_TO_MANY`` as the AttributeMatchingModel. When choosing ``MANY_TO_MANY`` , the system can match attributes across the sub-types of an attribute type. For example, if the value of the ``Email`` field of Profile A and the value of ``BusinessEmail`` field of Profile B matches, the two profiles are matched on the ``Email`` type. When choosing ``ONE_TO_ONE`` ,the system can only match if the sub-types are exact matches. For example, only when the value of the ``Email`` field of Profile A and the value of the ``Email`` field of Profile B matches, the two profiles are matched on the ``Email`` type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html#cfn-entityresolution-matchingworkflow-rulebasedproperties-attributematchingmodel
            '''
            result = self._values.get("attribute_matching_model")
            assert result is not None, "Required property 'attribute_matching_model' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.RuleProperty"]]]:
            '''A list of ``Rule`` objects, each of which have fields ``RuleName`` and ``MatchingKeys`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html#cfn-entityresolution-matchingworkflow-rulebasedproperties-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchingWorkflow.RuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleBasedPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflow.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={"matching_keys": "matchingKeys", "rule_name": "ruleName"},
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            matching_keys: typing.Sequence[builtins.str],
            rule_name: builtins.str,
        ) -> None:
            '''An object containing ``RuleName`` , and ``MatchingKeys`` .

            :param matching_keys: A list of ``MatchingKeys`` . The ``MatchingKeys`` must have been defined in the ``SchemaMapping`` . Two records are considered to match according to this rule if all of the ``MatchingKeys`` match.
            :param rule_name: A name for the matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_entityresolution as entityresolution
                
                rule_property = entityresolution.CfnMatchingWorkflow.RuleProperty(
                    matching_keys=["matchingKeys"],
                    rule_name="ruleName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ad893f1319125d264f9286a93c40cd8616031944a24803bccedd15e3233ef0f)
                check_type(argname="argument matching_keys", value=matching_keys, expected_type=type_hints["matching_keys"])
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "matching_keys": matching_keys,
                "rule_name": rule_name,
            }

        @builtins.property
        def matching_keys(self) -> typing.List[builtins.str]:
            '''A list of ``MatchingKeys`` .

            The ``MatchingKeys`` must have been defined in the ``SchemaMapping`` . Two records are considered to match according to this rule if all of the ``MatchingKeys`` match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rule.html#cfn-entityresolution-matchingworkflow-rule-matchingkeys
            '''
            result = self._values.get("matching_keys")
            assert result is not None, "Required property 'matching_keys' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''A name for the matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rule.html#cfn-entityresolution-matchingworkflow-rule-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_entityresolution.CfnMatchingWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "input_source_config": "inputSourceConfig",
        "output_source_config": "outputSourceConfig",
        "resolution_techniques": "resolutionTechniques",
        "role_arn": "roleArn",
        "workflow_name": "workflowName",
        "description": "description",
        "tags": "tags",
    },
)
class CfnMatchingWorkflowProps:
    def __init__(
        self,
        *,
        input_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.InputSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
        output_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.OutputSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
        resolution_techniques: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.ResolutionTechniquesProperty, typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        workflow_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMatchingWorkflow``.

        :param input_source_config: A list of ``InputSource`` objects, which have the fields ``InputSourceARN`` and ``SchemaName`` .
        :param output_source_config: A list of ``OutputSource`` objects, each of which contains fields ``OutputS3Path`` , ``ApplyNormalization`` , and ``Output`` .
        :param resolution_techniques: An object which defines the ``resolutionType`` and the ``ruleBasedProperties`` .
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
        :param workflow_name: The name of the workflow. There cannot be multiple ``DataIntegrationWorkflows`` with the same name.
        :param description: A description of the workflow.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_entityresolution as entityresolution
            
            cfn_matching_workflow_props = entityresolution.CfnMatchingWorkflowProps(
                input_source_config=[entityresolution.CfnMatchingWorkflow.InputSourceProperty(
                    input_source_arn="inputSourceArn",
                    schema_arn="schemaArn",
            
                    # the properties below are optional
                    apply_normalization=False
                )],
                output_source_config=[entityresolution.CfnMatchingWorkflow.OutputSourceProperty(
                    output=[entityresolution.CfnMatchingWorkflow.OutputAttributeProperty(
                        name="name",
            
                        # the properties below are optional
                        hashed=False
                    )],
                    output_s3_path="outputS3Path",
            
                    # the properties below are optional
                    apply_normalization=False,
                    kms_arn="kmsArn"
                )],
                resolution_techniques=entityresolution.CfnMatchingWorkflow.ResolutionTechniquesProperty(
                    resolution_type="resolutionType",
                    rule_based_properties=entityresolution.CfnMatchingWorkflow.RuleBasedPropertiesProperty(
                        attribute_matching_model="attributeMatchingModel",
                        rules=[entityresolution.CfnMatchingWorkflow.RuleProperty(
                            matching_keys=["matchingKeys"],
                            rule_name="ruleName"
                        )]
                    )
                ),
                role_arn="roleArn",
                workflow_name="workflowName",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2be3b46399b509a45bb640cf4a70ab0714322917a6d3dc4c241cb16ab2d1dbb0)
            check_type(argname="argument input_source_config", value=input_source_config, expected_type=type_hints["input_source_config"])
            check_type(argname="argument output_source_config", value=output_source_config, expected_type=type_hints["output_source_config"])
            check_type(argname="argument resolution_techniques", value=resolution_techniques, expected_type=type_hints["resolution_techniques"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument workflow_name", value=workflow_name, expected_type=type_hints["workflow_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_source_config": input_source_config,
            "output_source_config": output_source_config,
            "resolution_techniques": resolution_techniques,
            "role_arn": role_arn,
            "workflow_name": workflow_name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def input_source_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.InputSourceProperty]]]:
        '''A list of ``InputSource`` objects, which have the fields ``InputSourceARN`` and ``SchemaName`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-inputsourceconfig
        '''
        result = self._values.get("input_source_config")
        assert result is not None, "Required property 'input_source_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.InputSourceProperty]]], result)

    @builtins.property
    def output_source_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.OutputSourceProperty]]]:
        '''A list of ``OutputSource`` objects, each of which contains fields ``OutputS3Path`` , ``ApplyNormalization`` , and ``Output`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-outputsourceconfig
        '''
        result = self._values.get("output_source_config")
        assert result is not None, "Required property 'output_source_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.OutputSourceProperty]]], result)

    @builtins.property
    def resolution_techniques(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.ResolutionTechniquesProperty]:
        '''An object which defines the ``resolutionType`` and the ``ruleBasedProperties`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-resolutiontechniques
        '''
        result = self._values.get("resolution_techniques")
        assert result is not None, "Required property 'resolution_techniques' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.ResolutionTechniquesProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role.

        Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workflow_name(self) -> builtins.str:
        '''The name of the workflow.

        There cannot be multiple ``DataIntegrationWorkflows`` with the same name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-workflowname
        '''
        result = self._values.get("workflow_name")
        assert result is not None, "Required property 'workflow_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMatchingWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSchemaMapping(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_entityresolution.CfnSchemaMapping",
):
    '''Creates a schema mapping, which defines the schema of the input customer records table.

    The ``SchemaMapping`` also provides AWS Entity Resolution with some metadata about the table, such as the attribute types of the columns and which columns to match on.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html
    :cloudformationResource: AWS::EntityResolution::SchemaMapping
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_entityresolution as entityresolution
        
        cfn_schema_mapping = entityresolution.CfnSchemaMapping(self, "MyCfnSchemaMapping",
            mapped_input_fields=[entityresolution.CfnSchemaMapping.SchemaInputAttributeProperty(
                field_name="fieldName",
                type="type",
        
                # the properties below are optional
                group_name="groupName",
                match_key="matchKey"
            )],
            schema_name="schemaName",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        mapped_input_fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchemaMapping.SchemaInputAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        schema_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param mapped_input_fields: A list of ``MappedInputFields`` . Each ``MappedInputField`` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.
        :param schema_name: The name of the schema. There cannot be multiple ``SchemaMappings`` with the same name.
        :param description: A description of the schema.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b85e0c42d14b4681c4f948114178ba1c1a3d4eee3aed6f96a55a11624008b9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaMappingProps(
            mapped_input_fields=mapped_input_fields,
            schema_name=schema_name,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b9491a9fbe1bcc73169aa2c5f87a0aa33490b2a27265d62378a0b8d687f933)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6cdea55ce60d609a9a8c6b9d013e19c06452d227285f779bdf5724280e9a7c4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time of this SchemaMapping got created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrSchemaArn")
    def attr_schema_arn(self) -> builtins.str:
        '''The SchemaMapping arn associated with the Schema.

        :cloudformationAttribute: SchemaArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The time of this SchemaMapping got last updated at.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="mappedInputFields")
    def mapped_input_fields(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchemaMapping.SchemaInputAttributeProperty"]]]:
        '''A list of ``MappedInputFields`` .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchemaMapping.SchemaInputAttributeProperty"]]], jsii.get(self, "mappedInputFields"))

    @mapped_input_fields.setter
    def mapped_input_fields(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchemaMapping.SchemaInputAttributeProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__582cf934b619d5bd24742b664e76c854f1f5f978250eb7c8b069eea939a36d15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mappedInputFields", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        '''The name of the schema.'''
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e60d6efab6fe4d38d530b8bf0a9230db6dd3ba98b56dfb812bea973c5fb07fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the schema.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45aaef5bf11ec7b2bf48bfb15f820ed7b15b4ae8a5c668df859ffb21058df8e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb00d34c669b02d875a4d122d6517a31b19c4fe763a25a3d3e60b62a88dc81c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_entityresolution.CfnSchemaMapping.SchemaInputAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_name": "fieldName",
            "type": "type",
            "group_name": "groupName",
            "match_key": "matchKey",
        },
    )
    class SchemaInputAttributeProperty:
        def __init__(
            self,
            *,
            field_name: builtins.str,
            type: builtins.str,
            group_name: typing.Optional[builtins.str] = None,
            match_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object containing ``FieldName`` , ``Type`` , ``GroupName`` , and ``MatchKey`` .

            :param field_name: A string containing the field name.
            :param type: The type of the attribute, selected from a list of values.
            :param group_name: Instruct AWS Entity Resolution to combine several columns into a unified column with the identical attribute type. For example, when working with columns such as first_name, middle_name, and last_name, assigning them a common ``GroupName`` will prompt AWS Entity Resolution to concatenate them into a single value.
            :param match_key: A key that allows grouping of multiple input attributes into a unified matching group. For example, let's consider a scenario where the source table contains various addresses, such as business_address and shipping_address. By assigning the ``MatchKey`` *Address* to both attributes, AWS Entity Resolution will match records across these fields to create a consolidated matching group. If no ``MatchKey`` is specified for a column, it won't be utilized for matching purposes but will still be included in the output table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_entityresolution as entityresolution
                
                schema_input_attribute_property = entityresolution.CfnSchemaMapping.SchemaInputAttributeProperty(
                    field_name="fieldName",
                    type="type",
                
                    # the properties below are optional
                    group_name="groupName",
                    match_key="matchKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d608d145fae97c0a85e57f344f3785207a465f180330e5a7bec62b41172c661e)
                check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
                check_type(argname="argument match_key", value=match_key, expected_type=type_hints["match_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_name": field_name,
                "type": type,
            }
            if group_name is not None:
                self._values["group_name"] = group_name
            if match_key is not None:
                self._values["match_key"] = match_key

        @builtins.property
        def field_name(self) -> builtins.str:
            '''A string containing the field name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-fieldname
            '''
            result = self._values.get("field_name")
            assert result is not None, "Required property 'field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the attribute, selected from a list of values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_name(self) -> typing.Optional[builtins.str]:
            '''Instruct AWS Entity Resolution to combine several columns into a unified column with the identical attribute type.

            For example, when working with columns such as first_name, middle_name, and last_name, assigning them a common ``GroupName`` will prompt AWS Entity Resolution to concatenate them into a single value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-groupname
            '''
            result = self._values.get("group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def match_key(self) -> typing.Optional[builtins.str]:
            '''A key that allows grouping of multiple input attributes into a unified matching group.

            For example, let's consider a scenario where the source table contains various addresses, such as business_address and shipping_address. By assigning the ``MatchKey`` *Address* to both attributes, AWS Entity Resolution will match records across these fields to create a consolidated matching group. If no ``MatchKey`` is specified for a column, it won't be utilized for matching purposes but will still be included in the output table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-matchkey
            '''
            result = self._values.get("match_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaInputAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_entityresolution.CfnSchemaMappingProps",
    jsii_struct_bases=[],
    name_mapping={
        "mapped_input_fields": "mappedInputFields",
        "schema_name": "schemaName",
        "description": "description",
        "tags": "tags",
    },
)
class CfnSchemaMappingProps:
    def __init__(
        self,
        *,
        mapped_input_fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchemaMapping.SchemaInputAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
        schema_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchemaMapping``.

        :param mapped_input_fields: A list of ``MappedInputFields`` . Each ``MappedInputField`` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.
        :param schema_name: The name of the schema. There cannot be multiple ``SchemaMappings`` with the same name.
        :param description: A description of the schema.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_entityresolution as entityresolution
            
            cfn_schema_mapping_props = entityresolution.CfnSchemaMappingProps(
                mapped_input_fields=[entityresolution.CfnSchemaMapping.SchemaInputAttributeProperty(
                    field_name="fieldName",
                    type="type",
            
                    # the properties below are optional
                    group_name="groupName",
                    match_key="matchKey"
                )],
                schema_name="schemaName",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbadfeefbc588fc98477889c4f0b74bc9f51ac6d9fd8188d64b6ad629a494dad)
            check_type(argname="argument mapped_input_fields", value=mapped_input_fields, expected_type=type_hints["mapped_input_fields"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mapped_input_fields": mapped_input_fields,
            "schema_name": schema_name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def mapped_input_fields(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSchemaMapping.SchemaInputAttributeProperty]]]:
        '''A list of ``MappedInputFields`` .

        Each ``MappedInputField`` corresponds to a column the source data table, and contains column name plus additional information that AWS Entity Resolution uses for matching.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-mappedinputfields
        '''
        result = self._values.get("mapped_input_fields")
        assert result is not None, "Required property 'mapped_input_fields' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSchemaMapping.SchemaInputAttributeProperty]]], result)

    @builtins.property
    def schema_name(self) -> builtins.str:
        '''The name of the schema.

        There cannot be multiple ``SchemaMappings`` with the same name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-schemaname
        '''
        result = self._values.get("schema_name")
        assert result is not None, "Required property 'schema_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMatchingWorkflow",
    "CfnMatchingWorkflowProps",
    "CfnSchemaMapping",
    "CfnSchemaMappingProps",
]

publication.publish()

def _typecheckingstub__8c9e9b620b89ac2aae774eb42384e0472b5a13eeb28983708b164b2400ebcd39(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    input_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.InputSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    output_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.OutputSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resolution_techniques: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.ResolutionTechniquesProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    workflow_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a2bf1cfd69ad77cafcf7b6d5e0508159e0ece5385e2b3a0808436e336abbfcc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83843fc5000b4b7c1f325390bceaadeeec20658b2de2de2143a3d987e3c49953(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46336e1b290b62290456cef0086653d1bf7bde247391e85b7b88570883b249d6(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.InputSourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6752620fe10a272a45c22eb2493e5e30fcac8bb82fcc95b6f46271727dadc72(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.OutputSourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfbb583351458ecc2896a0f04d4bae86260e8762b28c2687fe570562260a9a48(
    value: typing.Union[_IResolvable_da3f097b, CfnMatchingWorkflow.ResolutionTechniquesProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68dfd5a70e354a050b7085c6c4cc4520862c51d487a8a8e920928f222fa1894(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e33fb06ce08c9c2af24c4cb3e68018f92d9bc69c0f62bc965ba1640232fd73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146028c4441df7c65ea8aba2981fe23a6e2fda2af137f4c78d1c5c84d63a3b1a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7a7896d7bea53a4e2ffc9445d9a42b8864f5ac9a6cf43c3b27fe3c77bd39a83(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a18bfef9ee8ade2fff3913e22cf37d98f5880893c2204caa684a7f3831327af(
    *,
    input_source_arn: builtins.str,
    schema_arn: builtins.str,
    apply_normalization: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006a3c9280759d8123ca560d0c7cfef20e64f8703bb04be12b8a7e08728768e5(
    *,
    name: builtins.str,
    hashed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92bb2dc25f018fe0017c7ab79f29b2fdfb4238d6fb1293a9cd606b9f93976df8(
    *,
    output: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.OutputAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    output_s3_path: builtins.str,
    apply_normalization: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c6ea89cbe5bb10bb721c60f7c5951a6a56729058a7b00d3dd16b091aa63ab9(
    *,
    resolution_type: typing.Optional[builtins.str] = None,
    rule_based_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.RuleBasedPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d1f97c0110dea5fb9a8413e199ae25878eedad10521ad056ca772f31ddb8ba(
    *,
    attribute_matching_model: builtins.str,
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad893f1319125d264f9286a93c40cd8616031944a24803bccedd15e3233ef0f(
    *,
    matching_keys: typing.Sequence[builtins.str],
    rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be3b46399b509a45bb640cf4a70ab0714322917a6d3dc4c241cb16ab2d1dbb0(
    *,
    input_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.InputSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    output_source_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.OutputSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resolution_techniques: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchingWorkflow.ResolutionTechniquesProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    workflow_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b85e0c42d14b4681c4f948114178ba1c1a3d4eee3aed6f96a55a11624008b9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    mapped_input_fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchemaMapping.SchemaInputAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    schema_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b9491a9fbe1bcc73169aa2c5f87a0aa33490b2a27265d62378a0b8d687f933(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6cdea55ce60d609a9a8c6b9d013e19c06452d227285f779bdf5724280e9a7c4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582cf934b619d5bd24742b664e76c854f1f5f978250eb7c8b069eea939a36d15(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSchemaMapping.SchemaInputAttributeProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e60d6efab6fe4d38d530b8bf0a9230db6dd3ba98b56dfb812bea973c5fb07fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45aaef5bf11ec7b2bf48bfb15f820ed7b15b4ae8a5c668df859ffb21058df8e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb00d34c669b02d875a4d122d6517a31b19c4fe763a25a3d3e60b62a88dc81c6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d608d145fae97c0a85e57f344f3785207a465f180330e5a7bec62b41172c661e(
    *,
    field_name: builtins.str,
    type: builtins.str,
    group_name: typing.Optional[builtins.str] = None,
    match_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbadfeefbc588fc98477889c4f0b74bc9f51ac6d9fd8188d64b6ad629a494dad(
    *,
    mapped_input_fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchemaMapping.SchemaInputAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    schema_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
