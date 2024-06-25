from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import os

def login():
    user=username.get()
    code=password.get()
    if user=="Abhishek@123456" and code=="Abhi@1718":
        window=Toplevel(screen)
        window.title("Bill")
        window.geometry('1000x600')
        window.configure(bg='gray')
        window.resizable(False,False)


    
        
       
        #write Your Program to join the login page
        def Reset():
            entry_Tea.delete(0,END)
            entry_Samosa.delete(0,END)
            entry_Vada_Paw.delete(0,END)
            entry_Missle.delete(0,END)
            entry_Dosa.delete(0,END)
            entry_Pani_Puri.delete(0,END)
            entry_Manturian.delete(0,END)
            entry_Pizza.delete(0,END)




        def Total():
            try:
                a1=int(Tea.get())
            except:
                a1=0

            try:a2=int(Samosa.get())
            except:a2=0

            try:a3=int(Vada_Paw.get())
            except:a3=0
                    
            try:a4=int(Missle.get())
            except:a4=0
                    
            try:a5=int(Dosa.get())
            except:a5=0

            try:a6=int(Pani_Puri.get())
            except:a6=0

            try:a7=int(Manturian.get())
            except:a7=0

            try:a8=int(Pizza.get())
            except:a8=0



            #define cost of each item per quantity
            c1=7*a1
            c2=12*a2
            c3=15*a3
            c4=60*a4
            c5=60*a5
            c6=40*a6
            c7=50*a7
            c8=200*a8

            lab_total=Label(frm2,font=('aria',20,'bold'),text='Total',width=16,fg='lightblue',bg='black')
            lab_total.place(x=0,y=50)

            entry_total=Entry(frm2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg='lightyellow')
            entry_total.place(x=20,y=100)

            totalcost=c1+c2+c3+c4+c5+c6+c7+c8
            string_Bill=('Rs.',str('%.2f' %totalcost))
            Total_bill.set(string_Bill)
        lab1=Label(window,text="MVLU Canteen BILLING",bg="black",fg="white",font=("calibri",33),width="300",height="2")
        lab1.pack()

        #MENU CARD
        frm=Frame(window,bg="lightgreen",highlightbackground="black",highlightthickness=1,width="300",height=370)
        frm.place(x=10,y=118)


        Label(frm,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="Lightgreen").place(x=80,y=0)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Tea.........Rs.7/Cup",fg='black',bg='lightgreen').place(x=10,y=80)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Samosa.........Rs.12/Plate",fg='black',bg='lightgreen').place(x=10,y=110)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Vada_Paw.........Rs.15/Plate",fg='black',bg='lightgreen').place(x=10,y=140)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Missle.........Rs.60/Plate",fg='black',bg='lightgreen').place(x=10,y=170)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Dosa.........Rs.60/Plate",fg='black',bg='lightgreen').place(x=10,y=200)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Pani_Puri.........Rs.40/Plate",fg='black',bg='lightgreen').place(x=10,y=230)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Manturian.........Rs.50/Plate",fg='black',bg='lightgreen').place(x=10,y=260)
        Label(frm,font=("Bradley Hand ITC",15,"bold"),text="Pizza.........Rs.200",fg='black',bg='lightgreen').place(x=10,y=290)



        #Bill
        frm2=Frame(window,bg='lightblue',highlightbackground='black',highlightthickness=1,width=300,height=370)
        frm2.place(x=690,y=118)

        Bill=Label(frm2,text='Bill',font=('calibri',20))
        Bill.place(x=120,y=10)
        #ENTRY WORK
        frm1=Frame(window,bd=5,height=370,width=300,relief=RAISED)
        frm1.pack()
        Tea=StringVar()
        Samosa=StringVar()
        Vada_Paw=StringVar()
        Missle=StringVar()
        Dosa=StringVar()
        Pani_Puri=StringVar()
        Manturian=StringVar()
        Pizza=StringVar()
        Total_bill=StringVar()

        #Label
        lab2_Tea=Label(frm1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue4")
        lab2_Samosa=Label(frm1,font=("aria",20,'bold'),text="Samosa",width=12,fg="blue4")
        lab2_Vada_Paw=Label(frm1,font=("aria",20,'bold'),text="Vada_Paw",width=12,fg="blue4")
        lab2_Missle=Label(frm1,font=("aria",20,'bold'),text="Missle",width=12,fg="blue4")
        lab2_Dosa=Label(frm1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
        lab2_Pani_Puri=Label(frm1,font=("aria",20,'bold'),text="Pani_Puri",width=12,fg="blue4")
        lab2_Manturian=Label(frm1,font=("aria",20,'bold'),text="Manturian",width=12,fg="blue4")
        lab2_Pizza=Label(frm1,font=("aria",20,'bold'),text="Pizza",width=12,fg="blue4")
        lab2_Tea.grid(row=1,column=0)
        lab2_Samosa.grid(row=2,column=0)
        lab2_Vada_Paw.grid(row=3,column=0)
        lab2_Missle.grid(row=4,column=0)
        lab2_Dosa.grid(row=5,column=0)
        lab2_Pani_Puri.grid(row=6,column=0)
        lab2_Manturian.grid(row=7,column=0)
        lab2_Pizza.grid(row=8,column=0)



        #ENTRY
        entry_Tea=Entry(frm1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
        entry_Samosa=Entry(frm1,font=("aria",20,'bold'),textvariable=Samosa,bd=6,width=8,bg="lightpink")
        entry_Vada_Paw=Entry(frm1,font=("aria",20,'bold'),textvariable=Vada_Paw,bd=6,width=8,bg="lightpink")
        entry_Missle=Entry(frm1,font=("aria",20,'bold'),textvariable=Missle,bd=6,width=8,bg="lightpink")
        entry_Dosa=Entry(frm1,font=("aria",20,'bold'),textvariable=Dosa,bd=6,width=8,bg="lightpink")
        entry_Pani_Puri=Entry(frm1,font=("aria",20,'bold'),textvariable=Pani_Puri,bd=6,width=8,bg="lightpink")
        entry_Manturian=Entry(frm1,font=("aria",20,'bold'),textvariable=Manturian,bd=6,width=8,bg="lightpink")
        entry_Pizza=Entry(frm1,font=("aria",20,'bold'),textvariable=Pizza,bd=6,width=8,bg="lightpink")


        entry_Tea.grid(row=1,column=1)
        entry_Samosa.grid(row=2,column=1)
        entry_Vada_Paw.grid(row=3,column=1)
        entry_Missle.grid(row=4,column=1)
        entry_Dosa.grid(row=5,column=1)
        entry_Pani_Puri.grid(row=6,column=1)
        entry_Manturian.grid(row=7,column=1)
        entry_Pizza.grid(row=8,column=1)


        #Buttons

        btn_reset=Button(frm1,bd=5,fg="Black",bg='lightblue',font=('ariel',16,'bold'),width=10,text="Reset",command=Reset)
        btn_reset.grid(row=9,column=0)

        btn_total=Button(frm1,bd=5,fg="Black",bg='lightblue',font=('ariel',16,'bold'),width=10,text="Total",command=Total)
        btn_total.grid(row=9,column=1)






        #End your program here
    #for password and username wrong
    elif user=='' and code=='':
        messagebox.showerror("Please Enter Username and Password")
    elif user=='':
        messagebox.showerror("All Fiel Mendatory")
    elif code=='':
        messagebox.showerror("All Fiel Mendatory")
    elif user!="Abhishek@123456" and code!="Abhi@1718":
        messagebox.showerror("Wrong Username or Password")

        


    
def main_screen():

    global screen
    global username
    global password
    screen=Tk()
    screen.geometry('1280x720')
    screen.configure(bg='gray')
    screen.title('Login Page')

    lab=Label(text='Login Page',font=('arial'))
    lab.pack()

    Label(text='Username',font=('arial',30,'bold'),bg='lightyellow').place(x=100,y=50)
    Label(text='Password',font=('arial',30,'bold'),bg='lightyellow').place(x=100,y=150)
    

    username=StringVar()
    password=StringVar()
    entry_username=Entry(textvariable=username,width=12,bd=2,font=('arial',30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(textvariable=password,width=12,bd=2,font=('arial',30),show='*')
    entry_password.place(x=400,y=150)
    Button(text='Login',height='2',width=23,bg='blue',fg='white',bd=0,command=login).place(x=450,y=250)
    
    


main_screen()

