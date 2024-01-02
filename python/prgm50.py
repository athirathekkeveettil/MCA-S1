# program that print numbers between 1 to 20
# every multiple of 3 print 'FIZZ'
# every multiple of 5 print 'BUZZ'
# every multiple of both 3 and 5 print 'FIZZBUZZ' instead of original number

def number():
    for i in range(1,21):
        if i%3==0 and i%5==0:
            print("FIZZBUZZ")
        elif i%5==0:
            print("BUZZ")
        elif i%3==0:
            print("FIZZ")
        else:
            print(i)
number()
            
