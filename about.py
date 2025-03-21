"""
MQTT Client GUI - About Window
Author: Sahin MERSIN - electrocoder <electrocoder@gmail.com>
"""

import os
import tkinter as tk
from tkinter import ttk


class AboutWindow(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.title("About MQTT Client")
        self.geometry('400x350')
        self.transient(main_window)
        self.grab_set()

        text = tk.Text(self, font=("Helvetica", 12), height=10)
        text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        ttk.Button(self, text='OK', command=self.destroy).pack(pady=5)

        basedir = os.path.dirname(__file__)
        file_name = os.path.join(basedir, "README.md")
        try:
            with open(file_name, 'r') as f:
                text.insert(tk.INSERT, f.read())
        except FileNotFoundError:
            text.insert(tk.INSERT, "README.md file not found.\n\nMQTT Client by Sahin Mersin\nVersion: 0v5")
