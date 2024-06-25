from tkinter import *
def addition():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1+num2
    label_result.config(text=f'Result:{result}')
    
window=Tk()
window.title('Addition')
label1=Label(window,text='Please Enter First Number')
label1.pack()
entry1=Entry(window)
entry1.pack()
label2=Label(window,text='Please Enter Second Number')
label2.pack()
entry2=Entry(window)
entry2.pack()
button=Button(window,text='Add',command=addition)
button.pack()
label_result=Label(window)
label_result.pack()
window.mainloop()
    
