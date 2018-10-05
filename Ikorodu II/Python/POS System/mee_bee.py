#welcome user
import sys
#Print App name, Creator's info and Supervisor's name to user
print("App Name: Bee's Pay\nCreator: Lawal Habeebah Oyindamola \nEmail: \
damolabee5@gmail.com \nSupervisor's name: Rex Ben")
print()
print('welcome to Union Bank')
#Print Address to user
print ('The place resturant\nplot 36, mobolaji Johnson way Alausa Ikeja Lagos\n')

while True:
#Prompt user to enter 'yes' to continue with progam or 'no' to end program
#".strip()" absorbs any space after the string that may lead to an error
#".lower()" converts upper case to lower
 choice=input('\n\nEnter yes if you would like to perform transaction or no to end \
the program\n: ').strip().lower()
#A while loop in case of an invalid input from user
 while choice != 'yes' and choice != 'no':
     choice = input("\nInvalid input: \nEnter 'yes' to perform a transaction or \
'no' to close the program: ")

 if choice=="yes":
#Prompt user for response
    response=input('\nchoose your option\n 1. Enter your card pin\n 2. Enter \
the last four digit on your card\n 3. Enter your acct number\n: ')
#A while loop in case of an invalid input from user
    while response != '1' and response != '2' and response != '3':
        response = input("\nInvalid Input: Enter either '1', '2', or '3'\
\n\nchoose your option\n 1. Enter your card pin\n 2. Enter the last four digit \
on your card\n 3. Enter your acct number\n: ")

    if response=='1':
#Prompt user to enter pin
        pin=input('Enter your pin\n: ')
#A while loop to check length of pin
        while len(pin)<=0:
            pin=input('Invalid pin:\nEnter your pin: ')
#Prompt user to select acct type. 1 for savings, 2 for current
        service=input('Enter 1 for savings\nEnter 2 for current\n: ')
#A while loop in case of an invalid input from user
        while service != '1' and service != '2':
            service=input('Invalid Input:\nEnter 1 for savings\nEnter 2 for \
current\n: ')
        if service =="1":
            while True:
                try:
#Prompt user to enter amount, while a ValueError has been set in case of....
#an invaliid input
                    amount=int(input('Enter the amount required\n: '))
                    break
                except ValueError:
                    print('\nInvalid Input')
#Print transaction details to user
            print(amount,'is received successfully')


        elif  service =="2":
            while True:
                try:
#Prompt user to enter amount, while a ValueError has been set in case of....
#an invaliid input
                    amount=int(input('Enter the amount required\n: '))
                    break
                except ValueError:
                    print('\nInvalid Input')
#Print transaction details to user
            print(amount,'is received successfully')

        else:
            print('Your request is invalid')


    elif response=='2':
        while True:
            try:
#Prompt user to enter last four digits on their card
                name=input('Enter the last four digit on your card\n: ')
                break
            except ValueError:
                print('\nInvalid Input')
#A list containing different ints just to represent registered user
        my_dico={"0011":"Ileyemi Odunayo","0012":"Talofeku Emiotisetan","0013\
":"shebaleshe jekinsimi\n: "}
#If user is registered, print to user that they have logged in
        if name in my_dico:
            print('Acct no. identified')

            while True:
                try:
#Prompt user to enter pin, while a ValueError has been set in case of....
#an invaliid input
                    pin=int (input('Pls enter your pin\n '))
                    break
                except ValueError:
                    print('\nInvalid Input')
            if pin>=0:
#Prompt user to select acct type. 1 for savings, 2 for current
                service=input('Enter 1 for savings\npress 2 for current\n: ')
#A while loop in case of an invalid input from user
                while service != '1' and service != '2':
                    service=input('Invalid Entry:\nEnter 1 for savings\nEnter \
2 for current\n: ')
                if service =="1":
                    while True:
                        try:
#Prompt user to enter amount, while a ValueError has been set in case of....
#an invaliid input
                            amount=int(input('enter the amount required\n: '))
                            break
                        except ValueError:
                            print('\nInvalid Input')
#Print transaction details to user
                    print(amount,'is received successfully')
                elif service =="2":

                    while True:
                        try:
#Prompt user to enter amount, while a ValueError has been set in case of....
#an invaliid input
                            amount=int(input('Enter the amount required \n: '))
                            break
                        except ValueError:
                            print('\nInvalid Input')
#Print transaction details to user
                    print(amount,'is received successfully')
                else:
                    print('Your request is invalid')
        else:
            print('Your pin is invalid')
        


    elif response=='3':
#Prompt user to enter acct no.
        acct_num=int(input('Enter your acct number\n: '))
#A list to represent registered user
        my_dico={12345, 56789, 98765} 
        if acct_num in my_dico:
#Prompt user to enter pin
            pin=input('Pls enter your pin: ')
            print(acct_num,'is confirmed')
            if len(pin)>=0:
#Prompt user to select acct type. 1 for savings, 2 for current
                service=input('Enter 1 for savings\npress 2 for current\n: ')
#A while loop in case of an invalid input from user
                while service != '1' and service != '2':
                    service = input('\nInvalid entry:\nEnter 1 for savings\npress\
2 for current\n: ')
                if service =="1":
                    while True:
                        try:
#Prompt user to enter amount, while a ValueError has been set in case of....
#an invaliid input
                            amount=int(input('\nenter the amount required\n  '))
                            break
                        except ValueError:
                            print('\nInvalid Input')
#Print transaction details to user
                    print('\n',amount,'is received successfully ')

                elif service =="2":
                    while True:
                        try:
#Prompt user to enter amount, while a ValueError has been set in case of....
#an invaliid input
                            amount=int(input('enter the amount required \n  '))
                            break
                        except ValueError:
                            print('\nInvalid Input')
#Print transaction details to user
                    print('\n',amount,' is received successfully ')
                else:
                    print('Your request is invalid')
        else:
            print('your acct is invalid')
            
 else:
    sys.exit()
