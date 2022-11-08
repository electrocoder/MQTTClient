from tkinter import *

root = Tk()

root.geometry("250x250")

# Grid.rowconfigure(root, 0, weight=1)
# Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 1, weight=1)

button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")
button_3 = Button(root, text="Button 3")
listbox1 = Listbox(root)
listbox1.configure(activestyle="dotbox")

button_1.grid(row=0, column=0, sticky="NSEW")
button_2.grid(row=1, column=0, sticky="NSEW")
button_3.grid(row=1, column=1, sticky="NSEW")
listbox1.grid(row=2, column=0, sticky="NSEW")

root.mainloop()
