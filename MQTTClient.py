import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import paho.mqtt.client as mqtt

import subscriber

from ui_frame import UIFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x50')

        self.main_window_frame = ttk.Frame()
        self.main_window_frame.pack(fill='both', expand=1)

        self.ui_frame = UIFrame(self.main_window_frame, self, height=35)
        self.ui_frame.pack(anchor="w", side=tk.TOP, fill=tk.X, padx=3, pady=3)

    def button_clicked(self):
        print("bbb")
        aa = subscriber.Subscriber(mqtt.Client())
        aa.basla()
        # aa.on_message()


if __name__ == "__main__":
    app = App()
    app.mainloop()
