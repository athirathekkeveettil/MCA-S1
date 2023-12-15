def reverse(a):
    for word in a[::-1]:
        print(word,end=" ")


a=input("enter Full Name:")
a=a.split(" ")
reverse(a)
