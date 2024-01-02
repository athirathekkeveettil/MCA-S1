# sort a dictionary in ascending and descending order

d={'id':1,'name':'athira'}
print(d)
d1=sorted(d.items())
print('Ascending :',d1)
d2=sorted(d.items(),reverse=True)
print('Descending : ',d2)
