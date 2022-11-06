import tkinter as tk

from config_file import ConfigFile


class OpenConnect:
    def __init__(self, main_window_frame_ui):
        self.main_window_frame_ui = main_window_frame_ui
        self.open_connect_window = tk.Toplevel(self.main_window_frame_ui)
        self.open_connect_window.grab_set()
        self.open_connect_window.title("MQTT Client Open Connect")

        self.open_connect_window.geometry("400x300")

        row = 0
        column = 0

        self.label_broker = tk.Label(self.open_connect_window, text="Broker")
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self.open_connect_window)
        self.entry_broker_text.set(" Select ")
        self.entry_broker = tk.OptionMenu(self.open_connect_window, self.entry_broker_text, *ConfigFile().read_sections())
        self.entry_broker.grid(row=row, column=column)

        row += 1
        column = 0
        self.button_cancel = tk.Button(self.open_connect_window, text="Cancel")
        self.button_cancel.grid(row=row, column=column)
        column += 1
        self.button_open = tk.Button(self.open_connect_window, text="Open", command=self.open_connect)
        self.button_open.grid(row=row, column=column)

    def open_connect(self):
        c = ConfigFile()
        broker, port, username, password = c.read_broker(self.entry_broker_text.get())
        self.main_window_frame_ui.entry_msg_text.set("ee")

        return True
