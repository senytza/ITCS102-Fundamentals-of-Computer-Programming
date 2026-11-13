#LIST AND WHILE

anime = []

isContinue = True

while isContinue:
    ans = input("Do you watch anime [YES/NO]?  ").lower()
    if ans == "yes":
        title = input("What anime did you watch?  ")
        anime.append(title)
        ans = input("Do you watch anime [YES/NO]?  ").lower()
        if ans == "yes":
            print("Continue")
            continue
    else:
        print(anime)
        break
