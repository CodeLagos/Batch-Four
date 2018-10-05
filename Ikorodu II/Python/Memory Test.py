print('Name: Badmus Olalekan Abraham \nEmail: abrahamolalekan@gmail.com \nProject Name: Memory Test \nSupervisor name: Rex Ben \nThis is a project that use random module. This is an interracting game, the program randomly select from the word provided and ask the user to guess the letters of a word in five attempts and after that providing clue of the first and last letter for the user to guessed the word that the letter was rightly guessed. I used while, if and elif function to achieve this. The program is case sensitive ensure all response are in lower case')

import random
word = ('pot', 'cooker', 'microwave', 'refrigerator','spoons','knife','plate')
word = random.choice(word)
correct = word
clue = word[0] + word[(len(word)-1):(len(word))]
letter_guess = ''
word_guess = ''
store_letter = ''
count = 0
limit = 5

#Welcome the user, show the user the number of attempts and ask the user to start
print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word for Kitchen equipment')
print('Let\'s begin!')
print('\n')
#Ask the user to guess the letter and the word
while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('no!')
        count += 1

    if count == 2:
        print('\n')
#Give the user the clue
        clue_request = input('Would you like a clue?')
        if clue_request == 'y':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        if clue_request == 'n':
            print('You\'re very brave!')

print('\n')
print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')
while word_guess:
    if word_guess.lower() == correct:
        print('Congrats!')
        break

    elif word_guess.lower() != correct:
        print('Unlucky! The answer was,', word)
        break

print('\n')
quit()
