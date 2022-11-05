import configparser
from os.path import exists


class ConfigFile:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file_name = r"configfile.ini"
        if exists(self.file_name):
            self.config.read(self.file_name)

    def read_file(self):
        self.config.read(self.file_name)
        param = self.config["iot"]
        broker = param["broker"]
        return broker

    def create_file(self, broker, port, username, password):
        print(broker)
        self.config.add_section(broker)
        self.config.set(broker, 'broker', broker)
        self.config.set(broker, 'port', port)
        self.config.set(broker, 'username', username)
        self.config.set(broker, 'password', password)

        with open(self.file_name, 'w') as configfile:
            self.config.write(configfile)

        return True
