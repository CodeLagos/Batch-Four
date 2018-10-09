#GUESSING GAME
print("This script is an Interactive guessing game, which will ask the user to guess a number depending on the user specify range. we are using the random module with the raint function to get a random number within the specification.")
import random
guesses_taken= 0
print("Hello! What is your name?")
my_name= input()
number= random.randint(1,20)
print("well,"+my_name+", I am thinking of a number between 1 and 20.")
while guesses_taken<6:
    print("take a guess.")
    guess= input()
    guess= int(guess)
    guesses_taken= guesses_taken+1
    if guess<number:
        print("your guess is too low.")
    if guess>number:
        print("your guess is too high.")
    if guess== number:
        break
if guess== number:
    guesses_taken= str(guesses_taken)
    print("good job," +my_name+"! you guessed my number in" + guesses_taken + "guesses!")
if guess!= number:
    number= str(number)
    print("Nope. The number I was thinking of was:" + number)
