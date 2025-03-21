"""
MQTT Client GUI - New Topic Creation Window
Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>
"""

import tkinter as tk
from tkinter import ttk
from config_file import ConfigFile


class NewTopic(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.title("Add New Topic")
        self.geometry("300x150")
        self.transient(main_window)
        self.grab_set()

        font = ("Helvetica", 12)
        frame = ttk.Frame(self, padding="10")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Topic:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_topic = ttk.Entry(frame, font=font)
        self.entry_topic.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(frame, text="Save", command=self.save_topic).grid(row=1, column=1, pady=10, sticky="e")
        ttk.Button(frame, text="Cancel", command=self.destroy).grid(row=1, column=0, pady=10, sticky="w")

    def save_topic(self):
        topic = ConfigFile().create_topic(self.main_window.entry_broker_text.get(), self.entry_topic.get())
        self.main_window.refresh_subscribe_list()
        self.main_window.entry_subscribe_topic_text.set(topic)
        self.destroy()
