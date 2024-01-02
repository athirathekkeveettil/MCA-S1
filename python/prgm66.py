# create a class rectangle with attributes length and breadth and methods area and perimeter
# compare two rectangle object with their areas

class Rectangle:

   def __init__(self,l=0,b=0):
       self.length=l
       self.breadth=b
   def area(self):
       return self.length*self.breadth
       
   def perimeter(self):
       return self.length+self.breadth
   def __eq__(self,other):
        return self.area()== other.area()


r1=Rectangle(5,4)
r2=Rectangle(4,4)


if r1==r2:
    print("Both are of same area")
else:
    print("Both have different area")
    
        
       
