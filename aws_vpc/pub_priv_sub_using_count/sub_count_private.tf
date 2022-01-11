# Private Subnet with Default Route to NAT Gateway
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet
resource "aws_subnet" "private" {
  count             = length(data.aws_availability_zones.aws_az.names)
  vpc_id            = aws_vpc.main_vpc.id
  cidr_block        = cidrsubnet(var.base_cidr, 8, count.index + length(data.aws_availability_zones.aws_az.names))
  availability_zone = data.aws_availability_zones.aws_az.names[count.index]

  tags = merge(var.default_tags,
    {
      Name = "Private-subnet-${data.aws_availability_zones.aws_az.names[count.index]}"
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
  count          = length(aws_subnet.private)
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private.id
}
