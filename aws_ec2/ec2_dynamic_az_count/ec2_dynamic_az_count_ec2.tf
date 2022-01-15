# Defining AWS Instance resource
resource "aws_instance" "public_web" {
  count                  = var.instance_count
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.micro"
  availability_zone      = local.az_names[count.index % length(local.az_names)]
  subnet_id              = aws_subnet.public[count.index % length(local.az_names)].id
  vpc_security_group_ids = [aws_security_group.public_sg.id]
  key_name               = "ssh-key"

  # Terraform user data startup script reference 
  user_data = file("${path.module}/startup.sh")
  root_block_device {
    delete_on_termination = true
  }
  # Declaration of variable along with concatenation of Availablity zone
  tags = merge(var.default_tags,
    {
      Name = "${var.ec2_name}${count.index + 1}_${local.az_names[count.index % length(local.az_names)]}"
    }
  )
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
# Creating a keypair
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/key_pair
resource "aws_key_pair" "ssh-key" {
  key_name   = "ssh-key"
  public_key = file(pathexpand("~/.ssh/id_rsa.pub"))
}