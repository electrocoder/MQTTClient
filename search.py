import tkinter as tk

from config_file import ConfigFile


class SearchWindow:
    def __init__(self, main_window_frame_ui):
        self.main_window_frame_ui = main_window_frame_ui

        self.new_connect_window = tk.Toplevel(self.main_window_frame_ui)
        self.new_connect_window.grab_set()
        self.new_connect_window.title("MQTT Client Search")

        self.new_connect_window.geometry("400x400")

        row = 0
        column = 0

        self.label_broker = tk.Label(self.new_connect_window, text="Search")
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self.new_connect_window)
        self.entry_broker = tk.Entry(self.new_connect_window,
                                     textvariable=self.entry_broker_text)
        self.entry_broker.grid(row=row, column=column)

        row += 1
        column = 0


        row += 1
        column = 0
        self.button_cancel = tk.Button(self.new_connect_window, text="Cancel",
                                       command=self.cancel)
        self.button_cancel.grid(row=row, column=column)
        column += 1



    def cancel(self):
        self.new_connect_window.destroy()
