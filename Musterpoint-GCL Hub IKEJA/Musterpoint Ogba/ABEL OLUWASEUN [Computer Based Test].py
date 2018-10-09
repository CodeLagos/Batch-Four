userName = input("      Hello World!!!\n Welcome to CODELAGOS \n\nName: ABEL OLUWASEUN ABIODUN \n\nEmail Address: zabelinas2005@gmail.com \n\nProject Topic: Computer Based Test (Using negative marking)\n\nFacilitator's Name : Mr Dotun Onasanya\n\nCenter : Muster point Co-working Space \n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password
count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
count += 1 # The user has already had one attempt above, therefore count has been incremented by 1 already.

while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.
    
    if count == 3: # Counter, to make sure the user only gets a limited number (3)of attempts
        print("\nThree Username and Password Attempts used. Goodbye") # Lets the user know they have reached their limit
        break # Leave the Loop and the whole program
    
    elif userName == 'pablo' and password == 'canice': # The userName and password is equal to 'pablo' and 'canice', which is correct, they can enter zabelinas!
        print("Welcome! \n") # Welcomes the User, the username and password is correct
        break # Leave the loop and the whole program as the username and passowrd is correct
    
    elif userName != 'pablo' and password != 'canice': # The userName and password is NOT equal to 'pablo' and 'canice', the user cannot enter zabelinas
        print("Your Username and Password is wrong!") # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet
    
    elif userName == 'pablo' and password != 'canice': # The userName is equal to 'pablo', but password is NOT equal to 'canice', the user cannot enter zabelinas
        print("Your Password is wrong!") # Lets the user know that their password is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet
    
    elif userName != 'pablo' and password == 'canice': # The userName is NOT equal to 'pablo', however password is equal to 'canice', the user cannot enter zabelinas
        print("Your Username is wrong!") # Lets the user know that their username is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue# Continue, as the user hasn't managed to get their username and password correct yet

score=0 
question1=input("How many days we have in week?\n(a)4 \n(b)7 \n(c)21 \n(d)30 \n")
if (question1.lower()=="b"):
    print("Correct")
    score=score + 1
else:
    print("wrong")
    score=score - 1
     
question2=input("When is the next general election?\n(a)2017 \n(b)2012 \n(c)2019 \n(d)2018 \n")
if (question2.lower()=="c"):
    print("Correct")
    score=score + 1
else:
    print("wrong")
    score=score - 1
         
question3=input("How many toes does a human body have?\n(a)6 \n(b)2 \n(c)10 \n(d)18 \n")
if (question3.lower()=="c"):
    print("Correct")
    score=score + 1
else:
    print("wrong")
    score=score - 1
    
question4=input("What is the capital of bauchi?\n(a)jalingo \n(b)bauchi \n(c)iseyin\n(d)wammako\n")
if (question4.lower()=="b"):
    print("Correct")
    score=score + 1
else:
    print("wrong")
    score=score - 1

question5=input("Paul Pogba plays for which club?\n(a)Man u \n(b)chelsea \n(c)fc barcelona \n(d)liverpool \n")
if (question5.lower()=="a"):
    print("Correct")
    score=score + 1
else:
    print("wrong")
    score=score - 1
print("your score is", score)

#print("do you want to continue? \nA) Yes \B) No \n")

#if 


