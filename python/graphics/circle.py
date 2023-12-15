
import math
def cir_area(r):
    print("Area of circle:",(math.pi*r*r))

def cir_peri(r):
    print("Perimeter of circle:",(2*math.pi*r))

r=int(input("Enter radius:"))
cir_area(r)
cir_peri(r)
