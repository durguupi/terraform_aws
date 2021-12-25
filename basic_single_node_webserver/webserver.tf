# Defining AWS Instance resource

resource "aws_instance" "webserver" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
  availability_zone = data.aws_availability_zones.aws_az.names[0]
  
# Terraform user data startup script reference 
  user_data = file("${path.module}/startup.sh")

# Declaration of variable along with concatenation of Availablity zone
  tags = {
    Name = "${var.tag_name}_${data.aws_availability_zones.aws_az.names[0]}"
  }
}

# Defining datasource to get ubuntu images

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

# This must be in the region selected on the AWS provider.

data "aws_availability_zones" "aws_az" {
  state = "available" 
}