# Private Subnet with Default Route to NAT Gateway
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet
resource "aws_subnet" "private" {
  for_each          = { for idx, az_name in local.az_names : idx => az_name }
  vpc_id            = aws_vpc.main_vpc.id
  cidr_block        = cidrsubnet(var.base_cidr, 8, each.key + length(local.az_names))
  availability_zone = local.az_names[each.key]

  tags = merge(var.default_tags,
    {
      Name = "Private-subnet-${local.az_names[each.key]}"
    }
  )
}

# Route Table for Private Subnet
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main_vpc.id

  tags = merge(var.default_tags,
    {
      Name = "Private Route Table"
    }
  )
}

# Association between Public Subnet and Public Route Table
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table_association
resource "aws_route_table_association" "private" {
  for_each       = { for idx, subnet in aws_subnet.private : idx => subnet }
  subnet_id      = each.value.id
  route_table_id = aws_route_table.private.id
}
