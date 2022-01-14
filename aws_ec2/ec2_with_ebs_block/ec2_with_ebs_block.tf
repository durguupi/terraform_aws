# AWS VOLUME ATTACHEMENT
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/volume_attachment
resource "aws_volume_attachment" "this" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.this.id
  instance_id = aws_instance.public_web.id
#   force_detach = true
}

# aws_ebs_volume
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ebs_volume
resource "aws_ebs_volume" "this" {
  availability_zone = local.az_names[0]
  size              = 1
  tags = merge(var.default_tags,
    {
      Name = "${var.ec2_name}_ebsvolume_${local.az_names[0]}"
    }
  )
}


