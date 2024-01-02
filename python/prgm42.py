# fibonacci number

# a)without recursion

n=int(input("enter number:"))
a,b=0,1
for i in range(1,n):
    a,b=b,a+b
print("Fibonacci Number:",a)

# b)with recursion

def fibonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n=int(input("enter number:"))
print("Fibonacci Number:",(fibonacci(n-1)))
