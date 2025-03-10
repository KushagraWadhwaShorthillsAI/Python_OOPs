class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


#Inheriting class A and hence the B class will have all the features of class A (B becomes th child class of A)
# A child class can access all the features of the parent class but the parent class cannot access the features of the child class 
class B(A):   
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


class C(B):
    def feature5(self):
        print("Feature 5 is working")


a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()   


c1=C()
c1.feature3()
c1.feature2()
c1.feature1()