# MULTIPLICATION TABLE SOLUTION

columns = int(input("Enter amount of columns: "))


for x in range(1,11):
    for y in range(1,columns+1):
        print(x, " x ",y," = ", x*y ,end="\t\t")
    print()

