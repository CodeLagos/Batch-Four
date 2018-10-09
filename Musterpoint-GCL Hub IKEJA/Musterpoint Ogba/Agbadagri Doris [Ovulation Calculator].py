#!/usr/bin/env python
print("email:\n1doriscrochet@gmail.com\n")
print("Name:\nDoris Agbadagri\n")
print("Project Topic: Calculating ovulation\n")
print("Instructor:\n Dotun Onasanya\n")
print("Venue:\n MusterPoint Ogba")
#this is a single line code while the next line is multiple line comment

"""
This project is useful for ladies only,
well not entirely true because a
""" 

# I imported datetime form the Libary
from datetime import datetime
currentMonth = datetime.now()
print(currentMonth)

#Here you are to input your the day one of your monlty flow
user_input = int(input("What was the first day of your last period:\n"))

#Here you are to input your circle lenght.
#Meanwhile, circle length is usually between 21 days to 31days

cycle_lenght = int(input("How many days is your Circle Lenght \n"))
if cycle_lenght == 25:
    expected_day = 25 + user_input + 10
elif cycle_lenght == 26:
    expected_day = 26 + user_input + 11
elif cycle_lenght == 27:
    expected_day = 27 + user_input + 12
    
elif cycle_lenght == 28:
    expected_day = 28 + user_input + 13
elif cycle_lenght == 29:
    expected_day = 29 + user_input + 14
elif cycle_lenght == 30:
    expected_day = 30 + user_input + 15
elif cycle_lenght == 31:
    expected_day = 31 + user_input + 16
else:
    expected_day = 25 + user_input + 10

if expected_day > 30:
        new_month_expected_day = expected_day - 30
        expected_day = str(new_month_expected_day) + 'of next month'
else:
    expected_day = str(expected_day) + 'of this month'
print("Expected ovulation day is:" + str(expected_day))

    

