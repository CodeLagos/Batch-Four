#THIS PROGRAM IS A RANDOM GUESSER GAME
#NAME: OMOJOLA OLUKAYODE (omojola_ilesanmi@ymail.com)
#PROJECT CODE LAGOS 4.0

#THIS LINE PROVIDES RANDOM FIGURES 
import random
randomNumber = random.randint(1,100)

#INITIALISE THE PROGRAM
print("GUESS A NUMBER BETWEEN 1 - 100")
#THIS "WHILE" LOOP IS FOR CONTINUITY
while True:
    while True:
        userGuess = int(input ("YOUR GUESS\n"))
        if userGuess == randomNumber:
            print ("YOU GOT IT!")
            break
#THIS ACTS AS A FLAT        
        elif userGuess >  randomNumber:
            print ("GUESS LOWER!")
            continue
        else:
            print ("GUESS HIGHER!")
            continue
#THIS MAKES THE PROGRAM LOOPABLE
    cont=input("DO YOU WANT TO PLAY AGAIN? Y or N\n")
#THIS TAKES YOUR INPUT AS LOWER CASE
    if cont.lower()=="y":
        continue
    else:
        break
   
   
