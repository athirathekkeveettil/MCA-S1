# lambda function to find area of square,rectangle,triangle

# square

s=int(input("Enter side of a square:"))
square=lambda s:s*s
print("Area of square:",square(s))

#rectangle

l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
rectangle=lambda l,b:l*b
print("Area of rectangle:",rectangle(l,b))

#triangle

b=int(input("Enter the breadth:"))
h=int(input("Enter the height:"))
triangle=lambda b,h:0.5*b*h
print("Area of rectangle:",triangle(b,h))


    
