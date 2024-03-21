class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
         self.name=input("enter your name")
         self.mark=int(input("enter your mark"))
    def putdetails(self):
        print(self.name,self.mark)
obj=student('','')
obj.getdetails()
obj.putdetails()