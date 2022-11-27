"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

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

    def create_file(self, broker, port, username, password):
        self.config.add_section(broker)
        self.config.set(broker, 'broker', broker)
        self.config.set(broker, 'port', port)
        self.config.set(broker, 'username', username)
        self.config.set(broker, 'password', password)

        with open(self.file_name, 'w') as configfile:
            self.config.write(configfile)

        return True

    def read_broker(self, broker):
        self.config.read(self.file_name)
        broker = self.config[broker]["broker"]
        port = self.config[broker]["port"]
        username = self.config[broker]["username"]
        password = self.config[broker]["password"]

        return broker, port, username, password

    def read_topics(self, broker):
        self.config.read(self.file_name)
        topics = self.config[broker]["topics"]

        return topics

    def create_topic(self, broker, topic):
        self.config.add_section(broker)
        self.config.set(broker, 'topics', topic)

        with open(self.file_name, 'w') as configfile:
            self.config.write(configfile)

        return self.config[broker]['topics']

    def delete(self, broker):
        self.config.read(self.file_name)
        delete = self.config.remove_section(broker)
        if delete:
            with open(self.file_name, 'w') as configfile:
                self.config.write(configfile)
            return True
        else:
            return False
