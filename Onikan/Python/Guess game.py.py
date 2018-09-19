print('''This program is written by lawal opeyemi
      Email address: opee2005ng@yahoo.com
      Phone number: 08087655247''')

Title = input("please your title: \n(a)mr\n(b)mrs\n(c)engr\n(d)miss\n(e)others, please indicate\n")
first_name = input("your first name please: ")
last_name = input("your last name please: ")
print("welcome", Title,first_name, last_name, "to guessing game")
print(" YOU ONLY HAVE FIVE ATTEMPS, WISH YOU LUCK!")

from random import randint
secret_number = randint(1,39) #random number between 1 and 39
for number_guesses in range(5): #you are to provide 5 numbers, one at a time 
    guess_number = eval(input("pleese enter your guess number beteween 1 and 39 (1-39): "))
    if guess_number < secret_number:
        print("HIGHER.", 5-number_guesses, ":guesses left.\n")
    elif guess_number > secret_number:
        print("LOWER.", 5-number_guesses, ":guesses left.\n")
    else:
        print("WAHOOOOOO!!!!!!!!! YOU GOT IT, CONGRATULATION TO YOU",Title,first_name,last_name)
        break
else:
    print(" oh no! you lose. The correct number is ", secret_number, ".Hope you enjoy it, come back later for another trial")
        
                        

