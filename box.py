#FIXED BOX ASTERISK SHAPE  ACTIVITY 17
for x in range(5):
    for y in range(5):
        if x==0 or x==4 or y==0 or y==4:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()



#CHANGABLE BOX SIZE
size = int(input("Enter Box Size: "))



for x in range(size):
    for y in range(size):
        if x==0 or x==size-1 or y==0 or y==size-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
