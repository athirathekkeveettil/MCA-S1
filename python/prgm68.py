# create a class Rectangle with private attributes length and width overloaded '<' operator to compare the area of two

class Rectangle:
    def __init__(self,l=0,w=0):
        self.__length=l
        self.__width=w
    def area(self):
        return self.__length*self.__width
    def __lt__(self,other):
        return self.area()< other.area()

r1=Rectangle(7,2)
r2=Rectangle(3,4)
r1.area()
r2.area()

if r1 < r2:
    print("Area of r1 is smaller than r2")
else:
    print("Area of r2 is smaller than r1")
