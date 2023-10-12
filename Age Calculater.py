from tkinter import *
from datetime import date
import tkinter.messagebox

root = Tk()

root.title("HamZa's Age Calculater")
# root.wm_iconbitmap("C:\Users\Qaisar\Downloads\AC.ico")
root.geometry("520x294")
root.configure(bg="silver")
root.minsize(520,294)
root.maxsize(520,760)

def ver():
     tkinter.messagebox.showinfo("Version",'\n ___Version 2.0___')

def ex():
   tkinter.messagebox.showinfo("Program",'Do you want to Exit!')
   exit()

def calculate():
     # Get the current date
    today = date.today()
    try:
        # Get the user's input for date, month, and year
        user_date = int(entry_date.get())
        user_month = int(entry_month.get())
        user_year = int(entry_year.get())

        # Create the user's birthdate
        birthdate = date(user_year, user_month, user_date)
        
        # Calculate the age in years
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        # Calculate the age in months
        age_in_months = (today.year - birthdate.year) * 12 + today.month - birthdate.month
        
        # Calculate the age in weeks
        age_in_weeks = (today - birthdate).days // 7
        
        # Calculate the age in days
        age_in_days = (today - birthdate).days
        
        # Calculate the age in hours, minutes, and seconds
        age_in_seconds = (today - birthdate).total_seconds()
        age_in_hours = age_in_seconds // 3600
        age_in_minutes = age_in_seconds // 60
    except:
        print("Invalid Entry!")
    # Update the result labels with the calculated ages
    output_years.delete(0, END)
    output_months.delete(0, END)
    output_weeks.delete(0, END)
    output_days.delete(0, END)
    output_hours.delete(0, END)
    output_minutes.delete(0, END)
    output_seconds.delete(0, END)
    
    output_years.insert(END, str(age) + " years")
    output_months.insert(END, str(age_in_months) + " months")
    output_weeks.insert(END, str(age_in_weeks) + " weeks")
    output_days.insert(END, str(age_in_days) + " days")
    output_hours.insert(END, str(age_in_hours) + " hours")
    output_minutes.insert(END, str(age_in_minutes) + " minutes")
    output_seconds.insert(END, str(int(age_in_seconds)) + " seconds")

def clear():
    # Clear the input fields and result labels
    entry_date.delete(0, END)
    entry_month.delete(0, END)
    entry_year.delete(0, END)
    
    output_years.delete(0, END)
    output_months.delete(0, END)
    output_weeks.delete(0, END)
    output_days.delete(0, END)
    output_hours.delete(0, END)
    output_minutes.delete(0, END)
    output_seconds.delete(0, END)

menu = Menu(root)
root.config(menu=menu)

subm = Menu(menu)
menu.add_cascade(label="Exit",menu=subm)
subm.add_command(label="Exit",command=ex)

subm1 = Menu(menu)
menu.add_cascade(label="About",menu=subm1)
subm1.add_command(label="Version",command=ver)

main_lable = Label(root,borderwidth=5,relief=GROOVE,text="Age Calculater",font=("arial black ",18,"bold"),bg="orchid",fg="white")
main_lable.pack(pady=5,padx=0)

today_lable = Label(root,borderwidth=3,relief=GROOVE,text="Today Date",font="arial 11 bold",bg="gray",fg="cyan")
today_lable.place(x=352,y=13)

date_lable = Label(root,font="arial 10 bold",bg="silver",borderwidth=3,relief=GROOVE,fg="black",text=date.today())
date_lable.place(x=442,y=13)

f1 = Frame(root,bg="purple",borderwidth=3,relief=GROOVE)
f1.pack(ipadx=8,ipady=1,pady=10)

lable1 = Label(f1,borderwidth=2,relief=SUNKEN, text=" Enter your date of birth ",fg="navy blue",bg="white",font=("arial",12,"bold"))
lable1.pack(side=LEFT,pady=3,padx=5,anchor="ne")

f2 = Frame(root,bg="red",borderwidth=3,relief=GROOVE)
f2.pack(pady=10,ipady=3,ipadx=20)

calculate_button = Button(f2,borderwidth=5,relief=GROOVE,text="CALCULATE",command=calculate,font=("cambria",20,"bold"),bg="navy blue",fg="white",padx=10)
calculate_button.pack(pady=12)

entry_date = StringVar()
entry_month = StringVar()
entry_year = StringVar()

user_date = entry_date.get()
user_month = entry_month.get()
user_year = entry_year.get()

lable2 = Label(f1,borderwidth=3,relief=GROOVE,text="Date:",font=("lucida",10,"bold"),bg="navy blue",fg="white")
lable2.pack(side=LEFT,anchor="ne",padx=3,pady=4)
entry_date = Entry(f1,textvariable=entry_date,width=5,font="lucida 10 bold",borderwidth=3,relief=GROOVE)
entry_date.pack(side=LEFT,anchor="ne",pady=5,padx=0)

lable3 = Label(f1,borderwidth=3,relief=GROOVE,text="Month:",font=("lucida",10,"bold"),bg="navy blue",fg="white")
lable3.pack(side=LEFT,anchor="ne",padx=3,pady=4)
entry_month = Entry(f1,textvariable=entry_month,width=5,font="lucida 10 bold",borderwidth=3,relief=GROOVE)
entry_month.pack(side=LEFT,anchor="ne",pady=5,padx=0)

