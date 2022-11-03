import tkinter as tk

from config_file import ConfigFile


def new_connect_window(master):
    window = tk.Toplevel(master)
    window.grab_set()
    window.title("MQTT Client New Connect")

    # window.geometry("400x300")

    row = 0
    column = 0

    label_broker = tk.Label(window, text="Broker")
    label_broker.grid(row=row, column=column)
    column += 1
    entry_broker_text = tk.StringVar(master)
    entry_broker = tk.Entry(window, textvariable=entry_broker_text)
    entry_broker.grid(row=row, column=column)

    row += 1
    column = 0

    label_port = tk.Label(window, text="Port")
    label_port.grid(row=row, column=column)
    column += 1
    entry_port_text = tk.StringVar(master)
    entry_port = tk.Entry(window, textvariable=entry_port_text)
    entry_port.grid(row=row, column=column)

    row += 1
    column = 0

    label_username = tk.Label(window, text="Username")
    label_username.grid(row=row, column=column)
    column += 1
    entry_username_text = tk.StringVar(master)
    entry_username = tk.Entry(window, textvariable=entry_username_text)
    entry_username.grid(row=row, column=column)

    row += 1
    column = 0

    label_password = tk.Label(window, text="Password")
    label_password.grid(row=row, column=column)
    column += 1
    entry_password_text = tk.StringVar(master)
    entry_password = tk.Entry(window, textvariable=entry_password_text)
    entry_password.grid(row=row, column=column)

    def save_config():
        ConfigFile().create_file(entry_broker_text.get(), entry_port_text.get(), entry_username_text.get(),
                                 entry_password_text.get())

    row += 1
    column = 0
    button_cancel = tk.Button(window, text="Cancel")
    button_cancel.grid(row=row, column=column)
    column += 1
    button_save = tk.Button(window, text="Save", command=save_config)
    button_save.grid(row=row, column=column)
