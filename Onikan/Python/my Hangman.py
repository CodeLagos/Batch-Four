#Ubeyday yusuf
#08181108918
#import random
import random

#import time
import time

# create a function
def main():
    #welcoming the user
    #get the user name
    name = input ("What is your name?")
    print ("Hello,"+name,"time to play Hangman!")
    
# close the function
main()

# set the secret word
word = "python"
guesses = ""

    # set the number of turns a player can play
turns = 5

    #wait for 1 sec
time.sleep(1)
print ("Start guessing....")

    # wait for 0.5 sec
time.sleep(0.5)

    #create while loop
while turns >0:
    
        #make a counter that starts with zero
    failed = 0
        #for ecery character in the secret_word
    for char in word:
            #check if the characters is in the players guess
        for char in guesses:
            #if char in guesses:
                #print out the character
                print (char,)
        else:
                    #if not found, print a dash
                print("_"),
                    #and increase the number of counter with one
                failed += 1
                    #if failed is equals to zero
                    #print you won
                if failed == 0:
                    print ("correct")
        break
    print
        #ask the user to guess a character
    guess = input("Guess a character (a alphabet) in the secret word:")
        #set the players guess to guesses
    guesses += guess
    if guess in word:
        print ("Correct")
    else:
            #if the guess is not in the secret word
            #turn counter decrease with 1 (now 4)
        turns -=1
            #print wrong
        print ("Wrong")
            #tell the player the number of turns left
    print ("You have",turns,"more guesses")
        # when there is no more turns left
    while turns == 0:
        print ("sorry, you lost")
        print ("The secret word was"+" " +word)
        print ("Game over")
        break

        
                
    
    
    
