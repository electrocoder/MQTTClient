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
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.config_window_button = ttk.Button(self, width=10, text="Configure")
        self.config_window_button.pack(side=tk.LEFT, expand=False, padx=3, pady=3)
        self.connect_button = ttk.Button(self, width=10, text="Connect")
        self.connect_button.pack(side=tk.LEFT, expand=False, padx=3, pady=3)
        self.disconnect_button = ttk.Button(self,
                                            width=10,
                                            text="Disconnect",
                                            state="disabled")
        self.disconnect_button.pack(side=tk.LEFT, expand=False, padx=3, pady=3)

        self.connection_indicator = tk.Label(self, text="DISCONNECTED", bg="#ff6b6b")
        self.connection_indicator.pack(side=tk.RIGHT, padx=5, pady=5)
        self.connection_error_notification = ttk.Label(self, foreground='red')
        self.connection_error_notification.pack(side=tk.RIGHT, expand=1, fill='x')

