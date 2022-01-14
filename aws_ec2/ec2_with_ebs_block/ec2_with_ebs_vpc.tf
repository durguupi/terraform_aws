# Main VPC
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc

resource "aws_vpc" "main_vpc" {
  cidr_block           = var.base_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = merge(var.default_tags,
    {
      Name = "Main VPC"
    }
  )
}

# This must be in the region selected on the AWS provider.
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/availability_zones
data "aws_availability_zones" "aws_az" {
  state = "available"
}

# Assiging Az-names to local variable
locals {
  az_names = data.aws_availability_zones.aws_az.names
}