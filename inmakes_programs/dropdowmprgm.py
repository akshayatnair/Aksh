from tkinter import *
root=Tk()
def fun1():
    print("hai clicked")

mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save1")
submenu.add_command(label="save2")
submenu.add_separator()
submenu.add_command(label="save3")
submenu.add_command(label="save4")

newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="undo",command=fun1)

root.mainloop()