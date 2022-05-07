from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("880x550+0+0")
root.resizable(False, False)
root.title("Kiraya bill")



label = Label(root,text="KIRAYAA NIKAAL LO",relief=GROOVE,bd=9,font=("times new romnan", 20, "bold"),bg="#074463",fg="gold",pady=4).pack(fill=X)
frame = Frame(root,bg="#074463",highlightbackground="black",bd=3,relief=GROOVE,highlightthickness=1,width=380,height=455).place(x=499,y=55)
Label(frame,text="  \tWELCOME TO THE KIRAYAA NIKAAL \n LO SOFTWARE :}\n========================================",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=60)
Label(frame,text="GUIDENCE : SO, THIS IS THE SAMPLE OR TO SAY \nEXAMPLE FOR HOW TO FILL THIS FROM IN \nWHICH FORMAT.  \n========================================",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=125)
Label(frame,text="- DATE = 06-05-2022",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=200)
Label(frame,text="- FROM_DATE = 06-04-2022 (LAST_MONTH_DATE)",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=220)
Label(frame,text="- TO_DATE = 06-05-2022 (CURRENT_MONTH_DATE)",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=240)
Label(frame,text="- TENANT_NAME = MR. GUIDO VAN ROSSUM",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=260)
Label(frame,text="- CURRENT_MONTH_UNIT = 3323",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=280)
Label(frame,text="- LAST_MONTH_UNIT = 3219",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=300)
Label(frame,text="- UNIT_RATE = Rs. 8 /- (ENTER YOUR AREA UNIT \nRATE)",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=320)
Label(frame,text="- ROOM_RENT = Rs. 8500 /-(ENTER YOUR ROOM \nRENT)",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=360)
Label(frame,text="=> NOW CLICK_BUTTON FOR GENERATE_BILL \n",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=510,y=400)
Label(frame,text="=> THEN YOU WILL SEE YOUR RESULT ON \nYOUR SCREEN \n      ========================================",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=475,y=423)
Label(frame,text=" \tKhatam Bye Bye Tata Good Bye Gaya...(;",bg="#074463",font=("Helvetica",11,"bold","italic"),fg="lightgreen").place(x=480,y=480)




# bottom label 

label = Label(root,text="Note: Please do not pay any amount without Receipt. (:",relief=GROOVE,bd=9,font="Helvetica 15 bold italic",bg="#074463",fg="white smoke",width=78).place(x=1,y=509)


def show():

    if a.get()=="":
        messagebox.showerror("Error","Please enter the Date :(") 
    elif b.get()=="":
        messagebox.showerror("Error","Please enter the From_Date :(")
    elif c.get()=="":
        messagebox.showerror("Error","Please enter the To_Date :(")
    elif d.get()=="":
        messagebox.showerror("Error","Please enter the Tenant Name :(")
    elif e.get()=="":
        messagebox.showerror("Error","Please enter the Current_M_Unit :(")
    elif f.get()=="":
        messagebox.showerror("Error","Please enter the Last_M_Unit :(")
    elif g.get()=="":
        messagebox.showerror("Error","Please enter the Unit :(")
    elif h.get()=="":
        messagebox.showerror("Error","Please enter the Rent :(")
    else:
        label=Label(root,text="Successfully Complete !",bg="white smoke",font="ariel 15 bold",fg="green").place(x=220,y=385)
       

    res=int(e.get())-int(f.get())
    j.set(res*int(g.get()))
    i.set(res*int(g.get())+int(h.get()))
   

