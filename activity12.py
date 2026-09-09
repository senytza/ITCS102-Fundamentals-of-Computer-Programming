#multiple if and elif conditions
#Creating a python script that captures age groups

name = input("What is your name? ->")
age = int(input("What is your age? ->"))

if age >= 0 and age <=5 :
	print("You are placed in the INFANT group age.")
elif age >= 6 and age <=12 :
	print("You are placed in the KID group age.")
elif age >= 13 and age <=15 :
	print("You are placed in the PRE-TEEN group age.")
elif age >= 6 and age <=19 :
	print("You are placed in the TEENAGER group age.")
elif age >= 20 and age <=25 :
	print("You are placed in the EARLY ADULTHOOD group age.")
elif age >= 26 and age <=29 :
	print("You are placed in the MID ADULTHOOD group age.")
elif age >= 30 and age <=58 :
	print("You are placed in the ADULTHOOD group age.")
elif age >= 59 and age <=150 :
	print("You are placed in the SENIOR group age.")
elif age >=151 :
	print("YOUR AGE IS NOT COUNTED FOR.")


