"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is About window
"""
import os
import tkinter as tk


class AboutWindow:
    def __init__(self, main_window_frame_ui, font_size):
        self.about_window = tk.Toplevel(main_window_frame_ui)
        self.about_window.grab_set()
        self.about_window.title("MQTT Client About")

        text1 = tk.Text(self.about_window, font=font_size)
        text1.grid(row=0, column=0, padx=50, pady=50)

        button1 = tk.Button(self.about_window, text='OK', font=font_size,
                            command=self.close)
        button1.grid(row=1, column=0, padx=50, pady=50)

        basedir = os.path.dirname(__file__)
        with open(os.path.join(basedir, "README.md")) as f:
            text1.insert(tk.INSERT, f.read())

    def close(self):
        self.about_window.destroy()
