import tkinter


class MenuInit(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master, relief=tkinter.SUNKEN, bd=2)

        self.menubar = tkinter.Menu(self)

        menu = tkinter.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="New")
        menu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Cut")
        menu.add_command(label="Copy")
        menu.add_command(label="Paste")
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.master.tk.call(master, "config", "-menu", self.menubar)

        self.canvas = tkinter.Canvas(self, bg="white", width=400, height=400,
                             bd=0, highlightthickness=0)
        self.canvas.pack()



try:
    root = tkinter.Tk()
    app = MenuInit(root)
    app.pack()
    root.mainloop()

except Exception as e:
    print(e)
