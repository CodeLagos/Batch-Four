#Name: Lawal Mukhtar 
#Center: Ikorodu II
#Email: lmukhtar29@gmail.com
#Project Name: Mortgage calculator
#Supervisor: RexBen
#This program calculates the monthly, weekly and daily repayment on a mortgage loan

#Ask the user for the principal,interest rate and duration of the loan
import sys
while True:
    try:
        while True:
            print('Note: your loan value must be 1000 and above')
            principal=int(input('please enter your loan value:'))
            if principal >=1000:
                break
            print()
            print('Note: your value must be a positive value')
        ann_int_rate=float(input('please enter your interest rate:'))
        for i in range(1>0):
            print(ann_int_rate)
            break
        print('Note: your value must be a positive value')
        num_of_payment=int(input('how many years do u want to calculate for the loan repayment. press \n1) For 1year \n2) For 2years \n3) For 3years \n4) For 4years \
\n5)For 5years \n6) For others \nResponse:'))
        for i in range(1>0):
            print(num_of_payment)
            
#sorting out the monthly interest rate from the annual interest rate
        monthly_int_rate=ann_int_rate/100/12

#sorting out the number of payments over the duraton of the loan
        duration=num_of_payment*12

#mortgage formula
#M=P[r(1+r)^n]/[(1+r)^n-1]
# M= Monthy payment( the program focus)
# P= Principal(loan amount)
# R= Monthly interest rate(by dividing the annual rate by 12)
# N= Number of payments(Months the loan will be repaid)

        monthly_payment=principal * ((monthly_int_rate * (1+monthly_int_rate)**duration )/ ((1+monthly_int_rate)**duration -1))
        weekly_payment=monthly_payment/4
        daily_payment=weekly_payment/7

#The total cost of the payment over the full lenght of loan
        total_cost= (monthly_payment * duration)+principal


        print("Your loan amount of ₦",+principal, "over",duration,"months", "with an intrest rate of %.5f " % monthly_int_rate)
        print("Your Monthly payment will be ₦%.2f " % monthly_payment)
        print("Your Weekly payment will be ₦%.2f " % weekly_payment)
        print("Your Daily payment will be ₦%.2f " % daily_payment)
        print("The total charge on this loan will be ₦%.2f !" % total_cost)
    except ValueError:
            print("please,enter an int() value ie a whole number")


