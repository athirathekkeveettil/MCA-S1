# accept a sentence from user and display the total count of vowels in the sentence

def vowel(n):
    count=0
    for i in n:
        if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u" :
            count+=1
    print("vowel count:",count)
n=input("enter a sentence:")
vowel(n)

