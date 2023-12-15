a=input("Enter the sentence:")
b={}
for i in a.split():
    b[i]=b.get(i,0)+1
print(b)
