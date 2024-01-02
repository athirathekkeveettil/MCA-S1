# program to search an item in a given list and display the number of occurrences of the given item

def search(n,item):
    count=0
    for i in n:
        if i==item:
            count+=1
    print("Item count=",count)
n=input("Enter a list of numbers:")
n=list(map(int,n.split(",")))
item=int(input("Enter item to search:"))
search(n,item)
    
