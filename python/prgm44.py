# sum of digits of a number

# a) without recursion

n=int(input("Enter a digit:"))
x=n
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("Sum of digits of",x,"is",sum)

# b) with recursion

def sum(n):
    if not n//10:
        return n
    else:
        return n%10+sum(n//10)
n=int(input("Enter a digit:"))
print("Sum of digits of",n,"is",sum(n))

