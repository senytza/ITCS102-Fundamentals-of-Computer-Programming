size = int(input("Input value of a: "))

for a in range(size):
    for b in range(size):
        if a+b == size-1 or a==b:
            print("*", end = " ")
        else:
            print(" ", end =" ")
    print()
