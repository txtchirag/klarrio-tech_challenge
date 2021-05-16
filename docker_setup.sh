#!/bin/bash

# setup docker https://docs.docker.com/engine/install/ubuntu/
# remove earlier versions
sudo apt-get remove docker docker-engine docker.io containerd runc


# add stable docker repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# install docker engine
sudo apt-get update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io

# post install steps
sudo usermod -aG docker $USER
sudo systemctl restart docker.service

