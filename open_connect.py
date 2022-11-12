"""MQTT Client GUI

Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>

Source Code: https://github.com/electrocoder/MQTTClient

MQTT Examples: https://github.com/mesebilisim/mqtt-examples

Date: 12.11.2022

File: This script is Open MQTT Broker
"""

import tkinter as tk
from tkinter import messagebox

from config_file import ConfigFile


class OpenConnect:
    def __init__(self, main_window_frame_ui, font_size):
        self.main_window_frame_ui = main_window_frame_ui

        self.open_connect_window = tk.Toplevel(self.main_window_frame_ui)
        self.open_connect_window.grab_set()
        self.open_connect_window.title("MQTT Client Open Connect")

        row = 0
        column = 0

        self.label_broker = tk.Label(self.open_connect_window, text="Broker",
                                     font=font_size)
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self.open_connect_window)
        self.entry_broker_text.set(" Select ")
        self.entry_broker = tk.OptionMenu(self.open_connect_window,
                                          self.entry_broker_text,
                                          *ConfigFile().read_sections())
        self.entry_broker.config(font=font_size)
        menu = self.open_connect_window.nametowidget(
            self.entry_broker.menuname)
        menu.config(font=font_size)
        self.entry_broker.grid(row=row, column=column)

        column += 1
        self.button_delete = tk.Button(self.open_connect_window, text="Delete",
                                       font=font_size,
                                       command=self.delete)
        self.button_delete.grid(row=row, column=column)

        row += 2
        column = 0

        self.button_cancel = tk.Button(self.open_connect_window, text="Cancel",
                                       font=font_size,
                                       command=self.cancel)
        self.button_cancel.grid(row=row, column=column, padx=50, pady=50)
        column += 1
        self.button_open = tk.Button(self.open_connect_window, text="Open",
                                     font=font_size,
                                     command=self.open_connect)
        self.button_open.grid(row=row, column=column, padx=50, pady=50)

    def open_connect(self):
        broker, port, username, password = ConfigFile().read_broker(
            self.entry_broker_text.get())
        self.main_window_frame_ui.entry_broker_text.set(broker)
        self.open_connect_window.destroy()

    def cancel(self):
        self.open_connect_window.destroy()

    def delete(self):
        deleted = ConfigFile().delete(
            self.entry_broker_text.get())
        if deleted:
            messagebox.showinfo("showinfo", "Broker is deleted.")
        else:
            messagebox.showerror("showerror", "Not deleted.")
