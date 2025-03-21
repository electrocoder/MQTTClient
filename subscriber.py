"""
MQTT Client GUI - MQTT Subscriber Client
Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>
"""

import tkinter as tk
from datetime import datetime
import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
from tkinter import messagebox


class Subscriber:
    def __init__(self, main_window):
        self.main_window = main_window
        self.client = None
        self.on_message_count = 0
        self.publish_message_count = 0

    def on_connect(self, client, userdata, flags, reason_code, properties=None):
        self.main_window.update_status(f"Connected | Messages: {self.on_message_count} | Published: {self.publish_message_count}")

    def on_disconnect(self, client, userdata, reason_code, properties=None):
        self.main_window.update_status(f"Disconnected | Messages: {self.on_message_count} | Published: {self.publish_message_count}")

    def on_message(self, client, userdata, msg, properties=None):
        topic = msg.topic
        try:
            message = msg.payload.decode('utf8')
        except Exception:
            message = None
        if message:
            if self.main_window.msg_filter and self.main_window.entry_msg_filter_text.get():
                if self.main_window.entry_msg_filter_text.get() in message or self.main_window.entry_msg_filter_text.get() in topic:
                    self.display_message(topic, message)
            else:
                self.display_message(topic, message)
        self.main_window.update_status(f"Connected | Messages: {self.on_message_count} | Published: {self.publish_message_count}")

    def display_message(self, topic, message):
        self.main_window.listbox_message.insert(tk.END, f">{self.on_message_count} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: {topic} {message}\n")
        self.main_window.listbox_message.see("end")
        self.on_message_count += 1

    def connect_start(self, name, broker, port, username, password):
        try:
            self.client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
            self.client.on_disconnect = self.on_disconnect
            self.client.on_message = self.on_message
            self.client.on_connect = self.on_connect
            self.client.username_pw_set(username, password)
            self.client.connect(broker, int(port), 60)
            self.client.loop_start()
            return True
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect: {str(e)}")
            return False

    def connect_stop(self):
        if self.client:
            self.client.loop_stop()
            self.client.disconnect()
            self.client = None
            return True
        return False

    def subscribe_start(self, topic):
        if self.client:
            self.client.subscribe(topic, qos=0)

    def publish_start(self, topic, msg):
        if self.client:
            self.client.publish(topic, msg)
            self.publish_message_count += 1
