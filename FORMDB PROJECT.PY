from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.geometry("1400x600")
root.title("Registeration form by kimghn")
bgimage=PhotoImage(file='photopyt.png')
bgphoto=Label(root,image=bgimage)
bgphoto.place(x=0,y=0)

def registeration():
    root.geometry("100x100")  
    mBox=messagebox.askquestion("تایید", "اطلاعات شما ذخیره شود؟")
    if mBox=='yes':
        db=sqlite3.connect('REGISTER.db')
        dbf=db.cursor()
        dbf.execute('CREATE TABLE IF NOT EXISTS registeration (name TEXT,lastname TEXT,socialnum TEXT PRIMARY KEY,age INT,gender TEXT,education TEXT,skill TEXT,phone INT,address TEXT)')
        name1=name0.get()
        lastname1=lastname0.get()
        socialnum1=socialnum0.get()
        age1=age0.get()
        varsg=vars1.get()
        varse=vars2.get()
        varss=f'{vars3.get()} {vars4.get()} {vars5.get()}'
        phone1=phone0.get()
        address1=blank6.get("1.0", END)
        dbf.execute('SELECT socialnum FROM registeration WHERE socialnum = ?', (socialnum1,))
        existSocialnum=dbf.fetchone()
        if existSocialnum is not None:
            db.close()
            messagebox.showerror("خطا", "کد ملی تکراری است")
        else:
            dbf.execute('INSERT INTO registeration VALUES(?,?,?,?,?,?,?,?,?)', (name1, lastname1, socialnum1, age1, varsg, varse, varss, phone1, address1))
            db.commit()
            db.close()
            messagebox.showinfo("تایید", "اطلاعات شما ذخیره شد")
    else:
        clears()

def clears():
    blank1.delete(0,END)
    blank2.delete(0,END)
    blank3.delete(0,END)
    blank4.delete(0,END)
    blank5.delete(0,END)
    blank6.delete(1.0,END)
    vars1.set("")
    vars2.set("")
    vars3.set("")
    vars4.set("")
    vars5.set("")
    
name=Label(root,text="نام",width=10,bg="#D8BFD8")
name.place(x=1190, y=120)
name0=StringVar()
blank1=Entry(root,textvariable=name0,justify="right")
blank1.place(x=1050, y=120)

lastname=Label(root,text="نام خانوادگی",width=10,bg="#D8BFD8")
lastname.place(x=1190, y=160)
lastname0=StringVar()
blank2=Entry(root,textvariable=lastname0,justify="right")
blank2.place(x=1050, y=160)

socialnum=Label(root, text="کد ملی", font=("arial",12), width=10,bg="#D8BFD8")
socialnum.place(x=940, y=120)
socialnum0=StringVar()
blank3=Entry(root,textvariable=socialnum0,justify="right")
blank3.place(x=800, y=120)

age=Label(root, text="سن", width=10,bg="#D8BFD8")
age.place(x=940, y=160)
age0=StringVar()
blank4=Entry(root,textvariable=age0,justify="right")
blank4.place(x=800, y=160)

gender= Label(root, text="جنسیت", width=10, font=("arial",12),bg="#D8BFD8")  
gender.place(x=1190, y=200)  
vars1=StringVar()  
Radiobutton(root, text="مرد", padx=10,variable=vars1, value='مرد',bg="#90EE90").place(x=1110, y=200)  
Radiobutton(root, text="زن", padx =10,variable=vars1, value='زن',bg="#90EE90").place(x=1010,y=200)    

education= Label(root, text="تحصیلات", width=10, font=("arial",12),bg="#D8BFD8")  
education.place(x=1190, y=240)  
vars2=StringVar()  
Radiobutton(root, text="دانش آموز", padx=10,variable=vars2, value='دانش آموز', bg="pink").place(x=1080, y=240)  
Radiobutton(root, text="دیپلم", padx=10,variable=vars2, value='دیپلم', bg="pink").place(x=980,y=240)  
Radiobutton(root, text="کاردانی", padx=10, variable=vars2, value='کاردانی', bg="pink").place(x=880,y=240)  
Radiobutton(root, text="کارشناسی", padx=10,variable=vars2, value='کارشناسی', bg="pink").place(x=780, y=240)  
Radiobutton(root, text="کارشناسی ارشد", padx=10,variable=vars2, value='کارشناسی ارشد', bg="pink").place(x=650,y=240)  
Radiobutton(root, text="دکتری", padx=10, variable=vars2, value='دکتری', bg="pink").place(x=550,y=240)  

skills= Label(root, text="تخصص", width=10, font=("arial",12),bg="#D8BFD8")  
skills.place(x=1190, y=280)  
vars3=StringVar()
vars4=StringVar()
vars5=StringVar()
Checkbutton(root, text="نرم افزار", variable=vars3,onvalue='نرم افزار', offvalue='', width=10,bg="#FFD700").place(x=1080, y=280)  
Checkbutton(root, text="سخت افزار", variable=vars4,onvalue='سخت افزار', offvalue='', width=10,bg="#FFD700").place(x=950,y=280)  
Checkbutton(root, text="فناوری اطلاعات", variable=vars5,onvalue='فناوری اطلاعات', offvalue='', width=10,bg="#FFD700").place(x=820,y=280)  

phone=Label(root, text="شماره تلفن", width=10, font=("arial",12),bg="#D8BFD8")
phone.place(x=1190, y=320)
phone0=StringVar()
blank5=Entry(root,textvariable=phone0, justify='right')
blank5.place(x=1050,y=320)

address=Label(root, text="آدرس", width=10,bg="#D8BFD8")
address.place(x=1190, y=360)
blank6=Text(root, width=50, height=5)
blank6.place(x=750,y=360)

register=Button(root, text="ثبت", width=10, bg="grey", command=registeration).place(x=1000,y=500)
clear=Button(root, text="پاک کردن", width=10, bg="grey",command=clears).place(x=900,y=500)

mainloop()