from tkinter import *
root=Tk()
def fun1():
    print("This is New Project")
def fun2():
    print("This is  New")
def fun3():
    print("This is New Scratch file")
def fun4():
     print("This is open")
def fun5():
         print("This is Save As ")
def edit1():
    print("This is undo typing...")
def edit2():
     print("This is redo")
def edit3():
      print("This is cut")
def edit4():
     print("This is copy")

def edit5():
         print("This is paste.")
def edit6():
    print("This is copy path/referance")
def view1():
   print("this is tool windows")
def view2():
   print("this is apperance")
def view3():
   print("this is Quick defenition")
def view4():
   print("this is quick type defenition")
def view5():
   print("quick documentation")
def view6():
   print("this is jump to source")
def nev1():
    print("this is back")
def nev2():
    print("this is forward")
def nev3():
    print("this is search engine")

def nev4():
    print("this  is class")

def nev5():
    print("this is file")
def nev6():
    print("this is symbol")
def code1():
    print("this is override methods")
def code2():
    print("this is implement methods")
def code3():
    print("this is generte")
def code4():
    print("this is code completion")
def code5():
    print("this is inspect code")
def code6():
    print("this is code cleanup")
def refact1():
    print("this is refactor this")
def refact2():
    print("this is rename")
def refact3():
    print("this is movie files")
def refact4():
    print("this is copy file")
def refact5():
    print("this is safe delete")
def refact6():
    print("this is invert boolean")

mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project",command=fun1)
submenu.add_command(label="New",command=fun2)
submenu.add_separator()
submenu.add_command(label="New Scratch File",command=fun3)
submenu.add_command(label="Open",command=fun4)
submenu.add_separator()
submenu.add_command(label="Save As",command=fun5)
submenu.add_command(label="Exit",command=submenu.quit)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo typing",command=edit1)
newmenu.add_command(label="Redo",command=edit2)
newmenu.add_separator()
newmenu.add_command(label="Cut",command=edit3)
newmenu.add_command(label="Copy",command=edit4)
newmenu.add_separator()
newmenu.add_command(label="Paste",command=edit5)
newmenu.add_command(label="Copy path/Reference",command=edit6)

newmenu1=Menu(mymenu)
mymenu.add_cascade(label="View",menu=newmenu1)
newmenu1.add_command(label="Tool Windows",command=view1)
newmenu1.add_command(label="Apperance",command=view2)
newmenu1.add_separator()
newmenu1.add_command(label="Quick Defenition",command=view3)
newmenu1.add_command(label="Quick Type Defenition",command=view4)
newmenu1.add_separator()
newmenu1.add_command(label="Quick Documentation",command=view5)
newmenu1.add_command(label="Jump to Source",command=view6)

newmenu2=Menu(mymenu)
mymenu.add_cascade(label="Navigate",menu=newmenu2)
newmenu2.add_command(label="Back",command=nev1)
newmenu2.add_command(label="Forward",command=nev2)
newmenu2.add_separator()
newmenu2.add_command(label="Search Engine",command=nev3)
newmenu2.add_command(label="Class",command=nev4)
newmenu2.add_separator()
newmenu2.add_command(label="File",command=nev5)
newmenu2.add_command(label="Symbol",command=nev6)

newmenu3=Menu(mymenu)
mymenu.add_cascade(label="Code",menu=newmenu3)
newmenu3.add_command(label="Override Methods",command=code1)
newmenu3.add_command(label="Implement Methods",command=code2)
newmenu3.add_separator()
newmenu3.add_command(label="Generate",command=code3)
newmenu3.add_command(label="Code Completion",command=code4)
newmenu3.add_separator()
newmenu3.add_command(label="Inspect Code",command=code5)
newmenu3.add_command(label="Code Cleanup",command=code6)

newmenu4=Menu(mymenu)
mymenu.add_cascade(label="Refactor",menu=newmenu4)
newmenu4.add_command(label="Refactor This",command=refact1)
newmenu4.add_command(label="Rename",command=refact2)
newmenu4.add_separator()
newmenu4.add_command(label="Move Files",command=refact3)
newmenu4.add_command(label="Copy Files",command=refact4)
newmenu4.add_separator()
newmenu4.add_command(label="Safe Delete",command=refact5)
newmenu4.add_command(label="Invert Boolean",command=refact6)

root.mainloop()

