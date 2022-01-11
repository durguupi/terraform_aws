# Declaration of region variable
variable "region" {
  type    = string
  default = "ap-south-1"
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
 