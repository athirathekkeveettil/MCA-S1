#program to demonstrate Assert Error for negative input

a = int(input("Enter a number :"))

try:
    assert a>0,"-ve number"
    print(a)

except AssertionError as e:
    print(e)
