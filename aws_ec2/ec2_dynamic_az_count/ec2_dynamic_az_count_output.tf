# Referencing output of Public subnet
output "Public_subnet" {
  value = {
    for i in aws_subnet.public[*] :
    i.tags.Name => i.cidr_block
  }
}

output "webserver_public_ip" {
  description = "Public IP address of the EC2 webserver instances"
  value = {
    for i in aws_instance.public_web[*] :
    i.tags.Name => i.public_ip
  }
}

output "webserver_private_ip" {
  description = "Public IP address of the EC2 webserver instances"
  value = {
    for i in aws_instance.public_web[*] :
    i.tags.Name => i.private_ip
  }
}