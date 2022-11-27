"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is MQTT Subscriber Client
"""

import tkinter as tk


class Subscriber:
    def __init__(self, main_window, client):
        self.main_window = main_window
        self.client = client

        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

        self.on_message_count = 0
        self.publish_message_count = 0

        self.topic = None
        self.message = None

    def on_connect(self, client, userdata, flags, rc):
        self.main_window.connect_status_text.set(
            "Connected | Message: %s | Publish: %s" % (
                self.on_message_count, self.publish_message_count))

    def on_disconnect(self, client, userdata, rc):
        self.main_window.connect_status_text.set(
            "Disconnect | Message: %s | Publish: %s" % (
                self.on_message_count, self.publish_message_count))

    def on_message(self, client, userdata, msg):
        self.topic = msg.topic
        self.message = msg.payload.decode('utf8')
        if self.main_window.msg_filter:
            if self.main_window.entry_msg_filter_text.get() in self.message:
                self.main_window.listbox_message.insert(tk.END,
                                                        ">{} {} {}\n".format(
                                                            self.on_message_count,
                                                            self.topic,
                                                            self.message))
                self.main_window.listbox_message.see("end")
                self.on_message_count += 1
        else:
            self.main_window.listbox_message.insert(tk.END,
                                                    ">{} {} {}\n".format(
                                                        self.on_message_count,
                                                        self.topic,
                                                        self.message))
            self.main_window.listbox_message.see("end")
            self.on_message_count += 1

        self.main_window.connect_status_text.set(
            "Connected | Message: %s | Publish: %s" % (
                self.on_message_count, self.publish_message_count))

    def connect_start(self, broker, port, username, password):
        self.client.username_pw_set(username, password)
        self.client.connect(broker, int(port), 60)
        return True

    def connect_stop(self):
        self.client.disconnect()
        return True

    def subscribe_start(self, topic):
        self.client.subscribe(topic, qos=0)
        self.client.loop_start()

    def publish_start(self, topic, msg):
        self.client.publish(topic, msg)
        self.publish_message_count += 1
