"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
from pulumi_aws.ec2 import availability_zone_group

# Providing the size of the instance type
size = 't2.micro'
tag_name = "webserver"
# Getting the AMI of latest Ubuntu 
ubuntu = aws.ec2.get_ami(
    most_recent=True,
    filters=[
        aws.ec2.GetAmiFilterArgs(
            name="name",
            values=["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"],
        ),
        aws.ec2.GetAmiFilterArgs(
            name="virtualization-type",
            values=["hvm"],
        ),
    ],
    owners=["099720109477"])

# Getting the Availablity Zones in region
available = aws.get_availability_zones(state="available")

# Defining the security group Enabling port 80 and port 22
group = aws.ec2.SecurityGroup('webserver-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ],
    egress=[
        { 'protocol': '-1', 'from_port': 0, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0'] },
    ])

# Defining the user_data 
user_data = """#!/bin/bash -x
echo "test of user_data"| sudo tee /tmp/user_data.log
sudo apt update
sudo apt install -y apache2
sudo ufw allow 'Apache'
sudo systemctl start apache2
sudo systemctl enable apache2
echo "<h1>Deployed via PULUMI</h1>" | sudo tee /var/www/html/index.html
output=$(curl http://169.254.169.254/latest/meta-data/local-ipv4)
echo "<h2>Private IP of the instance is $output</h2>" | sudo tee -a /var/www/html/index.html
"""

# deployer = aws.ec2.KeyPair("deployer", public_key="")

# Defining the Ec2 instance 
server = aws.ec2.Instance('webserver-www',
    instance_type=size,
    vpc_security_group_ids=[group.id], # reference security group from above
    user_data=user_data, # User_data
    ami=ubuntu.id,
    availability_zone = available.names[0],## Deploy the resource in Availablity zone 1 
    #key_name=deployer,
    tags={
        "Name": tag_name + "-" + available.names[0],
    }
    ) 

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)