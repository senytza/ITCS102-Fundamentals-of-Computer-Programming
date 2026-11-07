# X SHAPED ASTERISK CODE:
for x in range(5):
    for y in range(5):
        if x+y == 4 or x==y:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

#CHANGEABLE PARALLELOGRAM SIZE ATTEMPT (UNFINISHED)

count = int(input("Enter Parallelogram Size: "))

for x in range(count):
    for y in range(count):
        if x+y==count-4 or (y==count-4 and x!=count-3 and y!=count-3 and x!=count-2 and y!=count-2 and x!=count-1 and y!=count-1):
            print("*",end=" ")
        elif (y==0 and x+y!=0 and x+y!=count-6 and x+y!=count-5) or (x+y==count-1 and y!=count-4 and y!=count-3 and y!=count-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#TBC
