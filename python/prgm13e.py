a=int(input('Enter a future year:'))

b=[i for i in range(2023,a) if((i%400==0)or(i%100!=0)and(i%4==0))]
print('Leap year between 2023 and',a,'are:',b)
