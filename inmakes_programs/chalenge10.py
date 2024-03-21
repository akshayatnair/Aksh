class vehicle():
     def __init__(self,modelnumber,enginetype,fuel):
          self.modelnumber=modelnumber
          self.enginetype=enginetype
          self.fuel=fuel
     def getspecs(self):
          self.modelnumber=input("enter the modelnumber")
          self.enginetype=input("enter the engine type")
          self.fuel=input("enter the type of fuel used")
     def displayspecs(self):
          print("the vehicle specifications are")
          print(self.modelnumber,self.enginetype,self.fuel)
class car(vehicle):
     def __init__(self,airbags):
          self.airbags=airbags
     def getdetails(self):
          self.airbags=input("whether this model contain airbag")
     def displaydetails(self):
          print("The Car Specifications are :")
          print(self.airbags)
class bike(vehicle):
     def __init__(self,wheelbase):
          self.wheelbase=wheelbase
     def putdetails(self):
          self.wheelbase=input("enter the wheelbase")
     def putdisplay(self):
          print("The Bike Specifications are :")
          print(self.wheelbase)
obj=bike('')
obj.getspecs()
obj.displayspecs()
obj.putdetails()
obj.putdisplay()
obj1=car('')
obj1.getdetails()
obj1.displaydetails()

