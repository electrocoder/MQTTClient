import tkinter as tk

from config_file import ConfigFile


class NewConnect:
    def __init__(self, master):
        self.master = master
        window = tk.Toplevel(self.master)
        window.grab_set()
        window.title("MQTT Client New Connect")

        # window.geometry("400x300")

        row = 0
        column = 0

        self.label_broker = tk.Label(window, text="Broker")
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self.master)
        self.entry_broker = tk.Entry(window, textvariable=self.entry_broker_text)
        self.entry_broker.grid(row=row, column=column)

        row += 1
        column = 0

        self.label_port = tk.Label(window, text="Port")
        self.label_port.grid(row=row, column=column)
        column += 1
        self.entry_port_text = tk.StringVar(self.master)
        self.entry_port = tk.Entry(window, textvariable=self.entry_port_text)
        self.entry_port.grid(row=row, column=column)

        row += 1
        column = 0

        self.label_username = tk.Label(window, text="Username")
        self.label_username.grid(row=row, column=column)
        column += 1
        self.entry_username_text = tk.StringVar(self.master)
        self.entry_username = tk.Entry(window, textvariable=self.entry_username_text)
        self.entry_username.grid(row=row, column=column)

        row += 1
        column = 0

        self.label_password = tk.Label(window, text="Password")
        self.label_password.grid(row=row, column=column)
        column += 1
        self.entry_password_text = tk.StringVar(self.master)
        self.entry_password = tk.Entry(window, textvariable=self.entry_password_text)
        self.entry_password.grid(row=row, column=column)

        row += 1
        column = 0
        self.button_cancel = tk.Button(window, text="Cancel")
        self.button_cancel.grid(row=row, column=column)
        column += 1
        self.button_save = tk.Button(window, text="Save", command=self.save_config)
        self.button_save.grid(row=row, column=column)

    def save_config(self):
        ConfigFile().create_file(self.entry_broker_text.get(), self.entry_port_text.get(),
                                 self.entry_username_text.get(),
                                 self.entry_password_text.get())
