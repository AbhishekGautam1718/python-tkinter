from tkinter import Tk
from tkinter import Label
import time
Abhi=Tk()
Abhi.title("Clock")
def show_clock():
    show_time=time.strftime("%H:%M:%S")
    digi_clock.config(text=show_time)
    digi_clock.after(200,show_time)
digi_clock=Label(Abhi,font=("Cursive",150),bg=("blue"),fg=("green"))
digi_clock.pack()
show_clock()
Abhi.mainloop()
