import tkinter as tk

import paho.mqtt.client as mqtt

import subscriber

from ui_frame import UIFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MQTT Client')
        self.geometry('400x200')

        self.main_window_frame = tk.Frame()
        self.main_window_frame.pack()

        self.ui_frame = UIFrame(self.main_window_frame, self, height=35)
        self.ui_frame.pack()

        self.sub = subscriber.Subscriber(self.ui_frame, mqtt.Client())

    def button_connect(self):
        print("basla")
        self.sub.subscribe_start()

    def button_disconnect(self):
        print("dur")
        self.sub.subscribe_stop()


if __name__ == "__main__":
    app = App()
    app.mainloop()