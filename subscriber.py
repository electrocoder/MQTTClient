"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/meseiot/iot-examples

Date: 12.11.2022

File: This script is MQTT Subscriber Client
"""

import tkinter as tk
from datetime import datetime
import paho.mqtt.client as mqtt


class Subscriber:
    def __init__(self, main_window):
        self.main_window = main_window
        self.client = None

        self.on_message_count = 0
        self.publish_message_count = 0

        self.topic = None
        self.message = None

    def on_connect(self, client, userdata, flags, rc):
        self.main_window.connect_status_text.set(
            "Connected | Message: %s | Publish: %s" % (
                self.on_message_count, self.publish_message_count))

    def on_disconnect(self, client, userdata, rc):
        self.mqtt_disconnect()

    def on_message(self, client, userdata, msg):
        self.topic = msg.topic
        try:
            self.message = msg.payload.decode('utf8')
        except:
            self.message = None
        if self.message:
            if self.main_window.msg_filter:
                if self.main_window.entry_msg_filter_text.get() in self.message or self.main_window.entry_msg_filter_text.get() in self.topic:
                    self.main_window.listbox_message.insert(tk.END,
                                                            ">{} {}: {} {}\n".format(
                                                                self.on_message_count,
                                                                datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                                                self.topic,
                                                                self.message))
                    self.main_window.listbox_message.see("end")
                    self.on_message_count += 1
            else:
                self.main_window.listbox_message.insert(tk.END,
                                                        ">{} {}: {} {}\n".format(
                                                            self.on_message_count,
                                                            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                                            self.topic,
                                                            self.message))
                self.main_window.listbox_message.see("end")
                self.on_message_count += 1

        self.main_window.connect_status_text.set(
            "Connected | Message: %s | Publish: %s" % (
                self.on_message_count, self.publish_message_count))

    def connect_start(self, name, broker, port, username, password):
        self.client = mqtt.Client()
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.username_pw_set(username, password)
        self.client.connect(broker, int(port), 60)
        return True

    def connect_stop(self):
        self.client.disconnect()
        self.client = None
        return True

    def subscribe_start(self, topic):
        self.client.subscribe(topic, qos=0)
        self.client.loop_start()

    def publish_start(self, topic, msg):
        self.client.publish(topic, msg)
        self.publish_message_count += 1

    def mqtt_disconnect(self):
        if self.connect_stop():
            self.main_window.connect_status_text.set("Disconnect")
            self.main_window.button_connect["state"] = tk.NORMAL
            self.main_window.button_connect["text"] = "Connect"
            self.main_window.button_disconnect["state"] = tk.DISABLED
            self.main_window.button_subscribe_topic[
                "state"] = tk.DISABLED
            self.main_window.button_publish_topic[
                "state"] = tk.DISABLED
            self.main_window.button_add_subscribe_topic["state"] = tk.DISABLED

            self.main_window.connect_status_text.set(
                "Disconnect | Message: %s | Publish: %s" % (
                    self.on_message_count, self.publish_message_count))
