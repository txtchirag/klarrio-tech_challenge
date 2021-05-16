#!/usr/bin/env python3
import json
import time
from decimal import Decimal as Decimal

import boto3
import paho.mqtt.client as mqtt

# dynamodb
dynamoDB = boto3.resource('dynamodb','us-east-1')
table = dynamoDB.Table("mqtt")


# Subscriber
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("#")


def on_message(client, userdata, msg):
    if msg.payload:
        topic = msg.topic
        try:
            message = json.loads(msg.payload.decode("utf-8"))
        except json.JSONDecodeError as e:
            print("JSONDecodeError")
            return
        try:
            DeviceID = message['DeviceID']
        except KeyError as e:
            print("KeyError")
            return
        time_val = Decimal(time.time())
        print(DeviceID, time_val, topic, message)

        #Update dynamoDB table
        table.put_item(Item={'DeviceID': DeviceID, 'time': time_val, 'topic': topic, 'message': message})


client = mqtt.Client()
client.connect("0.0.0.0")
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
