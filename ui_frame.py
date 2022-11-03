import tkinter as tk


class UIFrame(tk.Frame):
    def __init__(self, master, main_window_self, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.button_connect = tk.Button(self,
                                        text="Connect",
                                        command=main_window_self.button_basla)
        self.button_connect.pack()

        self.button_disconnect = tk.Button(self,
                                           text="Dur",
                                           command=main_window_self.button_dur)
        self.button_disconnect.pack()

        self.entry_msg_text = tk.StringVar()
        self.entry_msg = tk.Entry(self, textvariable=self.entry_msg_text)
        self.entry_msg.pack()
