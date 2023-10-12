from tkinter import *

root = Tk()

Heightvalue = StringVar()
Widthvalue = StringVar()
root.geometry('300x200')
root.title('Change Window Size')
root.configure(background='#9277fe')


def action():
    root.geometry(f'{Widthvalue.get()}x{Heightvalue.get()}')


Label(text='Width :', background='#4f89db', fg='white', padx=15, pady=5,font="lucida 8 bold").grid(column=1, row=2, padx=15, pady=5)
Label(text='Height :', background='#4f89db', fg='white', padx=15, pady=5,font="lucida 8 bold").grid(column=1, row=3, padx=15, pady=5)
Entry(textvariable=Widthvalue, background='#c4f593').grid(column=2, row=2)
Entry(textvariable=Heightvalue, background='#c4f593').grid(column=2, row=3)
Button(text='Apply Changes', command=action, background='gray',font="lucida 8 bold").grid(column=2, row=5)
root.mainloop()
