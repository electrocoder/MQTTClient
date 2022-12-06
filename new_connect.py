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

        frame = tk.Frame()
        frame.pack()

        self.label_name = tk.Label(frame, text="Name",
                                   font=font_size)
        self.label_name.pack(**ipadding, fill=tk.X)

        self.entry_name_text = tk.StringVar(frame)
        self.entry_name = tk.Entry(frame, font=font_size,
                                   textvariable=self.entry_name_text)
        self.entry_name.pack(**ipadding, fill=tk.X)

        self.label_broker = tk.Label(frame, text="Broker",
                                     font=font_size)
        self.label_broker.pack(**ipadding, fill=tk.X)

        self.entry_broker_text = tk.StringVar(frame)
        self.entry_broker = tk.Entry(frame, font=font_size,
                                     textvariable=self.entry_broker_text)
        self.entry_broker.pack(**ipadding, fill=tk.X)

        self.label_port = tk.Label(frame, text="Port",
                                   font=font_size)
        self.label_port.pack(**ipadding, fill=tk.X)

        self.entry_port_text = tk.StringVar(frame)
        self.entry_port = tk.Entry(frame, font=font_size,
                                   textvariable=self.entry_port_text)
        self.entry_port.pack(**ipadding, fill=tk.X)

        self.label_username = tk.Label(frame,
                                       text="Username", font=font_size)
        self.label_username.pack(**ipadding, fill=tk.X)

        self.entry_username_text = tk.StringVar(frame)
        self.entry_username = tk.Entry(frame, font=font_size,
                                       textvariable=self.entry_username_text)
        self.entry_username.pack(**ipadding, fill=tk.X)

        self.label_password = tk.Label(frame,
                                       text="Password", font=font_size)
        self.label_password.pack(**ipadding, fill=tk.X)

        self.entry_password_text = tk.StringVar(frame)
        self.entry_password = tk.Entry(frame, font=font_size,
                                       textvariable=self.entry_password_text)
        self.entry_password.pack(**ipadding, fill=tk.X)

        self.button_cancel = tk.Button(frame, text="Cancel",
                                       font=font_size,
                                       command=self.cancel)
        self.button_cancel.pack(**ipadding, fill=tk.X)

        self.button_save = tk.Button(frame, text="Save",
                                     font=font_size,
                                     command=self.save_config)
        self.button_save.pack(**ipadding, fill=tk.X)

    def save_config(self):
        ConfigFile().create_file(self.entry_name_text.get(),
                                 self.entry_broker_text.get(),
                                 self.entry_port_text.get(),
                                 self.entry_username_text.get(),
                                 self.entry_password_text.get())
        self.destroy()

    def cancel(self):
        self.destroy()