lable4 = Label(f1,borderwidth=3,relief=GROOVE,text="Year:",font=("lucida",10,"bold"),bg="navy blue",fg="white")
lable4.pack(side=LEFT,anchor="ne",padx=3,pady=4)
entry_year = Entry(f1,textvariable=entry_year,width=7,font="lucida 10 bold",borderwidth=3,relief=GROOVE)
entry_year.pack(side=LEFT,anchor="ne",pady=5,padx=0)

f3 = Frame(root,bg="gray",borderwidth=2,relief=GROOVE)
f3.pack(anchor="nw",padx=5,ipadx=210,pady=15)

lable5 = Label(f3,text="Your age is",borderwidth=3,relief=GROOVE,font=("lucida",12,"bold"),bg="navy blue",fg="white")
lable5.pack(anchor="nw",ipadx=30)

output_years = Listbox(f3,width=49,height=1,font="lucida 10 bold",bg="white",fg="blue",relief=GROOVE,borderwidth=3)
output_years.place(x=155,y=2)

f3 = Frame(root,bg="gray",borderwidth=2,relief=GROOVE)
f3.pack(anchor="nw",padx=5,ipadx=210,pady=15)

lable5 = Label(f3,text="Your age in Months",borderwidth=3,relief=GROOVE,font=("lucida",12,"bold"),bg="navy blue",fg="white")
lable5.pack(anchor="nw",ipadx=30)

output_months = Listbox(f3,width=40,height=1,font="lucida 10 bold",bg="white",fg="blue",relief=GROOVE,borderwidth=3)
output_months.place(x=217,y=2)

f3 = Frame(root,bg="gray",borderwidth=2,relief=GROOVE)
f3.pack(anchor="nw",padx=5,ipadx=210,pady=15)

lable5 = Label(f3,text="Your age in Weeks",borderwidth=3,relief=GROOVE,font=("lucida",12,"bold"),bg="navy blue",fg="white")
lable5.pack(anchor="nw",ipadx=30)

output_weeks = Listbox(f3,width=41,height=1,font="lucida 10 bold",bg="white",fg="blue",relief=GROOVE,borderwidth=3)
output_weeks.place(x=209,y=2)

f3 = Frame(root,bg="gray",borderwidth=2,relief=GROOVE)
f3.pack(anchor="nw",padx=5,ipadx=210,pady=15)

lable5 = Label(f3,text="Your age in Days",borderwidth=3,relief=GROOVE,font=("lucida",12,"bold"),bg="navy blue",fg="white")
lable5.pack(anchor="nw",ipadx=30)

output_days = Listbox(f3,width=42,height=1,font="lucida 10 bold",bg="white",fg="blue",relief=GROOVE,borderwidth=3)
output_days.place(x=200,y=2)

f3 = Frame(root,bg="gray",borderwidth=2,relief=GROOVE)
f3.pack(anchor="nw",padx=5,ipadx=210,pady=15)

lable5 = Label(f3,text="Your age in Hours",borderwidth=3,relief=GROOVE,font=("lucida",12,"bold"),bg="navy blue",fg="white")
lable5.pack(anchor="nw",ipadx=30)

output_hours = Listbox(f3,width=41,height=1,font="lucida 10 bold",bg="white",fg="blue",relief=GROOVE,borderwidth=3)
output_hours.place(x=207,y=2)

f3 = Frame(root,bg="gray",borderwidth=2,relief=GROOVE)
f3.pack(anchor="nw",padx=5,ipadx=210,pady=15)

lable5 = Label(f3,text="Your age in Minutes",borderwidth=3,relief=GROOVE,font=("lucida",12,"bold"),bg="navy blue",fg="white")
lable5.pack(anchor="nw",ipadx=30)

output_minutes = Listbox(f3,width=39,height=1,font="lucida 10 bold",bg="white",fg="blue",relief=GROOVE,borderwidth=3)
output_minutes.place(x=220,y=2)

f3 = Frame(root,bg="gray",borderwidth=2,relief=GROOVE)
f3.pack(anchor="nw",padx=5,ipadx=210,pady=15)

lable5 = Label(f3,text="Your age in Seconds",borderwidth=3,relief=GROOVE,font=("lucida",12,"bold"),bg="navy blue",fg="white")
lable5.pack(anchor="nw",ipadx=30)

output_seconds = Listbox(f3,width=38,height=1,font="lucida 10 bold",bg="white",fg="blue",relief=GROOVE,borderwidth=3)
output_seconds.place(x=228,y=2)

end_lable = Label(root,text="May you live long!",fg="#04422F",bg="silver",font=("Georgia",10,"bold"))
end_lable.pack()

f4 =Frame(root,bg="navy blue",borderwidth=2,relief=GROOVE)
f4.pack(padx=5,ipadx=15,pady=5)

clear_button = Button(f4,borderwidth=6,relief=GROOVE,text="Clear",command=clear,font=("cambria",13,"bold"),bg="#253556",fg="red",padx=10)
clear_button.pack(pady=12)

root.mainloop()