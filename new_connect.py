"""
MQTT Client GUI - New MQTT Broker Connection Window
Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>
"""

import tkinter as tk
from tkinter import ttk
from config_file import ConfigFile


class NewConnect(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.title("New Connection")
        self.geometry("300x300")
        self.transient(main_window)
        self.grab_set()

        font = ("Helvetica", 12)
        frame = ttk.Frame(self, padding="10")
        frame.pack(fill="both", expand=True)

        labels = ["Name", "Broker", "Port", "Username", "Password"]
        self.entries = {}
        for idx, label in enumerate(labels):
            ttk.Label(frame, text=f"{label}:").grid(row=idx, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(frame, font=font)
            entry.grid(row=idx, column=1, padx=5, pady=5, sticky="ew")
            self.entries[label.lower()] = entry

        ttk.Button(frame, text="Save", command=self.save_config).grid(row=5, column=1, pady=10, sticky="e")
        ttk.Button(frame, text="Cancel", command=self.destroy).grid(row=5, column=0, pady=10, sticky="w")

    def save_config(self):
        config = ConfigFile()
        config.create_file(
            self.entries["name"].get(),
            self.entries["broker"].get(),
            self.entries["port"].get(),
            self.entries["username"].get(),
            self.entries["password"].get()
        )
        self.main_window.refresh_broker_list()
        self.destroy()
