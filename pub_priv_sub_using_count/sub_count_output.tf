# Referencing output of Public subnet
output "Public_subnet" {
  value = {
    for i in aws_subnet.public[*] :
    i.tags.Name => i.cidr_block
  }
}

# Referencing output of Private subnet
output "Private_subnet" {
  value = {
    for i in aws_subnet.private[*] :
    i.tags.Name => i.cidr_block
  }
}