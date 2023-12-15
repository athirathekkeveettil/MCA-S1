# program that accepts an integer from user and raises ValueError with argument 'Abnormal Condition',if the reading is not within 90-120

n=int(input("enter a number:"))
try:
    if n>=90 and n<=120:
        print(n)
    else:
        raise ValueError
except ValueError:
    print("Abnormal Condition!!")
    
    



    
