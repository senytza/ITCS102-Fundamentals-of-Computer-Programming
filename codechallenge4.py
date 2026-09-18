#ACTIVITY DONE
# import getpass

#LOAN
u = "admin123"
p = "password123"
username = input("Enter Username --> ")
password = input("Enter Password --> ")
loaneeName = "N/A"
jobDescription = "N/A"
has_collateral = "False" or "True"
collateralDescription = "N/A"
collateralValue = 0.0
age = 0
is_employed = True
credit_score = 0
annual_income = 0
loanAmount = 0.0
interest_rate = 0.0
total_amount = loanAmount * interest_rate

#age
if username == u: #LOGIN
    if password == p:
        print(
        "\n-------------------------------------------------"
        "\n------------------LOGIN STATUS-------------------"
        "\n\n\tUser Recognized. Access Authorized."
        "\n\nINPUT INFORMATION:")
        loaneeName = input("Enter your first name --> ")
        jobDescription = input("Enter kind of job --> ") #information not relevant to calculating
        has_collateral = bool(input("Do you have collateral? 'True' if yes, blank if false --> "))
        if has_collateral:
            collateralDescription = input("What kind of collateral do you have? ")
            collateralValue = eval(input("Value of your collateral? "))
            if collateralValue >= 30000:
                print("Collateral accepted.")
                age = int(input("Enter your age --> "))
                if age>=21<=64:
                    is_employed = bool(input("Are you employed?'True' if yes, blank if false --> "))
                    if is_employed:
                        print(
                        "\n-------------------------------------------------"
                        "\n-----------------LOAN ELIGIBILITY----------------"
                        "\n\n\tYou are eligible for a loan."
                        "\n\nINPUT INFORMATION:")
                        credit_score = int(input("Enter your credit score --> "))
                        annual_income = eval(input("Enter your annual income --> "))
                        loanAmount = eval(input("How much will you loan from us? --> "))
                        if credit_score >= 750: #TIER 1
                            if annual_income >= 100000:
                                interest_rate = 4.5
                                total_amount = loanAmount % interest_rate
                                print(
                                "\n-------------------------------------------------"
                                "\n-----------------LOAN DETAILS--------------------"
                                "\nYour interest rate is:", interest_rate,"%"
                                "\nYour loan amount is:", loanAmount,
                                "\nYour total payable is:",total_amount,
                                "\n\n")
                            else:
                                interest_rate = 5.0
                                total_amount = loanAmount % interest_rate
                                print(
                                "\n-------------------------------------------------"
                                "\n-----------------LOAN DETAILS--------------------"
                                "\nYour interest rate is:", interest_rate,"%"
                                "\nYour loan amount is:", loanAmount,
                                "\nYour total payable is:",total_amount,
                                "\n\n")
                        elif 600 <= credit_score <= 749: #TIER 2
                            interest_rate = 8.0
                            total_amount = loanAmount % interest_rate
                            print(
                            "\n-------------------------------------------------"
                            "\n-----------------LOAN DETAILS--------------------"
                            "\nYour interest rate is:", interest_rate,"%"
                            "\nYour loan amount is:", loanAmount,
                            "\nYour total payable is:",total_amount,
                            "\n\n")
                            if has_collateral:
                                interest_rate = 7.0
                                total_amount = loanAmount % interest_rate
                                print(
                                "\n-------------------------------------------------"
                                "\n-----------------LOAN DETAILS--------------------"
                                "\nYour interest rate is:", interest_rate,"%"
                                "\nYour loan amount is:", loanAmount,
                                "\nYour total payable is:",total_amount,
                                "\n\n")
                            if annual_income <= 39999:
                                interest_rate = 9.5
                                total_amount = loanAmount % interest_rate
                                print(
                                "\n-------------------------------------------------"
                                "\n-----------------LOAN DETAILS--------------------"
                                "\nYour interest rate is:", interest_rate,"%"
                                "\nYour loan amount is:", loanAmount,
                                "\nYour total payable is:",total_amount,
                                "\n\n")
                        elif credit_score <= 599:#TIER 3
                            print(
                                "\n-------------------------------------------------"
                                "\n\n\tRejected: Credit Score Too Low\n"
                                "\n-------------------------------------------------")
                    else: #Not employed
                        print(
                            "\n-------------------------------------------------"
                            "\n\n\tRejected: Fails Baseline Criteria.\n"
                            "\n-------------------------------------------------")
                else: #age >= 65:
                    print("Your age is not accounted for.")
            else:#collateralValue <= 29999
                print("Your collateral's value is too low.")
        elif has_collateral is False:
            age = int(input("Enter your age --> "))
            if age>=21<=64:
                is_employed = bool(input("Are you employed?'True' if yes, blank if false --> "))
                if is_employed:
                    print(
                    "\n-------------------------------------------------"
                    "\n-----------------LOAN ELIGIBILITY----------------"
                    "\n\n\tYou are eligible for a loan."
                    "\n\nINPUT INFORMATION:")
                    credit_score = int(input("Enter your credit score --> "))
                    annual_income = eval(input("Enter your annual income --> "))
                    loanAmount = eval(input("How much will you loan from us? --> "))
                    if credit_score >= 750: #TIER 1
                        if annual_income >= 100000:
                            interest_rate = 4.5
                            total_amount = loanAmount * interest_rate
                            print(
                            "\n-------------------------------------------------"
                            "\n-----------------LOAN DETAILS--------------------"
                            "\nYour interest rate is:", interest_rate,"%"
                            "\nYour loan amount is:", loanAmount,
                            "\nYour total payable is:",total_amount,
                            "\n\n")
                        else:
                            interest_rate = 5.0
                            total_amount = loanAmount * interest_rate
                            print(
                            "\n-------------------------------------------------"
                            "\n-----------------LOAN DETAILS--------------------"
                            "\nYour interest rate is:", interest_rate,"%"
                            "\nYour loan amount is:", loanAmount,
                            "\nYour total payable is:",total_amount,
                            "\n\n")
                    elif 600 <= credit_score <= 749: #TIER 2
                        interest_rate = 8.0
                        total_amount = loanAmount * interest_rate
                        print(
                        "\n-------------------------------------------------"
                        "\n-----------------LOAN DETAILS--------------------"
                        "\nYour interest rate is:", interest_rate,"%"
                        "\nYour loan amount is:", loanAmount,
                        "\nYour total payable is:",total_amount,
                        "\n\n")
                        if has_collateral:
                            interest_rate = 7.0
                            total_amount = loanAmount * interest_rate
                            print(
                            "\n-------------------------------------------------"
                            "\n-----------------LOAN DETAILS--------------------"
                            "\nYour interest rate is:", interest_rate,"%"
                            "\nYour loan amount is:", loanAmount,
                            "\nYour total payable is:",total_amount,
                            "\n\n")
                        if annual_income <= 39999:
                            interest_rate = 9.5
                            print(
                            "\n-------------------------------------------------"
                            "\n-----------------LOAN DETAILS--------------------"
                            "\nYour interest rate is:", interest_rate,"%"
                            "\nYour loan amount is:", loanAmount,
                            "\nYour total payable is:",total_amount,
                            "\n\n")
                    elif credit_score <= 599:#TIER 3
                        print(
                            "\n-------------------------------------------------"
                            "\n\n\tRejected: Credit Score Too Low\n"
                            "\n-------------------------------------------------")
                else: #Not employed
                    print(
                        "\n-------------------------------------------------"
                        "\n\n\tRejected: Fails Baseline Criteria.\n"
                        "\n-------------------------------------------------")
            else: #age >= 65:
                print("Your age is not accounted for.")
    else: #Password wrong
        print("Password Incorrect.")
