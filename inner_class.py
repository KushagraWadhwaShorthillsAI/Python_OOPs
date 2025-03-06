class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno  
        self.lap=self.Laptop()   #lap refers to the inner class Laptop, need not be mentioned as a parameter in the method definition

    def show(self):
        print(self.name,"(Roll No:",self.rollno,")", "uses the laptop of",self.lap.brand)  
        print("Other details are:- ")
        print(self.lap.cpu,self.lap.ram)         #calls the show method of the inner class Laptop

    #Inner class
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student("Navin",2)
s2=Student("Jenny",3)

s1.show()

s2.lap.brand="Dell"
s2.lap.cpu="i7"
s2.lap.ram=16

s2.show()