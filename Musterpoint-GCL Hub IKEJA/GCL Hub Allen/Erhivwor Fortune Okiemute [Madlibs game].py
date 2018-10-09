print("Welcome to the Madlibs game.")
print("Please make sure you begin every sentence with a Capital letter.")
print()
NAME = input("What is your name?: ")
if NAME=="Madlibs":
      print("Nice to play with my name sake")
else:
      print("Hello " + NAME + ", Welcome to the Madlibs Game. My name is Madlibs")
print()
AGE = int(input("How old are you?: "))
if AGE<20:
      print("I am 20. Show some respect")
elif AGE==20:
      print("We are peers")
else:
      print("Am 20. You're older")
print()
FAVOURITE_GAME = input("What is your favourite game?: ")
if FAVOURITE_GAME=="Madlibs":
      print("We share similar interest, I like that.")
else:
      print("I don't like " + FAVOURITE_GAME +"." + " I prefer playing the Madlibs.")
print()
FAVOURITE_FOOD = input("What's your favourite native food? ")
print("Well, " + FAVOURITE_FOOD + " gives me running stomach, so it's off the menu.")
print()
YOUR_STATE = input("Which state do you come from?: ")
print()
TOWN = input("Where in " +YOUR_STATE+"?: ")
print()
print("My experience in " + YOUR_STATE + " state was so devastating.")
print("My wallet was stolen at " + TOWN+("."))
print("That's an experience I will never forget.")
print()
dream_car = input("What is your dream car? ")
print()
vacation_destination = input("Where would you like to spend vacation? ")
print()
NET_WORTH = input("Your net worth in figures?: ")
print()
print("You seem to be a person with big dreams.")
print("You cannot drive a " + dream_car + " to " + vacation_destination + " so stop dreaming.")
print("Besides, " + NET_WORTH + " naira cannot afford such an expensive car and vacation.")
print()
user_input=int(input("Did you enjoy the MadLibs Game? \nEnter 1 for Yes \nEnter 0 for No \n: "))
if user_input==1:
      print ("Thank you " + NAME + " for playing the MadLibs Game.")
else:
      print( NAME + " go and design your own game.")
