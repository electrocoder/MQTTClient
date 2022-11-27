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


class OpenConnect(tk.Toplevel):
    def __init__(self, main_window, font_size):
        super().__init__(main_window)

        self.main_window = main_window
        self.title("MQTT Client Open Connect")

        row = 0
        column = 0

        self.label_broker = tk.Label(self, text="Broker",
                                     font=font_size)
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self)
        self.entry_broker = tk.OptionMenu(self,
                                          self.entry_broker_text,
                                          *ConfigFile().read_sections())
        self.entry_broker.config(font=font_size)
        menu = self.nametowidget(
            self.entry_broker.menuname)
        menu.config(font=font_size)
        self.entry_broker.grid(row=row, column=column)

        column += 1
        self.button_delete = tk.Button(self, text="Delete",
                                       font=font_size,
                                       command=self.delete)
        self.button_delete.grid(row=row, column=column)

        row += 2
        column = 0

        self.button_cancel = tk.Button(self, text="Cancel",
                                       font=font_size,
                                       command=self.cancel)
        self.button_cancel.grid(row=row, column=column, padx=50, pady=50)
        column += 1
        self.button_open = tk.Button(self, text="Open",
                                     font=font_size,
                                     command=self.open_connect)
        self.button_open.grid(row=row, column=column, padx=50, pady=50)

    def open_connect(self):
        broker, port, username, password = ConfigFile().read_broker(
            self.entry_broker_text.get())
        self.main_window.entry_broker_text.set(broker)

        self.main_window.entry_subscribe_topic['menu'].delete(0, 'end')

        new_choices = ConfigFile().read_topics(broker).split(',')
        for choice in new_choices:
            if choice:
                self.main_window.entry_subscribe_topic['menu'].add_command(
                    label=choice,
                    command=tk._setit(self.main_window.entry_subscribe_topic_text,
                                      choice))
                self.main_window.entry_subscribe_topic_text.set(choice)

        self.destroy()

    def cancel(self):
        self.destroy()

    def delete(self):
        deleted = ConfigFile().delete(
            self.main_window.entry_broker_text.get())
        if deleted:
            messagebox.showinfo("showinfo", "Broker is deleted.")
        else:
            messagebox.showerror("showerror", "Not deleted.")
