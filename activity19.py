#LOGIN ATTEMPT COUNT WITH WHILE COMMANDS

# from .getpass import getpass

isLogin = False
loginAttempt = 0

u = "Senya"
p = "wisnel"

while not isLogin:
    uname = input("Enter Username:" )
    pword = input("Enter Password:" )
    
    if uname == u and pword == p:
        print("Login Successful.")
        print("Total Login Attempts:",loginAttempt)
        isLogin = True
    else:
        print("Incorrect Login Information:")
        loginAttempt += 1
        isLogin = False
