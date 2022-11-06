import tkinter as tk

import paho.mqtt.client as mqtt

import subscriber
from main_window_frame_ui import MainWindowFrameUI


import about as about
import new_connect as new_connect
import open_connect as open_connect

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MQTT Client')
        self.geometry('400x200')

        self.main_window_frame = tk.Frame()
        self.main_window_frame.pack()

        self.main_window_frame_ui = MainWindowFrameUI(self.main_window_frame, self, height=35)
        self.main_window_frame_ui.pack()

        self.sub = subscriber.Subscriber(self.main_window_frame_ui, mqtt.Client())

    def button_connect(self):
        print("button_connect")
        self.sub.subscribe_start()

    def button_disconnect(self):
        print("button_disconnect")
        self.sub.subscribe_stop()

    def about_window(self):
        about.AboutWindow(self.master)

    def new_connect_window(self):
        new_connect.NewConnect(self.master)

    def open_connect_window(self):
        open_connect.OpenConnect(self.main_window_frame_ui)



if __name__ == "__main__":
    app = App()
    app.mainloop()
