import tkinter as tk

class Frames:
    
    try:
        #creating frame
        root = tk.Tk()
        root.geometry("300x200+400+400")
        root.resizable()
        root.title("Math program")

        #first label
        label0 = tk.Label(root, text="Write a number here then hit Go: ")
        label0.pack()

        #input box
        entrybox = tk.Entry(root)
        entrybox.pack()
        entrybox.focus_set()

        #creating labels within frame and packing them on frame
        label1 = tk.Label(root, text='red', fg='red')
        label2 = tk.Label(root, text='blue', fg='blue')
        label3 = tk.Label(root, text='green', fg='green')
        label1.pack()
        label2.pack()
        label3.pack()

        #creating a button
        button = tk.Button(root, text='Go')
        button.pack()

        #start the frame
        root.mainloop()

    # handling expression in any case
    except Exception as e:
        print(e)
