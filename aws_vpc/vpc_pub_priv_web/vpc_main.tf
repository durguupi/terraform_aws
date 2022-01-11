# Main VPC
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc

resource "aws_vpc" "main_vpc" {
  cidr_block           = var.cidr_vpc
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name        = "Main VPC"
    Environment = var.env_name
  }
}

# This must be in the region selected on the AWS provider.

data "aws_availability_zones" "aws_az" {
  state = "available"
}