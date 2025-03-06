class Student:
    school="VIS"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3 

#Method to calculate average   
    def avg(self):
        return((self.m1+self.m2+self.m3)/3)
    
#Method to calculate the sum
    def sum(self):
        return(self.m1+self.m2+self.m3)
    

#Mutator Methods- To change the value
    def set_m1(self,value):
        self.m1=value

#Accessor Methods- To retrieve the value
    def get_m1(self):
        return self.m1
    
s1=Student(34,52,23)
s2=Student(89,32,12)

print(s1.avg())
print(s1.sum()) 