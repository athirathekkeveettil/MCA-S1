# sum of numbers
# a)without recursion

def sum(n):
    sum=0
    for i in n:
        sum+=i
    return sum

n=input("Enter numbers:")
n=list(map(int,n.split(",")))
if len(n)==1:
    print("Sum is",n[0])
else:
    print("Sum is",sum(n))


# b)with recursion

def sum(n):
    if len(n)==1:
        return n[0]
    else:
        return n[0]+sum(n[1:])

n=input("Enter numbers:")
n=list(map(int,n.split(",")))
print("Sum is",sum(n))




 
