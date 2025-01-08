#!/bin/bash

# This scrip will setup docker in your Ubuntu system

# Version 2.0
# Author: Dhruv Jain

# Installing Docker

echo "####### Installing Docker #######"

echo "####### Updating the system #######"
sudo apt-get update

echo "####### Installing Docker #######"
sudo apt install docker.io -y

sleep 2
echo "####### restart docker #######"
sudo systemctl restart docker

sleep 6
echo "####### Enable docker #######"
sudo systemctl enable docker

sleep 4

echo "####### Adding user to docker group #######"
sudo usermod -aG docker $USER

echo "####### Docker is Installed ######"

echo "################ Installing docker-compose ##############"

sudo apt-get install docker-compose-v2 -y
sudo apt  install docker-compose -y

echo "################ Docker-compose installed ###############"
echo "To Run flask-app run : - "
echo "docker-compose up -d"
newgrp docker
exit 1