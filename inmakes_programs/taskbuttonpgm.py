from tkinter import *
class buttonaction:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.pbutton=Button(frame,text="click",command=self.pmsg)
        self.pbutton.pack()

        self.qbutton=Button(frame,text="cancel",command=self.qmsg)
        self.qbutton.pack(side=LEFT)

        self.rbutton=Button(frame,text="exit",command=frame.quit)
        self.rbutton.pack(side=RIGHT)


    def pmsg(self):
        print("clicked")
    def qmsg(self):
        print("cancelled")
root=Tk()
obj=buttonaction(root)
root.mainloop()
