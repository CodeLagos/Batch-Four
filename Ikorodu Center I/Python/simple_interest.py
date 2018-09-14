#Name: AFOLABI ABDUL-MALIK
#This program is to calculate the profit of a trader at every point of sale.
#Prompt user to enter the number of goods to be purchased.
number_of_goods=int(input("please enter the number of goods to be purchased:"))
#Prompt user to enter the actual amount of goods per one.
principal=float(input("please enter the principal:"))
Principal=(principal * number_of_goods)
#Prompt user to enter rate
rate=float(input("please enter the rate:"))
#prompt user to enter time
time=float(input("please enter the time:"))
interest=(principal * rate * time)/100
print(round(interest, 2))
principal =input("enter the principal")
interest =input("enter the interest")
total=(principa + interest)
print(total)
