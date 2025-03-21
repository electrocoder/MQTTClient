"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/meseiot/iot-examples

Date: 12.11.2022

File: This script is About window
"""
import os
import tkinter as tk


class AboutWindow(tk.Toplevel):
    def __init__(self, main_window, font_size):
        super().__init__(main_window)

        self.title("MQTT Client About")
        self.geometry('400x350')

        ipadding = {'ipadx': 1, 'ipady': 1}

        text1 = tk.Text(self, font=font_size, height=10)
        text1.pack(**ipadding, side=tk.TOP, expand=True, fill=tk.BOTH)

        button1 = tk.Button(self, text='OK', font=font_size,
                            command=self.close)
        button1.pack(**ipadding, side=tk.TOP, expand=True, fill=tk.BOTH)

        basedir = os.path.dirname(__file__)
        self.file_name = os.path.join(basedir, "README.md")
        with open(self.file_name) as f:
            text1.insert(tk.INSERT, f.read())

    def close(self):
        self.destroy()
