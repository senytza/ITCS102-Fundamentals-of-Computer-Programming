count = 7

for x in range(count):
    for y in range(count):
        if x+y==3 or (y==3 and x!=4 and y!=4 and x!=5 and y!=5 and x!=6 and y!=6):
            print("*",end=" ")
        elif (y==0 and x+y!=0 and x+y!=1 and x+y!=2) or (x+y==6 and y!=4 and y!=5 and y!=6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
