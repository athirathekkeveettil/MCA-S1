# accept a list of integers from user.For all values above 100 store the string "OVER" in the specific position


def listof(n):
    for i in range(0,len(n)):
        if n[i]>100:
            n[i]="OVER"
    print(n)
n=list(map(int,input("enter a list of integers:").split(",")))
listof(n)
