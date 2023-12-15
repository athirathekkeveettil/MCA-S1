def even(a):
    for item in a:
        if(item==237):break
        elif not item %2:print(item)
a=input("Enter the numbers:")
a=list(map(int,a.split(",")))
even(a)
