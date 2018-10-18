from tkinter import *

def windows():
    try:
       window = Tk()
       window.pack()
       label1 = Label(window,text='red', fg='red')
       label2 = Label(window, text='blue', fg='blue')
       label3 = Label(window, text='green', fg='green')
       label1.pack()
       label2.pack()
       label3.pack()
       button=Button(window, text='OK')
       button.pack()
       window.mainloop()
    except:
       print("Something went wrong...")

windows()
