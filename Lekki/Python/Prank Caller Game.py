#Adebayo Dada
#adebayodada24@gmail.com
#Prankcaller Dice Rolling Game
#Step1: Call up random function to represent Dice
from random import randint
#Step2: Set up an empty list for storing questions that have been played.
questions_store=[]
roll_again=''
#Step3: Using the while loop create a continuous function and set an exit function to terminate the program.
while(roll_again.lower()!='e'):
    roll_again=input('Ready to roll? ENTER=Roll. E=exit')
    if(roll_again.lower()!='e'):
        num_rolled=randint(1,6)
        print('You rolled a', num_rolled)
#Step4: Populate questions list with questions required for game.        
        questions=[
            "In the movie Avengers what is the name of the Character of The Incredible Hulk?\n (a) Bruce Banner\n (b) Tony Stark\n (c) Steve Rogers\n (d) Peter Parker\n",
            "In what year did the series Friends air?\n (a) 1992\n (b) 1997\n (c) 1994\n (d) 1993\n",
            "In the series Greys Anatomy what was Richard Webbers first wifes name?\n (a) Catherine\n (b) Adele\n (c) Ellis\n (d) Miranda\n",
            "What year did World war 2 end?\n (a) 1937\n (b) 1939\n (c) 1947\n (d) 1945\n",
            "Who was the first man to walk on the moon?\n (a) Narmstrong\n (b) JNeismith\n (c) REinstein\n (d) LJames\n",
            "Who was the first governor of california?\n (a) Peter Wilson\n (b) Jerry Brown\n (c) Arnorld Schwarzenegger\n (d) Pater Burnett\n",
            "Which of Marvel Comics author has been cast in every Marvel movie?\n (a) Larry Lieber\n (b) Steve Ditko\n (c) Stan lee\n (d) Jack Kirby\n",
            "In the series Game of Thrones where is the home of the Starks?\n (a) High Garden\n (b) Winterfell\n (c) Dorne\n (d) Dragonstone\n",
            "In the show Family Guy what is Peter Griffins wifes name?\n (a) Marge\n (b) Lisa\n (c) Meg\n (d) Lois\n",
            "Who wrote the book Lord of the rings?\n (a) JR Tolken\n  (b) George RR Martin\n (c) JK Rowlings\n (d) Sidney Sheldon\n"
            ]
#Step5: Populate answers list with answers for the questions asked.
        answers=['a','c','b','d','a','d','c','b','d','a']
#Step6: By using the modulus function match questions with their answers from the 2 lists
        questions[0]==answers[0]
        questions[1]==answers[1]
        questions[2]==answers[2]
        questions[3]==answers[3]
        questions[4]==answers[4]
        questions[5]==answers[5]
        questions[6]==answers[6]
        questions[7]==answers[7]
        questions[8]==answers[8]
        questions[9]==answers[9]
#Step 7: create another list for the tasks to be performed if the answer given is wrong.
        wrong=['Wrong! Call a random number telling them you are coming to kidnap them this night\n',
               'Wrong! Call your dad telling him you have a special secret you have never told him. The secret is you are Batman\n',
               'Wrong! Call your mum up telling her you are pregnant\n',
               'Wrong! Call the police telling them you know who shot 2Pac if they ask who say Your Mama\n',
               'Wrong! Call your neigbor and tell him/her I saw you last night and keep saying it increasing the tone of your voice\n',
               'Wrong! Call up your boss and tell him you hate his gutts and you are going to beat him up\n',
               'Wrong! Call a stranger up and sing to him/her\n',
               'Wrong! Call your dad telling him the worst thing you did?\n',
               'Wrong you have to drink a bottle of vodka\n',
               'Wrong you have to dance to no music at all\n'
               ]
#Step8: Define how the empty list should operation
        selection=randint(0,9)
        if(questions[selection] in questions_store):
            print("You have answered this question")
        else:
            questions_store.append(questions[selection])
#Step9: Randomize the questions asked using the random function.
            A=str(input(questions[selection]))
#Step10: Assign the correct answers to the random questions asked.
            if A==answers[selection]:
                print('You are correct')
            else:
                print('You are incorrect')
                print(wrong[selection])
#Step11: Terminate Prankcaller game.
else:
        print('Thanks for playing')
