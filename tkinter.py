from tkinter import Tk #we have to import this module
from tkinter import Label #we have to import Label for write a text in our window
window=Tk() # it use for show a window
window.title("Welcome to Abhishek Gautam GUI") #its our window name
window.minsize(width=100, height=200) # this is minimum size of window for open
lab=Label(window,text="Hello Abhishek Gautam")#for write a text in our window
lab.pack() # its work to print our text in open window in center
lab.grid(row=0,column=1) # its work to print our text in open window as you want to print
window.mainloop
