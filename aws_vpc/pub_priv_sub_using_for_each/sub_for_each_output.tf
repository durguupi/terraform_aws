# Referencing output of Public subnet
# The aws_subnet.public generated will be a map, with key as each subnet and values of its tag names and 
# cidr_block is referenced here.
output "Public_subnet_Names" {
  value = { for k, v in aws_subnet.public :
  v.tags.Name => v.cidr_block }
}

output "Private_subnet_Names" {
  value = { for k, v in aws_subnet.private :
  v.tags.Name => v.cidr_block }
}