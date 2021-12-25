# Declaration of region variable

variable "region" {
  type = string
  default = "ap-south-1"
}

variable "tag_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "webserver"
}