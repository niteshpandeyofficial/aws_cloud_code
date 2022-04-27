#!/usr/bin/env python3

from aws_cdk import core

from aws_sdk_test.aws_sdk_test_stack import AwsSdkTestStack


app = core.App()
AwsSdkTestStack(app, "aws-sdk-test")

app.synth()
