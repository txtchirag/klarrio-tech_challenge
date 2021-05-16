#!/bin/bash

# install dependencies
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl gnupg lsb-release net-tools python3-pip awscli
pip install boto3 paho-mqtt 
pip install --upgrade awscli

