"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is New MQTT Broker
"""

import tkinter as tk

from config_file import ConfigFile


class NewConnect(tk.Toplevel):
    def __init__(self, main_window, font_size):
        super().__init__(main_window)

        self.main_window = main_window
        self.title("MQTT Client New Connect")

        ipadding = {'ipadx': 10, 'ipady': 10}

        frame = tk.Frame(self)
        frame.pack(fill = tk.BOTH, expand = True)

        self.label_name = tk.Label(frame, text="Name",
                                   font=font_size)
        self.label_name.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.entry_name_text = tk.StringVar(self)
        self.entry_name = tk.Entry(frame, font=font_size,
                                   textvariable=self.entry_name_text)
        self.entry_name.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        frame1 = tk.Frame(self)
        frame1.pack(fill = tk.BOTH, expand = True)

        self.label_broker = tk.Label(frame1, text="Broker",
                                     font=font_size)
        self.label_broker.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.entry_broker_text = tk.StringVar(self)
        self.entry_broker = tk.Entry(frame1, font=font_size,
                                     textvariable=self.entry_broker_text)
        self.entry_broker.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        frame2 = tk.Frame(self)
        frame2.pack(fill = tk.BOTH, expand = True)

        self.label_port = tk.Label(frame2, text="Port",
                                   font=font_size)
        self.label_port.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.entry_port_text = tk.StringVar(self)
        self.entry_port = tk.Entry(frame2, font=font_size,
                                   textvariable=self.entry_port_text)
        self.entry_port.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        frame3 = tk.Frame(self)
        frame3.pack(fill = tk.BOTH, expand = True)

        self.label_username = tk.Label(frame3,
                                       text="Username", font=font_size)
        self.label_username.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.entry_username_text = tk.StringVar(self)
        self.entry_username = tk.Entry(frame3, font=font_size,
                                       textvariable=self.entry_username_text)
        self.entry_username.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        frame4 = tk.Frame(self)
        frame4.pack(fill = tk.BOTH, expand = True)

        self.label_password = tk.Label(frame4,
                                       text="Password", font=font_size)
        self.label_password.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.entry_password_text = tk.StringVar(self)
        self.entry_password = tk.Entry(frame4, font=font_size,
                                       textvariable=self.entry_password_text)
        self.entry_password.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        frame5 = tk.Frame(self)
        frame5.pack(fill = tk.BOTH, expand = True)

        self.button_cancel = tk.Button(frame5, text="Cancel",
                                       font=font_size,
                                       command=self.cancel)
        self.button_cancel.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.button_save = tk.Button(frame5, text="Save",
                                     font=font_size,
                                     command=self.save_config)
        self.button_save.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

    def save_config(self):
        ConfigFile().create_file(self.entry_name_text.get(),
                                 self.entry_broker_text.get(),
                                 self.entry_port_text.get(),
                                 self.entry_username_text.get(),
                                 self.entry_password_text.get())
        self.destroy()

    def cancel(self):
        self.destroy()
