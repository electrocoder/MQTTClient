from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master)
variable.set("qqqq") # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

mainloop()
