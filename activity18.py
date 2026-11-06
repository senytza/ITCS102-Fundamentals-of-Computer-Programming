tuloy = True

while tuloy == True:
  ask = input("Do you wish to continue this program [Y/N]?   ")
  if ask.lower() == "yes":
    print("Continuing.")
    continue
  else:
    print("Stopping.")
    break

