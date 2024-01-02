# program that accepts an integer from user and raises an value error with abnormal condition
# if the reading is within the 90-120

try:
    n=int(input("Enter the number:"))
    if(n not in range(90,120)):
        raise ValueError
    else:
        print("Value:",n)
except ValueError:
        print("Abnormal Condition!")
