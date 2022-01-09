#!/bin/bash
echo "test of user_data"| sudo tee /tmp/user_data.log
output=$(curl http://169.254.169.254/latest/meta-data/local-ipv4)
echo "Private IP of the instance is $output" | sudo tee -a /tmp/user_data.log
