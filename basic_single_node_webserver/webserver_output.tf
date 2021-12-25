# Description for the output of Instance ID

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.webserver.id
}

# Description for the output of Instance Public IP

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.webserver.public_ip
}