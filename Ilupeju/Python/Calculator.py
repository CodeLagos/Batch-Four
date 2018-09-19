#PROJECT NAME': SIMPLE CALCULATOR
#NAME: ONYEKWUO ANAYOCHUKWU COSMAS
#EMAIL: Onyekwuocosmas@gmail.com
#PHONE NUMBER: 08174518987
#CENTRE: ILLUPEJU
#CLASS: AFTERNOON


import math
from tkinter import *
from math import *

print("Welcome To Cosmas' Calculator \n")


def add(x, y):
    return x+y


def multiplication(x, y):
    return x*y


def subtraction(x, y):
    return x-y


def divide(x, y):
    return x/y


cont = "yes"
while cont == "yes" or cont == "YES":
    print("Select an operator:")
    print("1.Addition \t \t", "2.subtraction \t \t", "3.Division \t \t", "4.multiplication")
    print("5.Square Root \t \t", "6.Factorial \t \t")

    print("Pls make your choice")
    choice = input()
    if choice == "1":
        try:
            num1 = float(input("Enter first number:\t"))
            num2 = float(input("Enter second number:\t"))
            print(num1, "+", num2, "=", round(add(num1, num2), 2))
            print("Do u want to perform another operation? (Yes/No):")
            cont = input()
        except ValueError:
            print("Pls enter a number")

    elif choice == "2":
        try:
            num1 = float(input("Enter first number:\t"))
            num2 = float(input("Enter second number:\t"))
            print(num1, "-", num2, "=", round(subtraction(num1, num2), 2))
            print("Do u want to perform another operation? (Yes/No):")
            cont = input()
        except ValueError:
            print("Pls enter a number")

    elif choice == "3":
        try:
            num1 = float(input("Enter first number:\t"))
            num2 = float(input("Enter second number:\t"))
            print(num1, "/", num2, "=", round(divide(num1, num2), 2))
            print("Do u want to perform another operation? (Yes/No):")
            cont = input()
        except ZeroDivisionError:
            print("You can't divide a number by 0")
        except ValueError:
            print("Pls enter a number")

    elif choice == "4":
        try:
            num1 = float(input("Enter first number:\t"))
            num2 = float(input("Enter second number:\t"))
            print(num1, "*", num2, "=", round(multiplication(num1, num2),2))
            print("Do u want to perform another operation? (Yes/No):")
            cont = input()
        except ValueError:
            print("Pls enter a number")
    elif choice == "5":
        try:
            user = int(input("Input the number: \t"))
            if user < 0:
                print("No square root for negative numbers \n")
                print("Do u want to perform another operation? (Yes/No):")
                cont = input()
        except ValueError:
            print("Pls enter a number")
        else:
            print("Square Root of", user, "=", round(math.sqrt(user), 2))
            print("Do u want to perform another operation? (Yes/No):")
            cont = input()
    elif choice == "6":
        try:
            num1 = float(input("Input number:\t"))
            print("Factorial =", factorial(num1))
            print("Do u want to perform another operation? (Yes/No):")
            cont = input()
        except ValueError:
            print("Only positive whole numbers have factorials..")
    elif cont == "No":
        print(quit())
    else:
        print("Invalid input")