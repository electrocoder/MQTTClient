import tkinter as tk

from config_file import ConfigFile


class OpenConnect:
    def __init__(self, master):
        self.master = master
        window = tk.Toplevel(self.master)
        window.grab_set()
        window.title("MQTT Client Open Connect")

        window.geometry("400x300")

        row = 0
        column = 0

        BROKERS = []
        print(ConfigFile().read_file())

        self.label_broker = tk.Label(window, text="Broker")
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(window)
        self.entry_broker_text.set("   Select   ")
        self.entry_broker = tk.OptionMenu(window, self.entry_broker_text, *BROKERS)
        self.entry_broker.grid(row=row, column=column)

        row += 1
        column = 0
        self.button_cancel = tk.Button(window, text="Cancel")
        self.button_cancel.grid(row=row, column=column)
        column += 1
        self.button_open = tk.Button(window, text="Open", command=self.open_connect)
        self.button_open.grid(row=row, column=column)

    def open_connect(self):
        pass
