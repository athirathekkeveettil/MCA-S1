# write lambda function :-

# a) To find largest of numbers

largest=lambda a,b: print(a) if a>b else print(b)
largest(2,4)

# b) To check the input number is divisible by 5

number=lambda a:print("Divisible by 5",not a%5)
number(6)

# c) To remove all strings with length <5 from a list of strings

s=input("enter a string:")
string=list(filter(lambda x:len(x)>=5,s.split()))
print(string)

# d) To increment a list of integers by 10% if the number is greater than 1000 else by 5%

numbers=[230,1500]
increment=lambda x:x+x * 0.1 if x > 1000 else x+x*.05
result=list(map(increment,numbers))
print(result)
