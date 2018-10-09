##Name - Salau Adenike
##Email - kifademi@gmail.com
##Facilitator's name - Mr. Dotun

#Description - This is a short adventure game (or atleast, it is supposed to be), where the user gets to pick various options.
 
import time
  
def dead():
  print("The zombies ate your brain. You failed")
  
 

playername = input("What is your name? \n>") 
print("Welcome to the Zombie Adventure Game 001")

print("Hello", playername, ", Welcome to planet Mars. 2000 years ago, zombies invaded the planet \nand have successfully turned everyone. Since there are no more brains on this \nplanet to eat, their plan is to invade another.")
time.sleep(6) 
print(""" You are the only thing standing between them and Earth.
    you have been sent to defeat the zombie horde.
    You are Humanity's last hope.
    Defeat the zombies and save your World.
      """)    
       

   
def game():
        print("Captain", playername, "\nInstruction : Destroy the zombies and find your way out. Your fate lies in your decision. Choose wisely.")
        print("You wake up inside an abandoned warehouse. You are alone, \nbut you can hear the zombies from somewhere in the building. What do you do?")
        time.sleep(2)
        choose=input("1.Start running \n2. Wait ")
        if choose == '1':
            print("You started running forward. you came across two doors, one to the right, the other to the left. You could no longer hear the zombies. Do you...")
            action= input("1. Open the door to the right? \n2. Open the door to the left? \n3. Turn around and see if the zombies are behind you?")
           
           
            if action == '1':
                print("You pushed open the right door, rushes in and quickly close the door.")
                time.sleep(2)
                print("Inside the room appears a dragon, flamimg at the mouth. Oh no!")
                do = input("1. Flee the room! 2. Slay the dragon 3. Tame the dragon")
            
                if do == '1':
                    print("While attempting to escape from the room, you stumbled and fell on a pile of coins you didn't notice earlier. The zombies heard the sound and burst into the room.")
                    time.sleep(3)
                    dead()            
                    enter=input("\nPress enter to go back to the last checkpoint")
                    game()
                
                elif do == '2':
                    print("As you attempt to fight the dragon, it attacked you,  \nlighting you on fire and you were burnt to crisp.")
                    time.sleep(3)
                    dead()                   
                    enter=input("\nPress enter to go back to the last checkpoint")
                    game()

                elif do == '3':
                    print("You extend a hand towards the dragon. \nIt raises its head, sniff your palm and must have sensed you mean no harm. \nIt then rub its head on your hand. The dragon has been tamed. \nYou climbed onto its back and it flew head first into a hidden wall. you see the zombies in their mass. The dragon lowers its head and breathes fire on them. all the zombies have been burnt. You have saved humanity!!!")
                    print("Thank you for trying the game. If you'd like to play again, type 'game()'to start")

                else:
                    print("You did not select the correct option. Choose from options 1-3")


            elif action == '2':
                 print("You opened the door to the left and quickly dashed in. \nInside, you find a treasure chest and a map. You can only pick one item. Which do you choose?")

                 item =(input("1. Treasure chest 2. The map"))
                 if item == '1':
                    print("Just as you lift the chest, a lever connected to the chest was pulled and a \nhidden door was opened. Out comes the hungry zombies and they attacked you.")
                    time.sleep(3)
                    dead()             
                    enter=input("\nPress enter to go back to the last checkpoint")
                    game()

                 elif item == '2':
                    print("As soon as you pick the map up, \nit starts glowing and shines its light on a hidden button on the wall. Hurry, you only have limited time!")
                    press=(input("Do you... \n1. Press the button? \n2.Fold the map and put it down? "))
                
                    if press == '1':
                        print("A second after you pressed the button, detonation sounds could be heard all \nacross the warehouse. The last group of soldiers deployed here must have planted the bombs but were unable to complete the mission before they were eaten. You quickly hide inside a hole in the room. After the dust cleared out, you saw zombies under the rumbles, all 'dead'. \nHurray! You defeated the zombies.")
                        print("Thank you for trying the game. If you'd like to play again, type 'game()'to start")
                    elif press == '2':
                        print("As soon as you put down the map, the light dissappered, but it was too late. \nThe zombies already saw the reflection. They burst through a hidden door and attacked you.")
                        time.sleep(3)
                        dead()                        
                        enter=input("\nPress enter to go back to the last checkpoint")
                        game()

                    else:
                        print("You took too long and chose the wrong option. The zombies were attracted by the light. They burst into the room through a hidden door and attacked you.")
                        time.sleep(3)
                        dead()                     
                        enter=input("\nPress enter to go back to the last checkpoint")
                        game()

            elif action == '3':
                print("How wise of you. \nThought you would have seen enough horror movies to know you never look back when being chased by deadly creature(s). Well, since you turned, you are lunch!")
                time.sleep(3)
                dead()                
                enter=input("\nPress enter to go back to the last checkpoint")
                game()

            else:
                    print("Please choose either option 1 or 2")   
                
        elif choose =='2':
              print("The zombies caught up with you.")
              time.sleep(3)
              dead()
              enter=input("\nPress enter to go back to the last checkpoint")
              game()

              
        else:
            print("You can only choose to flee or wait. Type game() to start again.") 
            
            
select=input("\nPress 1 to proceed to the game")
if select == '1':
  game()
else:
    print("Error. Invalid selection. type 'game()' to start")
              


            





            
