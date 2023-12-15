a=input("Enter a string:")
print(a)
if a.lower().endswith('ing'):
    a+='ly'
else:
    a+='ing'
print(a)
