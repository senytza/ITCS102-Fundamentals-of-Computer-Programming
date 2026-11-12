# interest rate: 0.00256
# interest = interest rate * loan
# monthly payment = interest+prncpl
print("\tTASK #1\n")
loan = int(input("Enter the loan amount: $"))
lPeriod = int(input("Enter the loan period in years: "))
iRate = 0.00256
remLoan = loan
interest = remLoan*iRate
months = lPeriod*12
principal = loan / months
monthPay = interest+principal

# print(f"\n\nLoan: {loan}"
# f"\nPeriod: {lPeriod}"
# f"\nInterest Rate: {iRate}"
# f"\nRemaining Loan: {remLoan}"
# f"\nInterest: {interest}"
# f"\nPeriod in Months: {months}"
# f"\nPrincipal: {round(principal, 2)}"
# f"\nMonthly Payment: {round(monthPay, 2)}\n\n")
print(
    "Payment Schedule"
    "\nMonth\t|  Monthly Payment\t|  Interest\t|  Principal\t\t|  Remaining Loan"
    "\n-----------------------------------------------------------------------------------------")
for x in range(0, 12*lPeriod):
    interest = remLoan*iRate
    monthPay = interest+principal
    remLoan = remLoan-principal
    for y in range(1):
        print(f"{x+1}\t|  ${round(monthPay, 2)}\t\t| ${round(interest, 2)}\t\t| ${round(principal, 2)}\t\t| ${round(remLoan, 2)}")
    print(end="")

print(
    "\n-----------------------------------------------------------------------------------------"
    "\n-----------------------------------------------------------------------------------------"
    "\n\n\tTASK #2\n")

for x in range(7):
    for y in range(13):
        if x==6 or x+y==6 or x==y-6:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print(
    "\n-----------------------------------------------------------------------------------------"
    "\n-----------------------------------------------------------------------------------------"
    "\n\n\tTASK #3\n")

for x in range(9):
    for y in range(5):
        if x==0 or x==4 or x+y==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
