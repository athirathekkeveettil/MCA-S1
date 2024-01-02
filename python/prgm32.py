# to check if a given key already exits in dictionary

d={"id":1,"name":"athira"}
print(d)
key=input("Enter a key to search:")
if key in d:
    print(key in d,"Key already exists")
else:
    print(key in d,"Key not exists")
