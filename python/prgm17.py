a=[1,1,2,3]
b=[]
for i in a:
 if(i not in b):
     b.append(i)
print('The list after removing duplicates',b)
