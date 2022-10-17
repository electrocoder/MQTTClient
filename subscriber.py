import logging

import paho.mqtt.client as mqtt
import time
import json


class Subscriber:
    def __init__(self, client):
        self.topic = "mese/iot/response"
        self.sid = 0

        self.client = client

        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.username_pw_set("iothookpublic", "iothookpublic")

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(self.topic, qos=1)

    def basla(self):
        self.client.connect("www.iothook.com", 1883, 60)
        self.client.loop_start()

    def dur(self):
        self.client.disconnect()

    def on_disconnect(self, client, userdata, rc):
        print("disconnet...")
        logging.info("disconnecting reason  " + str(rc))
        self.client.connected_flag = False
        self.client.disconnect_flag = True

    def on_message(self, client, userdata, msg):
        print(
            msg.topic + " " + msg.payload.decode('utf8') + " " + str(self.sid))
        print("")
        self.sid += 1
        return "aaa"
