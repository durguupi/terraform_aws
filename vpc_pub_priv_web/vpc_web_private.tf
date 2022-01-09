# Defining AWS Instance resource

resource "aws_instance" "private_web" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.micro"
  availability_zone      = data.aws_availability_zones.aws_az.names[1]
  subnet_id              = aws_subnet.private.id
  vpc_security_group_ids = [aws_security_group.private_sg.id]
  key_name               = "ssh-key"

  # Terraform user data startup script reference 
  user_data = file("${path.module}/startup_private.sh")

  # Declaration of variable along with concatenation of Availablity zone
  tags = {
    Name        = "private_${var.ec2_name}_${data.aws_availability_zones.aws_az.names[1]}"
    Environment = var.env_name
  }
}

