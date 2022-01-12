# Public Subnet with Default Route to Internet Gateway
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet
resource "aws_subnet" "public" {
  for_each                = { for idx, az_name in local.az_names : idx => az_name }
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = cidrsubnet(var.base_cidr, 8, each.key)
  map_public_ip_on_launch = "true"
  # Here the each.key refers to index and it starts with 0 and increments to number of AZ present
  # Here it will be 0,1,2,3 (aws_subnet.public["0"] .... aws_subnet.public["3"]) will be created
  availability_zone = local.az_names[each.key]

  tags = merge(var.default_tags,
    {
      Name = "Public-subnet-${local.az_names[each.key]}"
    }
  )
}

# main_vpc Internal Gateway for VPC
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/internet_gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main_vpc.id
  tags = merge(var.default_tags,
    {
      Name = "Default IGW"
    }
  )
}

# Route Table for Public Subnet
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = merge(var.default_tags,
    {
      Name = "Public Route Table"
    }
  )
}

# Association between Public Subnet and Public Route Table
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table_association
resource "aws_route_table_association" "public" {
  for_each       = { for idx, subnet in aws_subnet.public : idx => subnet }
  subnet_id      = each.value.id
  route_table_id = aws_route_table.public.id
}
