# Declaration of region variable
variable "region" {
  type    = string
  default = "ap-south-1"
}
# Environment name
variable "env_name" {
  description = "Value of the Name tag for the Environment"
  type        = string
  default     = "dev"
}
# EC2 tag name
variable "ec2_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "webserver"
}
# CIDR block for the VPC
variable "cidr_vpc" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}
# CIDR block for the Public subnet
variable "public_subnet_cidr" {
  description = "CIDR block for the Public subnet"
  default     = "10.0.1.0/24"
}
# CIDR block for the Private subnet
variable "private_subnet_cidr" {
  description = "CIDR block for the Private subnet"
  default     = "10.0.2.0/24"
}