else: #User not accounted for
    print("User Invalid.")

print(
"-------------------------------------------------"
"\n-------------INPUTTED INFORMATION----------------"
"\nLoanee Name:",loaneeName,
"\nJob Description:", jobDescription,
"\nUser Age:",age,
"\nEmployment Status:",is_employed,
"\nCredit Score:",credit_score,
"\nAnnual Income:",annual_income,
"\nCollateral Status:",has_collateral,
"\n\t> Kind of Collateral:",collateralDescription,
"\n\t> Collateral Value:",collateralValue,
"\nLoan Amount:",loanAmount,
"\nInterest Rate:", interest_rate,
"\nTotal Amount Payable:", total_amount
)
# loaneeName = input("Enter your first name --> ")
# jobDescription = input("Enter kind of job --> ") #information not relevant to calculating
# loanAmount = eval(input("How much will you loan from us? --> "))
# is_employed = bool(input("Are you employed? Write 'True' if yes, leave blank if false --> "))
# credit_score = int(input("Enter your credit score --> "))
# annual_income = eval(input("Enter your annual income --> "))


#LOGIN, LOANEE FIRST NAME, JOB DESCRIPTION
#ENTER NAME OF COLLATERAL: E.G ASSETS (LAND, VEHICLE)
#COLLATERAL WORTH SHOULD BE: ANYTHING LESS THAN 30K IS INVALID
#MAXIMUM AGE IS 65
#ASK USER TO SPECIFY LOAN, THEN CALCULATE LOAN'S INTEREST, THEN GIVE USER TOTAL
    
    
# #INPUTTED INFORMATION
# print("-------------------------------------------------")
# print("-------------INPUTTED INFORMATION----------------")
# print()
# print("User Age:",age)
# print("Employment Status:",is_employed)
# print("Credit Score:",credit_score)
# print("Annual Income:",annual_income)
# print("Collateral Status:",has_collateral)
# print()
# #CONDITIONS
# print("-------------------------------------------------")
# print("---------------LOAN ELIGIBILITY------------------")
# print()
# if age >= 21 and is_employed:
#     print("You are eligible for a loan.")
# else:
#     print("Rejected: Fails baseline criteria.")
# print()
# print("-------------------------------------------------")
# print("--------------FINANCIAL EVALUATION---------------")
# print()
# interest_rate = 0.0
# if age >= 21 and is_employed: #ELEGIBILITY
#     print("You are eligible for a loan.")
#     if credit_score >= 750 : #TIER 1
#         if annual_income >= 100000:
#             interest_rate = "Approved at 4.5% interest."
#         else:
#             interest_rate = "Approved at 5.0% interest."
#     elif 600 <= credit_score <= 749: #TIER 2
#         interest_rate = "Approved at 8.0% interest."
#         if has_collateral:
#             interest_rate = "Approved at 7.0% interest."
#         if annual_income <= 39999:
#             interest_rate = "Approved at 9.5 interest."
#     elif credit_score <= 599: #TIER 3
#         interest_rate = "Rejected: Credit Score Too Low"
#     print(interest_rate)
# else:
#     print("Rejected: Fails baseline criteria.")
