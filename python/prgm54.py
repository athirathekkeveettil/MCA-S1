# remove a specific line from a file

inputfile=False
try:
    inputfile=open("test.txt","r+")
    print(inputfile.read())
    inputfile.seek(0,0)
    inputfile=inputfile.readlines()
    n=int(input("Enter the line to be removed:"))
    inputfile.pop(n-1)
    inputfile.truncate(0)
    inputfile.seek(0,0)
    print("File after removal:")
    print(inputfile.read())

except Exception as e:
    print(e)
finally:
    if inputfile:
        inputfile.close()
