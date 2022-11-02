"""
MQTTk - Lightweight graphical MQTT client and message analyser

Copyright (C) 2022  Máté Szabó

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
import tkinter.ttk as ttk


class UIFrame(ttk.Frame):
    def __init__(self, master, main_window_self, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.connect_button = ttk.Button(self, width=10,
                                               text="Connect",
                                               command=main_window_self.button_basla)
        self.connect_button.pack()

        self.connect_button = ttk.Button(self, width=10,
                                               text="Dur",
                                               command=main_window_self.button_dur)
        self.connect_button.pack()

        self.textbox_text = tk.StringVar()
        self.textbox_text.set("qwe")
        self.textbox = ttk.Entry(self, textvariable=self.textbox_text)
        self.textbox.pack()