# file io
    with open(a.get()+".txt","w") as k:
        k.write("\t        Binesh Bhati"+"\n")
        k.write("--------------------------------------------------------"+"\n")
        k.write("H.No-225, Sec-53, Sai Encalve, Vill-Gijhore, Noida (U.P.) "+"\n")
        k.write("========================================================="+"\n")
        k.write("Date: "+a.get()+"\n")
        k.write("From_Date: "+b.get()+"\n")
        k.write("To_Date: "+c.get()+"\n")
        k.write("Tenant Name: "+d.get()+"\n")
        k.write("Current_M_Unit: "+e.get()+"\n")
        k.write("Last_M_Unit: "+f.get()+"\n")
        k.write("Unit: "+g.get()+"\n")
        k.write("Rent: "+h.get()+"\n")
        k.write("========================================================="+"\n")
        k.write("Total_Amount: Rs."+i.get()+"\n")
        k.write("Electricity_Bill: Rs."+j.get()+"\n")
        k.write("========================================================="+"\n")

a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
j=StringVar()



# label 
frame1 = Frame(root,bg="#074463",highlightbackground="black",bd=9,relief=GROOVE,highlightthickness=1,width=500,height=454).place(x=1,y=56)


label = Label(frame1,text="Date : ",bg="#074463",fg="lightgreen",font=("times new roman", 19, "bold")).place(x=42,y=67)
label = Label(frame1,text="From_Date : ",bg="#074463",fg="lightgreen",font=("times new roman", 19, "bold")).place(x=42,y=92)
label = Label(frame1,text="To_Date : ",bg="#074463",fg="lightgreen",font=("times new roman", 19, "bold")).place(x=42,y=120)
label = Label(frame1,text="Tenant_Name : ",bg="#074463",fg="lightgreen",font=("times new roman", 19, "bold")).place(x=42,y=150)
label = Label(frame1,text="Current_M_Unit : ",bg="#074463",fg="lightgreen",font=("times new roman",19, "bold")).place(x=42,y=180)
label = Label(frame1,text="Last_M_Unit : ",bg="#074463",fg="lightgreen",font=("times new roman", 19, "bold")).place(x=42,y=210)
label = Label(frame1,text="Unit : ",bg="#074463",fg="lightgreen",font=("times new roman", 19, "bold")).place(x=42,y=240)
label = Label(frame1,text="Rent : ",bg="#074463",fg="lightgreen",font=("times new roman", 19, "bold")).place(x=42,y=270)
label = Label(frame1,text="Total_Amount : ",bg="#074463",fg="lightgreen",font=("times new roman" ,19, "bold")).place(x=42,y=410)
label = Label(frame1,text="Electricity_Bill : ",bg="#074463",fg="lightgreen",font=("times new roman" ,19, "bold")).place(x=42,y=460)
label = Label(frame1,text="Click On G_Button =>>",bg="#074463",fg="lightgreen",font=("times new roman" ,16, "bold")).place(x=35,y=338)






# entry 

# frame2 = Frame(root,bg="#074463",highlightbackground="black",bd=9,relief=GROOVE,highlightthickness=1,width=500,height=450).place(x=1,y=56)

e1 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=a,font="ariel 15 bold",width="15").place(x=250,y=68)
e2 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=b,font="ariel 15 bold",width="15").place(x=250,y=100)
e3 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=c,font="ariel 15 bold",width="15").place(x=250,y=128)
e4 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=d,font="ariel 15 bold",width="15").place(x=250,y=158)
e5 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=e,font="ariel 15 bold",width="15").place(x=250,y=188)
e6 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=f,font="ariel 15 bold",width="15").place(x=250,y=218)
e7 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=g,font="ariel 15 bold",width="15").place(x=250,y=248)
e8 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=h,font="ariel 15 bold",width="15").place(x=250,y=278)
e9 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=i,font="ariel 15 bold",width="15").place(x=250,y=418)
e10 = Entry(root,bd=5,bg="cadetblue",fg="gold",relief=SUNKEN,textvariable=j,font="ariel 15 bold",width="15").place(x=250,y=465)

# button 

generate = Button(root,bg="cadetblue",fg="black",text="Generate Bill",bd=5,command=show,font="ariel 15 bold").place(x=270,y=330)

      

root.mainloop()