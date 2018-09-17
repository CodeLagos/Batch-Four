#Name: Toluwani Adeseri
#Email: tadeseri@yahoo.com
#Phone number: 08057945070
#Class: Python_Batch 4 Morning
#Centre: Ilupeju

name=input("Hello User, please enter your name: ")
print("You are welcome",name,"to CodeLagos Retirement Savings Calculator created by Toluwani Adeseri")
print("\n")
retirement_age=65
for i in range(18,66):
    current_age=int(input("Please enter your current age between 18 and 65: "))
    if current_age<18:
        print("Sorry, you are not employable because you are less than 18")
    elif current_age>65:
        print("Sorry, you are currently retired")
    else:
        break
deposit=int(input("How much would you be contributing annually to the pension scheme? "))
principal=int(input("How much do you have as opening balance or lumpsum to start with? "))
interest=int(input("What is the estimated average investment return per annum in (%)? "))
years_until_retirement=retirement_age-current_age
print("Calculating...")
RSA_balance=principal*((1+(interest/100))**years_until_retirement)
for i in range(years_until_retirement):
    years_until_retirement-=1
    RSA_balance+=(deposit*((1+(interest/100))**years_until_retirement))
print("\n")
print("Dear",name+", your estimated RSA Balance at Retirement is NGN",round(RSA_balance,2))

