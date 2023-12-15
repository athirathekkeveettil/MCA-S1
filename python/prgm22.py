a=input("Enter a word:")
print(a)
b={}
for i in a:
    b[i]=b.get(i,0)+1
print(b)
