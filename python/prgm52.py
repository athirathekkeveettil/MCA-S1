# function to get a new string from a given string by adding 'ls' to the begginning of string ,if already begins with 'ls' return string unchnaged

def string(s):
    if s.startswith('ls'):
        return s
    else:
        return 'ls'+s
s=input("Enter a string:")
print("New String:",string(s))
