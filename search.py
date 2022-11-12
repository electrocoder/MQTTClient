import time
import tkinter as tk
from threading import Thread


class Window(tk.Toplevel):
    def __init__(self, parent, font_size, subscriber):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')

        self.thread = Thread(target=self.work)
        self.subscriber = subscriber

        tk.Button(self,
                text='Close',
                command=self.threading).pack(expand=True)

    def threading(self):
        self.thread.daemon = True
        self.thread.start()

    def work(self):
        while True:
            print("sssssssss", self.subscriber.get_message())

class SearchWindow:
    def __init__(self, font_size, subscriber):

        self.search_window = tk.Toplevel()
        self.search_window.grab_set()
        self.search_window.title("MQTT Client Search")
        self.search_window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.search_window.geometry("400x400")

        self.subscriber = subscriber
        self.search = False
        self.thread = Thread(target=self.work)

        row = 0
        column = 0

        self.label_broker = tk.Label(self.search_window, text="Search", font=font_size)
        self.label_broker.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self.search_window)
        self.entry_broker = tk.Entry(self.search_window, font=font_size,
                                     textvariable=self.entry_broker_text)
        self.entry_broker.grid(row=row, column=column)

        column += 1

        self.button_search = tk.Button(self.search_window, text="Search", font=font_size,
                                       command=self.threading)
        self.button_search.grid(row=row, column=column)

        row += 1
        column = 0
        self.button_cancel = tk.Button(self.search_window, text="Cancel", font=font_size,
                                       command=self.cancel)
        self.button_cancel.grid(row=row, column=column)

    def on_closing(self):
        print("on_closing")
        self.search_window.after(0, self.cancel())

    def cancel(self):
        print("cancel")
        self.search_window.destroy()

    def threading(self):
        self.thread.daemon = True
        self.thread.start()

    def work(self):
        while True:
            print("sssssssss", self.subscriber.get_message())

