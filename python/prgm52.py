# Write lambda functions, each to find area of square, rectangle and triangle.

square=lambda s:print ("area of square=",s*s)
rectangle=lambda l,b:print ("area of rectangle=",l*b)
triangle=lambda ba,h:print ("area of triangle=",0.5*ba*h)
s=int(input("enter the side of the square:"))
l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
h=int(input("enter the height of the triangle:"))
ba=int(input("enter the base of the triangle:"))
square(s)
rectangle(l,b)
triangle(ba,h)
