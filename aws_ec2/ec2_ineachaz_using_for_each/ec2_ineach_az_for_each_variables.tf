# Declaration of region variable
variable "region" {
  type    = string
  default = "us-east-2"
}
# EC2 tag name
variable "ec2_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "webserver"
}

# CIDR block for the VPC
variable "base_cidr" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}


variable "default_tags" {
  description = "Tags for infrastructure resources"
  type        = map(string)
  default = {
    Name : "Value",
    Project : "Terraform-AWS",
    Environment : "Dev",
    ManagedBy : "Terraform",
    CreatedBy : "Team-1"
  }
}
 