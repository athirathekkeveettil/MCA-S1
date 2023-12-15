a=input("Enter a string:")
a=a.split(",")
a.sort(key=len)
print("Length of longest word",len(a[-1]))
if len(a[-1])==len(a[-2]):
    print("BINGO")
