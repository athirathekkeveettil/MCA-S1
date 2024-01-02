# sum of first N whole numbers

# a)without recursion

n=int(input("Enter a number:"))
sum=0
for i in range(n):
    sum=sum+i
print("sum of first",n,"whole numbers is",sum)

# b)with recursion

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
n=int(input("enter a number:"))
print("sum of first",n,"whole numbers is",sum(n-1))
