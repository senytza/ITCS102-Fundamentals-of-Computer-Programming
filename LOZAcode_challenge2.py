#CodeChallenge2
#Bruh_what

#Variables
amount = 19863

#COMPUTATION
thousand = amount // 1000
fivehundred = (amount - (thousand * 1000)) // 500
twohundred = (amount - ((fivehundred * 500) + (thousand * 1000))) // 200
onehundred = (amount - ((twohundred * 200) + (fivehundred * 500) + (thousand * 1000))) // 100
fifty = (amount - ((onehundred * 100) + (twohundred * 200) + (fivehundred * 500) + (thousand * 1000))) // 50
twenty = (amount - ((fifty * 50 ) + (onehundred * 100) + (twohundred * 200) + (fivehundred * 500) + (thousand * 1000))) // 20
ten = (amount - ((twenty * 20) + (fifty * 50 ) + (onehundred * 100) + (twohundred * 200) + (fivehundred * 500) + (thousand * 1000))) // 10
five =(amount - ((ten * 10) + (twenty * 20) + (fifty * 50 ) + (onehundred * 100) + (twohundred * 200) + (fivehundred * 500) + (thousand * 1000))) // 5
one = (amount - ((five * 5) + (ten * 10) + (twenty * 20) + (fifty * 50 ) + (onehundred * 100) + (twohundred * 200) + (fivehundred * 500) + (thousand * 1000))) // 1


#PRINT
print("The Amount to be depositted ->", amount)
print("1000 = ", thousand)
print("500 =", fivehundred)
print("200 =", twohundred)
print("100 =", onehundred)
print("50 = ", fifty)
print("20 =", twenty)
print("10 =", ten)
print("5 =", five)
print("1 =", one)