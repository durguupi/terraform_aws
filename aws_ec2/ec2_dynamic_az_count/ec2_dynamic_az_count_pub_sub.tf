# Public Subnet with Default Route to Internet Gateway
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet
resource "aws_subnet" "public" {
  count                   = length(local.az_names)
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = cidrsubnet(var.base_cidr, 8, count.index)
  map_public_ip_on_launch = "true"
  availability_zone       = local.az_names[count.index]

  tags = merge(var.default_tags,
    {
      Name = "Public-subnet-${local.az_names[count.index]}"
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
  count          = length(aws_subnet.public)
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}
