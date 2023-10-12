from tkinter import *
from tkinter import ttk,messagebox
import webbrowser
import speech_recognition
from pygame import mixer

def search():
    if questionFeild.get()!="":
        if temp.get() == "google":
            webbrowser.open(f"https://www.google.com/search?q={questionFeild.get()}")
        if temp.get() == "duck":
            webbrowser.open(f"https://duckduckgo.com/?va=a&t=hn&q={questionFeild.get()}")
        if temp.get() == "amazon":
            webbrowser.open(f"https://www.amazon.com/s?k={questionFeild.get()}&sprefix=mobile%2Caps%2C499&ref=nb_sb_ss_ts-doa-p_3_6")
        if temp.get() == "youtube":        
            webbrowser.open(f"https://www.youtube.com/results?search_query={questionFeild.get()}")
    else:
        messagebox.showerror('Error','There is nothing to search.')        

def voice():
    mixer.init()
    mixer.music.load("music1.mp3")
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            audio=sr.listen(m)
            message = sr.recognize_google(audio)
            mixer.music.load("music2.mp3")
            questionFeild.delete(0,END)
            questionFeild.insert(0,message)
            search()
        except:
            pass    

root = Tk()

root.geometry("660x160+100+100")
root.title("HAMZA Search Engine")
root.wm_iconbitmap("icon.ico")
root.resizable(0,0)
root.config(bg="light gray")

temp = StringVar()

style = ttk.Style()
print(style.theme_names())
style.theme_use("classic")

main_lable = Label(root,text="Well Come to HAMZA search engine",font="lucida 20 bold",
                   bg="light gray",fg="navy blue")
main_lable.grid(row=0,column=1)

querylable = Label(root,text="Write here",font="helvetica 14 bold",bg="light gray")
querylable.grid(row=1,column=0)

questionFeild = Entry(root,width=36,font="helvetica 18 bold",relief=SUNKEN,bd=3)
questionFeild.grid(row=1,column=1,padx=10,pady=3)

micImage = PhotoImage(file="mic.png")
micbutton = Button(root,image=micImage,bg="light gray",bd=0,cursor="hand2",
                   activebackground="light gray",command=voice)
micbutton.grid(row=1,column=2)

searchImage = PhotoImage(file="search.png")
searchbutton = Button(root,image=searchImage,bg="light gray",bd=0,cursor="hand2",activebackground="light gray",
                      command=search)
searchbutton.grid(row=1,column=3)

googleradiobutton = ttk.Radiobutton(root,text="Google",value="google",variable=temp)
googleradiobutton.place(x=75,y=80)

duckradiobutton = ttk.Radiobutton(root,text="Duck Duck go",value="duck",variable=temp)
duckradiobutton.place(x=200,y=80)

amazonradiobutton = ttk.Radiobutton(root,text="Amazon",value="amazon",variable=temp)
amazonradiobutton.place(x=380,y=80)

youtuberadiobutton = ttk.Radiobutton(root,text="Youtube",value="youtube",variable=temp)
youtuberadiobutton.place(x=510,y=80)

button_quit = Button(root,borderwidth=4, relief=GROOVE, text="QUIT", command=root.quit,padx=20,
                      pady=4,fg="red", bg="gray",font="lucida 12 bold" )
button_quit.place(x=305,y=110)

def enter_function(value):
    searchbutton.invoke()

root.bind("<Return>",enter_function)

temp.set("google")

root.mainloop()