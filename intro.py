class Car:


    def __init__(self):
        self.mil=10
        self.com="BMW"


c1= Car()
c2= Car()

c1.mil=8

print(c1.com,c1.mil)
print(c2.com,c2.mil)