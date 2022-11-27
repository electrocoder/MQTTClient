"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is About window
"""
import os
import tkinter as tk


class AboutWindow(tk.Toplevel):
    def __init__(self, main_window, font_size):
        super().__init__(main_window)

        self.main_window = main_window
        self.title("MQTT Client About")

        text1 = tk.Text(self, font=font_size)
        text1.grid(row=0, column=0, padx=50, pady=50)

        button1 = tk.Button(self, text='OK', font=font_size,
                            command=self.close)
        button1.grid(row=1, column=0, padx=50, pady=50)

        basedir = os.path.dirname(__file__)
        self.file_name = os.path.join(basedir, "README.md")
        with open(self.file_name) as f:
            text1.insert(tk.INSERT, f.read())

    def close(self):
        self.destroy()
