import tkinter as tk
from tkinter.font import Font


class AboutWindow:
    def __init__(self, main_window_frame_ui, font_size):
        self.about_window = tk.Toplevel(main_window_frame_ui)
        self.about_window.grab_set()
        self.about_window.title("MQTT Client About")

        text1 = tk.Text(self.about_window, font=font_size)
        text1.pack()

        button1 = tk.Button(self.about_window, text='OK', font=font_size, command=self.close)
        button1.pack()

        with open('README.md') as f:
            text1.insert(tk.INSERT, f.read())

    def close(self):
        self.about_window.destroy()

