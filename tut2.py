from tkinter import *
root = Tk()
label1 = Label(root,text="This is a tutorial about Python Tkinter")
label1.pack(side=TOP,expand=True)
label2 = Label(root,text="Do you wish to learn?",fg="blue")
label2.pack(side=TOP,expand=True)
button1 = Button(root, text="Accept", fg="green",command=root.destroy)
button1.pack(side=LEFT,expand=True)
button2 = Button(root, text="Close", fg="red",command=root.destroy)
button2.pack(side=RIGHT,expand=True)
root.mainloop()