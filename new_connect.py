"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is New MQTT Broker
"""

import tkinter as tk

from config_file import ConfigFile


class NewConnect:
    def __init__(self, main_window_frame_ui, font_size):
        self.main_window_frame_ui = main_window_frame_ui

        self.new_connect_window = tk.Toplevel(self.main_window_frame_ui)
        self.new_connect_window.grab_set()
        self.new_connect_window.title("MQTT Client New Connect")

        row = 0
        column = 0

        self.label_broker = tk.Label(self.new_connect_window, text="Broker", font=font_size)
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self.new_connect_window)
        self.entry_broker = tk.Entry(self.new_connect_window, font=font_size,
                                     textvariable=self.entry_broker_text)
        self.entry_broker.grid(row=row, column=column)

        row += 1
        column = 0

        self.label_port = tk.Label(self.new_connect_window, text="Port", font=font_size)
        self.label_port.grid(row=row, column=column)
        column += 1
        self.entry_port_text = tk.StringVar(self.new_connect_window)
        self.entry_port = tk.Entry(self.new_connect_window, font=font_size,
                                   textvariable=self.entry_port_text)
        self.entry_port.grid(row=row, column=column)

        row += 1
        column = 0

        self.label_username = tk.Label(self.new_connect_window,
                                       text="Username", font=font_size)
        self.label_username.grid(row=row, column=column)
        column += 1
        self.entry_username_text = tk.StringVar(self.new_connect_window)
        self.entry_username = tk.Entry(self.new_connect_window, font=font_size,
                                       textvariable=self.entry_username_text)
        self.entry_username.grid(row=row, column=column)

        row += 1
        column = 0

        self.label_password = tk.Label(self.new_connect_window,
                                       text="Password", font=font_size)
        self.label_password.grid(row=row, column=column)
        column += 1
        self.entry_password_text = tk.StringVar(self.new_connect_window)
        self.entry_password = tk.Entry(self.new_connect_window, font=font_size,
                                       textvariable=self.entry_password_text)
        self.entry_password.grid(row=row, column=column)

        row += 1
        column = 0
        self.button_cancel = tk.Button(self.new_connect_window, text="Cancel", font=font_size,
                                       command=self.cancel)
        self.button_cancel.grid(row=row, column=column)
        column += 1
        self.button_save = tk.Button(self.new_connect_window, text="Save", font=font_size,
                                     command=self.save_config)
        self.button_save.grid(row=row, column=column)

    def save_config(self):
        ConfigFile().create_file(self.entry_broker_text.get(),
                                 self.entry_port_text.get(),
                                 self.entry_username_text.get(),
                                 self.entry_password_text.get())
        self.new_connect_window.destroy()

    def cancel(self):
        self.new_connect_window.destroy()
