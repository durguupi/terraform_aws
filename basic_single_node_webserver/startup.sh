#!/bin/bash
# echo "test of user_data"| sudo tee /tmp/user_data.log
# curl http://169.254.169.254/latest/meta-data/local-ipv4 | sudo tee -a /tmp/user_data.log
sudo apt-get update
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
echo "<h1>Deployed via Terraform</h1>" | sudo tee /var/www/html/index.html
# curl http://169.254.169.254/latest/meta-data/local-ipv4 | sudo tee -a /var/www/html/index.html
output=$(curl http://169.254.169.254/latest/meta-data/local-ipv4)
echo "<h2>Private IP of the instance is $output</h2>" | sudo tee -a /var/www/html/index.html