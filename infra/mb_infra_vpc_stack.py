from aws_cdk import core

import aws_cdk.aws_ec2 as ec2

class MbVpcStack(self)
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpx = ec2.Vpc(self, "VPC",
                           max_azs = 3,
                           cidr="10.10.0.0/16",
                           #2 private sbnets and 1 public subnet
        ec2.)
