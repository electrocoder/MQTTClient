import configparser


class ConfigFile:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def read_file(self):
        return "rrr"

    def create_file(self, broker):
        print(broker)
        self.config.add_section(broker)
        self.config.set(broker, 'host', 'localhost')
        self.config.set(broker, 'user', 'finxter1')
        self.config.set(broker, 'port', '5543')
        self.config.set(broker, 'password', 'myfinxterpw')
        self.config.set(broker, 'db', 'postgres')

        with open(r"configfile.ini", 'w') as configfile:
            self.config.write(configfile)
