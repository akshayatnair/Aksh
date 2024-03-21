from tkinter import *
root=Tk()
def fun():
    print("click here")
button1=Button(root,text="ok",command=fun)
button1.pack()
root.mainloop()


