from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get(). isdigit():
            value = int (scvalue.get())
        else:            
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
                
        scvalue.set(value) 
        screen.update()     

    elif text == "C":
        scvalue.set("")
        screen.update()

    elif text == "<<":
        scvalue.set(scvalue.get()[:-1])
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("440x870")
root.minsize(440,870)
root.maxsize(440,870)
root.title("Calculater by HamZa")
root.wm_iconbitmap("icon1.ico")
frame1 = Frame(root,bg="blue",borderwidth=1,padx=12, pady=2)
frame1.pack()
l=Label(frame1, text="Casio 940/#",fg="navy blue", font="italic 20 bold")
l.pack(side=RIGHT,anchor="w",fill=BOTH)

button_quit = Button(root,borderwidth=8, relief=GROOVE, text="QUIT", command=root.quit,padx=20, pady=-20,fg="red", bg="gray",font="bold" )
button_quit.pack(anchor="nw",fill = Y,padx=4,pady=2)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font="lucida 70 bold")
screen.pack(fill=X, ipadx=8, pady=8, padx=10)

f = Frame(root, bg="brown")
b1 = Button(f,borderwidth=6, text="9",relief=GROOVE, padx=28 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")
b2= Button(f,borderwidth=6, text="8",relief=GROOVE, padx=28 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")
b3= Button(f, borderwidth=6,text="7",relief=GROOVE, padx=28 , pady=5 , fg="black",bg="gray",font="lucida 25 bold")

b1.pack(side=RIGHT,padx=18,pady=5)
b1.bind("<Button-1>", click )
b2.pack(side=RIGHT,padx=18,pady=5)
b2.bind("<Button-1>", click )
b3.pack(side=RIGHT,padx=18,pady=5)
b3.bind("<Button-1>", click )
f.pack()

f = Frame(root, bg="brown")
b1 = Button(f,borderwidth=6, text="6",relief=GROOVE, padx=28 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")
b2= Button(f,borderwidth=6, text="5",relief=GROOVE, padx=28 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")
b3= Button(f,borderwidth=6, text="4",relief=GROOVE, padx=28 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")

b1.pack(side=RIGHT,padx=18,pady=5)
b1.bind("<Button-1>", click )
b2.pack(side=RIGHT,padx=18,pady=5)
b2.bind("<Button-1>", click )
b3.pack(side=RIGHT,padx=18,pady=5)
b3.bind("<Button-1>", click )
f.pack()

f = Frame(root, bg="brown")
b1 = Button(f,borderwidth=6, text="3",relief=GROOVE, padx=28 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")
b2= Button(f, borderwidth=6,text="2",relief=GROOVE, padx=28 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")
b3= Button(f,borderwidth=6, text="1",relief=GROOVE, padx=28 , pady=5 ,fg="black", bg="gray",font="lucida 25 bold")

b1.pack(side=RIGHT,padx=18,pady=5)
b1.bind("<Button-1>", click )
b2.pack(side=RIGHT,padx=18,pady=5)
b2.bind("<Button-1>", click )
b3.pack(side=RIGHT,padx=18,pady=5)
b3.bind("<Button-1>", click )
f.pack()

f = Frame(root, bg="brown")
b1 = Button(f,borderwidth=6, text="0",relief=GROOVE, padx=27 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")
b2= Button(f,borderwidth=6, text="+",relief=GROOVE, padx=28 , pady=5 ,fg="purple", bg="gray",font="lucida 25 bold")
b3= Button(f,borderwidth=6, text="-",relief=GROOVE, padx=32 , pady=5 ,fg="purple",bg="gray", font="lucida 25 bold")

b1.pack(side=RIGHT,padx=18,pady=5)
b1.bind("<Button-1>", click )
b2.pack(side=RIGHT,padx=18,pady=5)
b2.bind("<Button-1>", click )
b3.pack(side=RIGHT,padx=18,pady=5)
b3.bind("<Button-1>", click )
f.pack()

f = Frame(root, bg="brown")
b1 = Button(f,borderwidth=6, text="*",relief=GROOVE, padx=30 , pady=5 ,fg="purple",bg="gray", font="lucida 25 bold")
b2= Button(f,borderwidth=6, text="/",relief=GROOVE, padx=32 , pady=5 ,fg="purple",bg="gray", font="lucida 25 bold")
b3= Button(f,borderwidth=6, text=".",relief=GROOVE, padx=31 , pady=5,fg="purple",bg="gray", font="lucida 25 bold")

b1.pack(side=RIGHT,padx=18,pady=5)
b1.bind("<Button-1>", click )
b2.pack(side=RIGHT,padx=16,pady=5)
b2.bind("<Button-1>", click )
b3.pack(side=RIGHT,padx=22,pady=5)
b3.bind("<Button-1>", click )
f.pack()

f = Frame(root, bg="brown")
b1 = Button(f,borderwidth=6, text="<<",relief=GROOVE, padx=17 , pady=5 ,fg="red",bg="gray", font="lucida 25 bold")
b2= Button(f,borderwidth=6, text=")",relief=GROOVE, padx=33 , pady=5 ,fg="orchid", bg="gray",font="lucida 25 bold")
b3= Button(f,borderwidth=6, text="(",relief=GROOVE, padx=30 , pady=5 ,fg="orchid",bg="gray", font="lucida 25 bold")

b1.pack(side=RIGHT,padx=18,pady=5)
b1.bind("<Button-1>", click )
b2.pack(side=RIGHT,padx=18,pady=5)
b2.bind("<Button-1>", click )
b3.pack(side=RIGHT,padx=18,pady=5)
b3.bind("<Button-1>", click )
f.pack()

f = Frame(root, bg="brown")
b1 = Button(f,borderwidth=6, text="C",relief=GROOVE, padx=25 , pady=5 ,fg="red",bg="gray", font="lucida 25 bold")
b2= Button(f,borderwidth=6, text="=",relief=GROOVE, padx=27 , pady=5 ,fg="navy blue", bg="gray",font="lucida 25 bold")
b3= Button(f,borderwidth=6, text="00",relief=GROOVE, padx=19 , pady=5 ,fg="black",bg="gray", font="lucida 25 bold")

b1.pack(side=RIGHT,padx=18,pady=5)
b1.bind("<Button-1>", click )
b2.pack(side=RIGHT,padx=18,pady=5)
b2.bind("<Button-1>", click )
b3.pack(side=RIGHT,padx=18,pady=5)
b3.bind("<Button-1>", click )
f.pack()

root.mainloop()