"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 26.11.2022

File: This script is Create New Topic
"""

import tkinter as tk
from tkinter import messagebox

from config_file import ConfigFile


class NewTopic:
    def __init__(self, main_window_frame_ui, font_size):
        self.main_window_frame_ui = main_window_frame_ui

        self.window = tk.Toplevel(self.main_window_frame_ui)
        self.window.grab_set()
        self.window.title("MQTT Client Create New Topic")

        row = 0
        column = 0

        self.label_topic = tk.Label(self.window, text="Topic",
                                     font=font_size)
        self.label_topic.grid(row=row, column=column)
        column += 1
        self.entry_topic_text = tk.StringVar(self.window)
        self.entry_topic = tk.Entry(self.window)
        self.entry_topic.config(font=font_size)
        self.entry_topic.grid(row=row, column=column)

        row += 2
        column = 0

        self.button_cancel = tk.Button(self.window, text="Cancel",
                                       font=font_size,
                                       command=self.cancel)
        self.button_cancel.grid(row=row, column=column, padx=50, pady=50)
        column += 1
        self.button_save = tk.Button(self.window, text="Save",
                                     font=font_size,
                                     command=self.save_topic)
        self.button_save.grid(row=row, column=column, padx=50, pady=50)

    def save_topic(self):
        broker, port, username, password = ConfigFile().read_topic(
            self.entry_topic_text.get())
        self.main_window_frame_ui.entry_topic_text.set(broker)
        self.window.destroy()

    def cancel(self):
        self.window.destroy()

