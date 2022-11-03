import tkinter as tk


def new_connect_window(master):
    window = tk.Toplevel(master)
    window.grab_set()
    window.title("MQTT Client New Connect")
    window.geometry("400x300")

    self.button_connect = tk.Button(self,
                                    text="Connect",
                                    command=main_window_self.button_connect)
    self.button_connect.pack()

    self.button_disconnect = tk.Button(self,
                                       text="Dur",
                                       command=main_window_self.button_disconnect)
    self.button_disconnect.pack()

    self.entry_msg_text = tk.StringVar()
    self.entry_msg = tk.Entry(self, textvariable=self.entry_msg_text)
    self.entry_msg.pack()
