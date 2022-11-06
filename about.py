import tkinter as tk


class AboutWindow:
    def __init__(self, main_window_frame_ui):
        self.about_window = tk.Toplevel(main_window_frame_ui)
        self.about_window.grab_set()
        self.about_window.title("MQTT Client About")
        self.about_window.geometry("300x300")

        tk.Label(self.about_window, text="This is a new window").pack()
