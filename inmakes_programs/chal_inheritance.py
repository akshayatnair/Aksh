class hospital:
    def __init__(self,adname,drname,sisname,dept):
        self.adname=adname
        self.drname=drname
        self.sisname=sisname
        self.dept=dept

    def getdetails(self):
            self.adname = input("enter the admin name \n")
            self.drname = input("enter the doctor name \n")
            self.sisname = input("enter the sister name \n")
            self.dept = input("enter the department \n")
class department(hospital):

    def putdetails(self):
        print("This is Department Class \n")
        print("Admin Name=",self.adname,"\n")
        print("Doctor name=",self.drname,"\n")
        print("sister name=",self.sisname,"\n")
        print("Department=",self.dept,"\n")

obj=department('','','','')
obj.getdetails()
obj.putdetails()
class patientward():
    def __init__(self,name,age,number,disease):
        self.name=name
        self.age=age
        self.number=number
        self.disease=disease
    def patientdetails(self):
        self.name=input("enter the patient name \n")
        self.age:int =int(input("enter the patient age \n"))
        self.number:int =int(input("enter the phn number \n"))
        self.disease=input("enter the patient disease \n")
    def patientdisplay(self):
        print("patient name=",self.name,"\n")
        print("Patient age=",self.age,"\n")
        print("patient phone number=",self.number,"\n")
        print("Patient disease=",self.disease,"\n")
obj1=patientward('','','','')
obj1.patientdetails()
obj1.patientdisplay()


