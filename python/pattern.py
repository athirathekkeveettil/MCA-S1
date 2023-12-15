for i in range(5):
    for j in range(5):
        if j==0   and i in {0,1,2,3,4}:
            print("1",end=" ")
        elif i in {0,1,2,3} and j==1:
            print("2",end=" ")
        elif i in {0,1,2} and j==2:
            print("3",end=" ")
        elif i in {0,1} and j==3:
            print("4",end=" ")
        elif i==0 and j==4:
            print("5",end=" ")
        else:
            print(" ",end=" ")
            
    print()
