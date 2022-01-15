#!/bin/bash
sudo apt-get update
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
EC2_AVAIL_ZONE=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
EC2_REGION="`echo \"$EC2_AVAIL_ZONE\" | sed 's/[a-z]$//'`"
echo "<h1>Deployed via Terraform in $EC2_REGION </h1>" | sudo tee /var/www/html/index.html
OUTPUT=$(curl http://169.254.169.254/latest/meta-data/local-ipv4)
echo "<h2>Private IP of the instance is $OUTPUT</h2>" | sudo tee -a /var/www/html/index.html
echo "<h2>Availability Zone of the instance is $EC2_AVAIL_ZONE</h2>" | sudo tee -a /var/www/html/index.html