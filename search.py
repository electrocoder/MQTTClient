import tkinter as tk
from threading import Thread


class SearchWindow:
    def __init__(self, main_window_frame_ui, font_size, subscriber):
        self.main_window_frame_ui = main_window_frame_ui

        self.search_window = tk.Toplevel(self.main_window_frame_ui)
        self.search_window.grab_set()
        self.search_window.title("MQTT Client Search")
        self.search_window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.subscriber = subscriber
        self.search = False
        self.thread = Thread(target=self.work)
        self.search_count = 0

        row = 0
        column = 0

        self.label_search = tk.Label(self.search_window, text="Search",
                                     font=font_size)
        self.label_search.grid(row=row, column=column)
        column += 1
        self.entry_broker_text = tk.StringVar(self.search_window)
        self.entry_broker = tk.Entry(self.search_window, font=font_size,
                                     textvariable=self.entry_broker_text)
        self.entry_broker.grid(row=row, column=column)

        column += 1

        self.button_search = tk.Button(self.search_window, text="Search",
                                       font=font_size,
                                       command=self.threading)
        self.button_search.grid(row=row, column=column)

        row += 1
        column = 0

        # subscribe list
        self.listbox_message_scrollbar = tk.Scrollbar(self.search_window,
                                                      orient=tk.VERTICAL)
        self.listbox_message = tk.Listbox(self.search_window, font=font_size)
        self.listbox_message.config(
            yscrollcommand=self.listbox_message_scrollbar.set)
        self.listbox_message.grid(
            column=column,
            columnspan=column + 2,
            ipadx=220,
            row=row,
            rowspan=row + 1,
            sticky="w")
        self.listbox_message_scrollbar.config(
            command=self.listbox_message.yview)
        self.listbox_message_scrollbar.grid(row=row, column=column + 2,
                                            ipady=70)

        row += 2
        column = 0

        self.label_search_text = tk.Label(self.search_window, text="...",
                                          font=font_size)
        self.label_search_text.grid(row=row, column=column)

    def on_closing(self):
        print("on_closing")
        self.search = False
        self.search_window.destroy()

    def threading(self):
        self.search = True
        self.thread.daemon = True
        self.thread.start()

    def work(self):
        while self.search:
            text = self.entry_broker_text.get()
            if text:
                message = self.subscriber.get_message()
                if text in str(message):
                    self.search_count += 1
                    self.label_search_text[
                        "text"] = "Search: {} Find: {}".format(text,
                                                               self.search_count)
                    self.listbox_message.insert(tk.END, "{}".format(message))
                    self.listbox_message.see("end")
