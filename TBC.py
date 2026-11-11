# interest rate: 0.00256
# interest = interest rate
# monthly payment = loan * interest
# principal = monthly payment - interest



loan = int(input("Enter the loan amount: $"))
lPeriod = int(input("Enter the loan period in years: "))
# lMonths = lPeriod * 12
iRate = 0.00256
interest = loan * iRate
principal = 4


for x in range(1, 12*lPeriod):
    print(f"{lPeriod} | monthlypayment | {interest} | {principal} | remainingloan")

print(f"Loan {loan}\nPeriod {lPeriod}\nIrate {iRate}\nInterest {interest}\nPrincipal {principal}")



# IBA PA

for x in range(5, 0, -1):
    for y in range(x):
        print(" ",end=" ")
    for z in range(1, 7-x):
        print(z,end=" ")
    for w in range(5,, -1):
        print(w,end=" ")
    print()
