import tkinter as tk

import paho.mqtt.client as mqtt

import subscriber
from main_window_frame_ui import MainWindowFrameUI


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
        print("basla")
        self.sub.subscribe_start()

    def button_disconnect(self):
        print("dur")
        self.sub.subscribe_stop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
