# factorial of a number
# a) without recursion

def factorial(n):
    factorial=1
    for i in range(1,n+1):
          factorial*=1
          return factorial

n=int(input("Enter the number:"))
print("Factorial of",n,"is",factorial(n))

# b)with recursion

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter the number:"))
print("Factorial of",n,"is",factorial(n))
