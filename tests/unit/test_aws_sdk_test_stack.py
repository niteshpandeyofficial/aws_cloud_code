import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_sdk_test.aws_sdk_test_stack import AwsSdkTestStack


def test_sqs_queue_created():
    app = core.App()
    stack = AwsSdkTestStack(app, "aws-sdk-test")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = AwsSdkTestStack(app, "aws-sdk-test")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
