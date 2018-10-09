#This program Calculates the energy consumption in you

from numpy import *
from sys import version

print("This program calculates the power demand and energy consumption of domestic appliances in accordance with the METER READING, BILLING CASH COLLECTION AND CREDIT MANAGEMENT FOR ELECTRICITY SUPPLIES REGULATIONS, 2007\n")
print("Class: Introduction to Python")
print("Facilitator: Mr Dotun\n")
print("Written by Adeyemi Moyosoluwa O. as a project for Code Lagos")
print("moyo_adeyemi@yahoo.com\n")



#Displays the purpose of the program

#Inputs account information
username=str(input("Enter your username: "))
mnumber=str(input("Enter your Meter Number: "))
print("Answer the following questions")

#Prompts for tariff type
print ("1. For Meter With R2SP (Single Phase Residential) Tariff of N21.30/KWH Press 1 \n2. For Meter With C1SP (Single Phase Commercial) Tariff of N27.20/KWH Press 2 \n3.For Meters With C2 (Higher Level Commercial) Tariff of N37.74/KWH Press 3")

tariff=int(input("Enter your option: "))
if tariff==1:
    t=21.30
elif tariff==2:
    t=22.20
elif tariff==3:
    t=37.74
else:
    print("Your Selection is Invalid\n Try Again!!!")

# Initialize the energy units variable
units = 0
app =["Pressing Irons ", 'Toasters','Kettles','Blenders','Microwave ovens','Water Dispensers','Water Heaters','Cookers','Fans','Refrigerators','Air-Conditioners','Televisions','Water Pumps','Washing Machine','Lighting Bulb']
watt=[1200, 1000, 2200, 450, 900, 700, 1500, 2500, 70, 100, 1119,300, 1119, 600, 30]

#create empty list
our_list = []

#Creates a series of input statetements that loops throuth the list of appliances [app] at home
i = 0
for i in range(len(app)):
  number=int(input("How many "+ app[i] + " do you have at home? "))
  #appends the list
  our_list.append(number)

units = 0
for i in our_list: #
    for w in watt:
        units += i*w

print(units)

units =(units/1000)/t

units = round(units, 2)
charge = units*t
charge = round(charge, 2)

print("Hello " + username+ " your Total Energy Consumption is ",units, "KwH" )
print("Your Total Energy Charge per hour is ", charge, "Naira per Hour" )


#charge=bud/100*t









