#import demo
# and &&, or ||, not !
import getpass #folder

username = "senya"
password = "senyasenya"

u = input("Input USERNAME --->")
p = getpass.getpass("Input PASSWORD --->")

if u == username and p == password :
	print("Username and Password Correct")
else:
	print("Access Denied")
