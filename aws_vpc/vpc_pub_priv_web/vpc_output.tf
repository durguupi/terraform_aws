# Description for the output of Instance ID

output "vpc_id" {
  description = "VPC ID of the EC2 instance"
  value       = aws_vpc.main_vpc.id
}

# Description for the output of Instance Public IP

output "webserver_public_ip" {
  description = "Public IP address of the EC2 webserver instance"
  value       = aws_instance.public_web.public_ip
}

# Description for the output of Webserver Instance Private IP

output "webserver_private_ip" {
  description = "Private IP address of the EC2 webserver instance"
  value       = aws_instance.public_web.private_ip
}

# Description for the output of Instance Private IP

output "EC2_instance_IP_in_privatesubnet" {
  description = "Private IP address of the EC2 instance in private subnet"
  value       = aws_instance.private_web.private_ip
}