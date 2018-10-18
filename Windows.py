from tkinter import *

def windows():
    window = Tk()
    label = Label(window,text='blue', fg='red')
    label.pack()
    button=Button(window, text='OK')
    button.pack()
    window.mainloop()

windows()
