#https://docs.google.com/document/d/1xwgVEyR7odIKyJp3T0Ku9MOA2QZhN4XBTrrn9NNuuX4/edit?tab=t.0
#ACTIVITY FINISHED.
#age (integer)
#is_employed (boolean)
#credit_score (integer)
#annual_income (float)
#has_collateral (boolean)

#VARIABLES
age = int(input("Enter your age --> "))
is_employed = bool(input("Are you employed? Write 'True' if yes, leave blank if false --> "))
credit_score = int(input("Enter your credit score --> "))
annual_income = eval(input("Enter your annual income --> "))
has_collateral = bool(input("Do you have collateral? Write 'True' if yes, leave blank if false --> "))

#INPUTTED INFORMATION
print("-------------------------------------------------")
print("-------------INPUTTED INFORMATION----------------")
print()
print("User Age:",age)
print("Employment Status:",is_employed)
print("Credit Score:",credit_score)
print("Annual Income:",annual_income)
print("Collateral Status:",has_collateral)
print()
#CONDITIONS
print("-------------------------------------------------")
print("---------------LOAN ELIGIBILITY------------------")
print()
if age >= 21 and is_employed:
    print("You are eligible for a loan.")
else:
    print("Rejected: Fails baseline criteria.")
print()
print("-------------------------------------------------")
print("--------------FINANCIAL EVALUATION---------------")
print()
interest_rate = 0.0
if age >= 21 and is_employed: #ELEGIBILITY
    print("You are eligible for a loan.")
    if credit_score >= 750 : #TIER 1
        if annual_income >= 100000:
            interest_rate = "Approved at 4.5% interest."
        else:
            interest_rate = "Approved at 5.0% interest."
    elif 600 <= credit_score <= 749: #TIER 2
        interest_rate = "Approved at 8.0% interest."
        if has_collateral:
            interest_rate = "Approved at 7.0% interest."
        if annual_income <= 39999:
            interest_rate = "Approved at 9.5 interest."
    elif credit_score <= 599: #TIER 3
        interest_rate = "Rejected: Credit Score Too Low"
    print(interest_rate)
else:
    print("Rejected: Fails baseline criteria.")







