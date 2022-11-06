# import required modules
from tkinter import *

tkWindow = Tk()
tkWindow.geometry('500x500')
tkWindow.title('Example Utility')

scrollbar = Scrollbar(tkWindow, orient="vertical")

SelectuserLabel = Label(tkWindow, text="Select").grid(row=0, column=0)
test = Listbox(tkWindow, width=10, height=5, font=("Helvetica", 14))
test.insert(END, 1)
test.insert(END, 2)
test.insert(END, 3)
test.insert(END, 4)
test.insert(END, 5)
test.insert(END, 6)
test.insert(END, 7)
test.insert(END, 8)
test.grid(row=0, column=1)
scrollbar.config(command=test.yview)
scrollbar.grid(row=0, column=2, sticky='ns')

tkWindow.mainloop()