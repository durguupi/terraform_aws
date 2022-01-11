# PUBLIC SECURIT GROUP ATTACHED TO PUBLIC WEBSERVER
resource "aws_security_group" "public_sg" {
  name   = "Public Secuity Group"
  vpc_id = aws_vpc.main_vpc.id
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  //If you do not add this rule, you can not reach the Webserver
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = [var.cidr_vpc]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "Public SG"
    Environment = var.env_name
  }
}


# PRIVATE SECURIT GROUP ATTACHED TO PRIVATE WEBSERVER
resource "aws_security_group" "private_sg" {
  name   = "Private Security Group"
  vpc_id = aws_vpc.main_vpc.id
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.public_subnet_cidr]
  }
  //Allowing PING traffic from Public subnet
  egress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = [var.cidr_vpc]
  }
  tags = {
    Name        = "Private SG"
    Environment = var.env_name
  }
}
