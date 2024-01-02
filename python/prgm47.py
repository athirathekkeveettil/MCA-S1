# generate all factors of a given number


def factor(n):
   for i in range(1,n+1):
        if n%i==0:
            print(i)
a=int(input("Enter the number:"))
print("Factors of",a,":")
factor(a)



