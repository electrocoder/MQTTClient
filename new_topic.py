"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/meseiot/iot-examples

Date: 26.11.2022

File: This script is Create New Topic
"""

import tkinter as tk

from config_file import ConfigFile


class NewTopic(tk.Toplevel):
    def __init__(self, main_window, font_size):
        super().__init__(main_window)

        self.main_window = main_window
        self.title("MQTT Client Create New Topic")

        row = 0
        column = 0

        self.label_topic = tk.Label(self, text="Add Topic",
                                    font=font_size)
        self.label_topic.grid(row=row, column=column)
        column += 1
        self.entry_topic = tk.Entry(self)
        self.entry_topic.config(font=font_size)
        self.entry_topic.grid(row=row, column=column)

        row += 1
        column = 0

        self.button_cancel = tk.Button(self, text="Cancel",
                                       font=font_size,
                                       command=self.cancel)
        self.button_cancel.grid(row=row, column=column, padx=55, pady=55)
        column += 1
        self.button_save = tk.Button(self, text="Save",
                                     font=font_size,
                                     command=self.save_topic)
        self.button_save.grid(row=row, column=column, padx=55, pady=55)

    def save_topic(self):
        topic = ConfigFile().create_topic(self.main_window.entry_broker_text.get(),
                                          self.entry_topic.get())
        self.main_window.entry_subscribe_topic_text.set(topic)
        self.destroy()

    def cancel(self):
        self.destroy()
