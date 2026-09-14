#Code Challenge 3
#Global Freight Calculator
#Calculate shipping cost: eval(): weightKG, distanceKM | input():name, weight, distance | "boolean" == True: isFragile
#STUDENT'S COMMENT FOR TEACHER: Sir M, it wasn't clarified at the beginning that for a bool(input()) to be FALSE, it MUST be left blank. Hence the confusion of the student.
#Using the BOTH bool(input()) classes for the specified variables must have caused confusion for the students solely because of this unmentioned fact.
#Admittedly, I had to search up online (Did NOT ask AI to make the code) and ask for help from friends to identify the problem at hand.
#Additionally, I will include in another file another method without using the boolean. It will be named "Code_Challenge3v2" on my github account: "senytza" under the ITCS102-Fundamentals-of-Computer-Programming.


#VARIABLES
customer = input("----------------------------------------\nWhat is the customer's name? ->")
itemType = input("----------------------------------------\nAvailable Items:\nA. Cat Food\nB. Dog Food\nC. Pet Dental Sticks\nWhat type of item are you buying? ->")
weight = float(eval(input("----------------------------------------\nHow much are you buying, in kg? ->")))
distance = float(eval(input("----------------------------------------\nHow far is the shipping distance, in km? ->")))
isFragile = bool(input("----------------------------------------\nIs the item fragile? If yes, enter 'True'. If not, STRICTLY leave blank. ->"))
isExpress = bool(input("----------------------------------------\nIs the item Express? If yes, enter 'True'. If not, STRICTLY leave blank. ->"))
isInternational = bool(input("----------------------------------------\nIs the item International? If yes, enter 'True'. If not, STRICTLY leave blank. ->"))

#COMPUTATION
baseCost = (weight * 2.50) + (distance * 0.15)

#CONDITIONS
if weight <= 2.00 and distance <= 100.00 and isInternational != True and isExpress != True:
    finalCost = 0.00
elif isExpress == True and isInternational == True:
    finalCost = (baseCost * 1.40) + 50
elif isExpress == True or (isInternational == True and weight > 20):
    finalCost = (baseCost * 1.20) + 25
elif weight > 30 or distance > 1000:
    finalCost = baseCost + 30
else:
    finalCost = baseCost

print("----------------------------------------\nORDER INFORMATION")
print("Customer Name:", customer)
print("Type of Item:", itemType)
print("Weight:",weight,"kg")
print("Distance:",distance,"km")
print("Fragility Status:", isFragile)
print("Rush Shipping Status:", isExpress)
print("International Shipping Status:", isInternational)
print("Total Shipping Cost: $",finalCost)

