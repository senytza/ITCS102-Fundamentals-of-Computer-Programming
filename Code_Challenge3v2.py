#Other method WITHOUT using boolean.
#This script works the same way and produces the same expected output.
#However, this method is easier to script and figure out. That's the only difference between the two.
#Thank you for understanding.


customer = input("----------------------------------------\nWhat is the customer's name? ->")
itemType = input("----------------------------------------\nAvailable Items:\nA. Cat Food\nB. Dog Food\nC. Pet Dental Sticks\nWhat type of item are you buying? ->")
weight = float(eval(input("----------------------------------------\nHow much are you buying, in kg? ->")))
distance = float(eval(input("----------------------------------------\nHow far is the shipping distance, in km? ->")))
isFragile = input("----------------------------------------\nIs the item fragile? (True/False) ->") == "True"
isExpress = input("----------------------------------------\nIs the item Express? (True/False) ->") == "True"
isInternational = input("----------------------------------------\nIs the item International? (True/False) ->") == "True"

#COMPUTATION
baseCost = (weight * 2.50) + (distance * 0.15)

#CONDITIONS
if weight <= 2.00 and distance <= 100.00 and not isInternational and not isExpress:
    finalCost = 0.00
elif isExpress and isInternational:
    finalCost = (baseCost * 1.40) + 50
elif isExpress or (isInternational and weight > 20):
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
