import random
from random import randint

print("Welcome to My Guessing Game \n Pls. Note that You have five lives...")
count = 0
while True and count <= 5:
    try:
        count += 1
        net = 5-count
        user = int(input("Choose integer between 1 - 10 \n"))
        Random = randint(1, 3)
        if Random == user:
            print("Congrats")
        elif Random != user and count < 6:
            print("System choose", Random, "Try Again")
            print("You have", net, "live left")
        elif count == 5:
            print("Game over", quit())
    except ValueError:
        print("Enter a valid number")