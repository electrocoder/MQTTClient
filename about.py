import tkinter as tk


class AboutWindow:
    def __init__(self, main_window_frame_ui):
        self.about_window = tk.Toplevel(main_window_frame_ui)
        self.about_window.grab_set()
        self.about_window.title("MQTT Client About")
        self.about_window.geometry("600x400")

        text1 = tk.Text(self.about_window)
        text1.grid(column=0, row=0, sticky='ew')

        button1 = tk.Button(self.about_window, text='OK', command=self.close)
        button1.grid(column=0, row=1)

        with open('README.md') as f:
            text1.insert(tk.INSERT, f.read())

    def close(self):
        self.about_window.destroy()

