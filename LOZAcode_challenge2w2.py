#CodeChallenge2w2

#VARIABLES
amount = 19863

#COMPUTATIONS
initialamount = 19863
thousand = initialamount // 1000
initialamount = initialamount % 1000

fivehundred = initialamount // 500
initialamount = initialamount % 500

twohundred = initialamount // 200
initialamount = initialamount % 200

onehundred = initialamount // 100
initialamount = initialamount % 100

fifty = initialamount // 50
initialamount = initialamount % 50

twenty = initialamount // 20
initialamount = initialamount % 20

ten = initialamount // 10
initialamount = initialamount % 10

five = initialamount // 5
initialamount = initialamount % 5

one = initialamount // 1
initialamount = initialamount % 1

#PRINT
print("The amount to be depositted ->", amount)
print("1000 = ", thousand)
print("500 =", fivehundred)
print("200 =", twohundred)
print("100 =", onehundred)
print("50 = ", fifty)
print("20 =", twenty)
print("10 =", ten)
print("5 =", five)
print("1 =", one)
