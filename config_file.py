"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/meseiot/iot-examples

Date: 12.11.2022

File: This script is Config file operations
"""

import configparser
import os
from os.path import exists


class ConfigFile:
    def __init__(self):
        self.config = configparser.ConfigParser()

        basedir = os.path.dirname(__file__)
        self.file_name = os.path.join(basedir, "config_file.ini")
        if exists(self.file_name):
            self.config.read(self.file_name)

    def read_sections(self):
        self.config.read(self.file_name)
        return self.config.sections()

    def create_file(self, name, broker, port, username, password):
        self.config.add_section(name)
        self.config.set(name, 'broker', broker)
        self.config.set(name, 'port', port)
        self.config.set(name, 'username', username)
        self.config.set(name, 'password', password)
        self.config.set(name, 'topics', '#,')

        with open(self.file_name, 'w') as configfile:
            self.config.write(configfile)

        return True

    def read_broker(self, name):
        self.config.read(self.file_name)
        broker = self.config[name]["broker"]
        port = self.config[name]["port"]
        username = self.config[name]["username"]
        password = self.config[name]["password"]

        return name, broker, port, username, password

    def read_topics(self, name):
        self.config.read(self.file_name)
        topics = self.config[name]["topics"]

        return topics

    def create_topic(self, name, topic):
        print("name", name)
        print("topic", topic)
        con = self.config[name]
        con['topics'] += topic + ","

        with open(self.file_name, 'w') as configfile:
            self.config.write(configfile)

        return topic

    def delete(self, name):
        self.config.read(self.file_name)
        delete = self.config.remove_section(name)
        if delete:
            with open(self.file_name, 'w') as configfile:
                self.config.write(configfile)
            return True
        else:
            return False
