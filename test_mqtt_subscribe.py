import logging

import paho.mqtt.client as mqtt
import time
import json


topic = "mese/iot/response"
sid = 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic, qos=1)


def on_disconnect(client, userdata, rc):
    print("disconnet...")
    logging.info("disconnecting reason  " + str(rc))
    client.connected_flag = False
    client.disconnect_flag = True


def on_message(client, userdata, msg):
    global sid
    print(msg.topic + " " + msg.payload.decode('utf8') + " " + str(sid))
    print("")
    sid += 1


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set("iothookpublic", "iothookpublic")

client.connect("www.iothook.com", 1883, 60)

client.loop_forever()
