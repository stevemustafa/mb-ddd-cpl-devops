from aws_cdk import (
    aws_ec2 as ec2,
    core
)


class InfraStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        self.vpc = ec2.Vpc
