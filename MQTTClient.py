import tkinter as tk

import paho.mqtt.client as mqtt

import subscriber
from main_window_frame_ui import MainWindowFrameUI
from config_file import ConfigFile


import about as about
import new_connect as new_connect
import open_connect as open_connect

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MQTT Client')
        self.geometry('600x200')

        self.main_window_frame = tk.Frame()
        self.main_window_frame.pack()

        self.main_window_frame_ui = MainWindowFrameUI(self.main_window_frame, self, height=35)
        self.main_window_frame_ui.pack()

        self.sub = subscriber.Subscriber(self.main_window_frame_ui, mqtt.Client())

    def button_connect(self):
        print("button_connect")
        broker, port, username, password = ConfigFile().read_broker(self.main_window_frame_ui.entry_broker_text.get())
        print(broker, port, username, password)
        self.sub.connect_start(broker, port, username, password)

    def button_disconnect(self):
        print("button_disconnect")
        self.sub.connect_stop()

    def button_subscribe_topic(self):
        print("button_subscribe_topic")
        self.sub.subscribe_start(self.main_window_frame_ui.entry_subscribe_topic_text.get())

    def button_publish_topic(self):
        print("button_publish_topic")
        # self.sub.subscribe_start(self.main_window_frame_ui.entry_subscribe_topic_text.get())

    def about_window(self):
        about.AboutWindow(self.master)

    def new_connect_window(self):
        new_connect.NewConnect(self.master)

    def open_connect_window(self):
        open_connect.OpenConnect(self.main_window_frame_ui)



if __name__ == "__main__":
    app = App()
    app.mainloop()
