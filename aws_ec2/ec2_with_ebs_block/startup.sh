#!/bin/bash
# Installing APACHE
sudo apt-get update
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2

# The best way is to run that script after \resource "aws_volume_attachment"\ created
DEVICE="/dev/xvdh"
# Get device id
DEVICE_FS=`sudo lsblk -o UUID -d ${DEVICE} -n`
# Create a file system on the volume if one does not already exist
if [ "`echo -n $DEVICE_FS`" == "" ] ; then
        sudo mkfs.ext4 ${DEVICE}
fi
MOUNT_POINT=/newvolume/
# Create a mount point directory
sudo mkdir $MOUNT_POINT
# Mount the device
sudo mount $DEVICE $MOUNT_POINT
# Automatically mount an attached volume after reboot 
# Backup fstab
sudo cp /etc/fstab /etc/fstab.orig
# Setup auto mount on reboot
echo "UUID=${DEVICE_FS} $MOUNT_POINT xfs defaults,nofail 0 2" | sudo tee -a /etc/fstab


# Change user for data operations / Non mandatory
sudo chown -R ubuntu:ubuntu $MOUNT_POINT

##### Constants
TITLE="System Information for $(hostname -f) via Terraform"
RIGHT_NOW="$(date +"%x %r %Z")"
TIME_STAMP="Updated on $RIGHT_NOW by $USER"
output=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)

### Functions
drive_space()
{
    echo "<h2>Filesystem space of $DEVICE</h2>"
    echo "<pre>"
    df -h $MOUNT_POINT
    echo "</pre>"
}

##### Main

cat << EOF  | sudo tee  /var/www/html/index.html
  <html>
  <head>
      <title>$TITLE</title>
  </head>

  <body>
      <h1>$TITLE</h1>
      <h2>PUBLIC IP of the instance is $output</h2>
      <p>$TIME_STAMP</p>
      $(drive_space)
  </body>
  </html>
EOF