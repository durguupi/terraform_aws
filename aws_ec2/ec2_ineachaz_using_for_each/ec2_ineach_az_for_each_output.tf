# Referencing output of Public subnet
output "Public_subnet_Names" {
  value = { for k, v in aws_subnet.public :
  v.tags.Name => v.cidr_block }
}


output "webserver_public_ip" {
  description = "Public IP address of the EC2 webserver instances"
  value = {
    for k, v in aws_instance.public_web :
    v.tags.Name => v.public_ip
  }
}

output "webserver_private_ip" {
  description = "Public IP address of the EC2 webserver instances"
  value = {
    for k,v in aws_instance.public_web :
    v.tags.Name => v.private_ip
  }
}