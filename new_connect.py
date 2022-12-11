"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/meseiot/iot-examples

Date: 12.11.2022

File: This script is New MQTT Broker
"""

from tkinter import *

from config_file import ConfigFile


class NewConnect(Toplevel):
    def __init__(self, main_window, font_size):
        super().__init__(main_window)

        self.main_window = main_window
        self.title("MQTT Client New Connect")
        self.geometry("300x300")

        ipadding = {'ipadx': 10, 'ipady': 10}

        frame = Frame(self, padx=5, pady=5)
        frame.grid(row=0, column=1)

        Label(frame, text='Name', padx=5, pady=5).pack()
        Label(frame, text='Broker', padx=5, pady=5).pack()
        Label(frame, text='Port', padx=5, pady=5).pack()
        Label(frame, text='Username', padx=5, pady=5).pack()
        Label(frame, text='Password', padx=5, pady=5).pack()

        frame2 = Frame(self, padx=5, pady=5)
        frame2.grid(row=0, column=2)

        self.entry_name_text = StringVar(self)
        self.entry_name = Entry(frame2, font=font_size,
                                textvariable=self.entry_name_text).pack(padx=5,
                                                                        pady=5)

        self.entry_broker_text = StringVar(self)
        self.entry_broker = Entry(frame2, font=font_size,
                                  textvariable=self.entry_broker_text).pack(
            padx=5, pady=5)

        self.entry_port_text = StringVar(self)
        self.entry_port = Entry(frame2, font=font_size,
                                textvariable=self.entry_port_text).pack(padx=5,
                                                                        pady=5)

        self.entry_username_text = StringVar(self)
        self.entry_username = Entry(frame2, font=font_size,
                                    textvariable=self.entry_username_text).pack(
            padx=5, pady=5)

        self.entry_password_text = StringVar(self)
        self.entry_password = Entry(frame2, font=font_size,
                                    textvariable=self.entry_password_text).pack(
            padx=5, pady=5)

        self.button_cancel = Button(self, text="Cancel",
                                    font=font_size,
                                    command=self.cancel, padx=10).grid(row=1,
                                                                       column=1,
                                                                       pady=5)

        self.button_save = Button(self, text="Save",
                                  font=font_size,
                                  command=self.save_config, padx=10).grid(
            row=1, column=2, pady=5)

    def save_config(self):
        ConfigFile().create_file(self.entry_name_text.get(),
                                 self.entry_broker_text.get(),
                                 self.entry_port_text.get(),
                                 self.entry_username_text.get(),
                                 self.entry_password_text.get())
        self.destroy()

    def cancel(self):
        self.destroy()
