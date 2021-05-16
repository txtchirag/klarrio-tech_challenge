#!/bin/bash

#pull image from docker hub
docker pull eclipse-mosquitto 

# run mosquitto container with ports 1883(remote) and 9001(websocket) exposed  
docker run -d --net=host --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto 

#change config file to set listener on ports and configure websocket and anonymous to true
docker cp mosquitto:/mosquitto/config/mosquitto.conf .
echo -e 'allow_anonymous true\nlistener 1883\nprotocol mqtt\nlistener 9001\nprotocol websockets\n' >> mosquitto.conf
docker cp mosquitto.conf mosquitto:/mosquitto/config/mosquitto.conf

# restart container
docker stop mosquitto
docker start mosquitto

nohup python3 dynamodb.py > dynamodb.log $
