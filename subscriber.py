import logging


class Subscriber:
    def __init__(self, main_window_frame_ui, client):
        self.topic = "timestamp"
        self.sid = 0

        self.client = client
        self.main_window_frame_ui = main_window_frame_ui

        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.username_pw_set("iothookpublic", "iothookpublic")

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(self.topic, qos=1)

    def on_disconnect(self, client, userdata, rc):
        print("disconnet...")
        logging.info("disconnecting reason  " + str(rc))

    def on_message(self, client, userdata, msg):
        print(
            msg.topic + " " + msg.payload.decode('utf8') + " " + str(self.sid))
        print("")
        self.sid += 1
        self.main_window_frame_ui.entry_msg_text.set(msg.payload.decode('utf8'))

    def subscribe_start(self):
        self.client.connect("www.iothook.com", 1883, 60)
        self.client.loop_start()

    def subscribe_stop(self):
        self.client.disconnect()
