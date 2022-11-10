import tkinter as tk


class Subscriber:
    def __init__(self, main_window_frame_ui, client):
        self.client = client
        self.main_window_frame_ui = main_window_frame_ui

        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

        self.on_message_count = 0
        self.publish_message_count = 0

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.main_window_frame_ui.connect_status_text.set(
            "Connected | Message: %s | Publish: %s" % (
            self.on_message_count, self.publish_message_count))

    def on_disconnect(self, client, userdata, rc):
        print("disconnet...")
        self.main_window_frame_ui.connect_status_text.set(
            "Disconnect | Message: %s | Publish: %s" % (
            self.on_message_count, self.publish_message_count))

    def on_message(self, client, userdata, msg):
        print(
            msg.topic + " " + msg.payload.decode('utf8'))
        print("")
        self.main_window_frame_ui.listbox_message.insert(tk.END,
                                                         "{} {} {}".format(
                                                             self.on_message_count,
                                                             msg.topic,
                                                             msg.payload.decode(
                                                                 'utf8')))
        self.main_window_frame_ui.listbox_message.see("end")
        self.on_message_count += 1
        self.main_window_frame_ui.connect_status_text.set(
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
