#!/usr/bin/env python3

import aws_cdk as cdk

from aws_sdk_test.aws_sdk_test_stack import AwsSdkTestStack


app = cdk.App()
AwsSdkTestStack(app, "aws-sdk-test")

app.synth()
