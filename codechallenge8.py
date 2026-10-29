# Diamond Pattern TBC
# y = 7, x = 7
rows = 7

for x in range(rows):
  for y in range(rows):
    if x+y == 3 or x+y == 9:
      print("*", end="")
    elif (x != 5 and x+y == 5 and y != 5) or (x != 6 and x+y == 7 and y != 6):
      print("*", end="")
    else:
      print(" ", end="")
  print()
