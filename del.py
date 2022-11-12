import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry('300x200')

helv36 = tkFont.Font(family='Helvetica', size=36)
options = 'eggs spam toast'.split()
selected = tk.StringVar(root, value=options[0])

choose_test = tk.OptionMenu(root, selected, *options)
choose_test.config(font=helv36) # set the button font

helv20 = tkFont.Font(family='Helvetica', size=20)
menu = root.nametowidget(choose_test.menuname)  # Get menu widget.
menu.config(font=helv20)  # Set the dropdown menu's font
choose_test.grid(row=0, column=0, sticky='nsew')

root.mainloop()