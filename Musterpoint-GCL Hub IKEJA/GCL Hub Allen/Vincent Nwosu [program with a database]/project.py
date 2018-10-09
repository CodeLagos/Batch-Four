import time

#This introduces the program
print("My name is Vincent Obioma Nwosu")
print("The name of my Facilitator is Mr. Dotun Onasanya")
print("My center is GCL HUB")
print("The Name of this program is VoN's Database")
print("This program works with a database which is actually a text file.")
print("\n")

#This function pulls out the menu containing four options
def menu():
    print("Welcome to VoN's Database")
    time.sleep(2)
    print("You can:")
    time.sleep(1)
    print("1. Add a name to the database")
    time.sleep(1)
    print("2. View names on the database")
    time.sleep(1)
    print("3. Delete a certain name from the database")
    time.sleep(1)
    print("4. Close the application")

#NOTE: The file path has to correspond to where the database.txt file is saved.
#Any text file can be used with any name but the path should correspond
    
while True:
    menu()
    time.sleep(2)
    print("\n")
    print("Kindly make a selection using number 1 - 4. ")
    time.sleep(1)
    choice = int(input("Type in your number here: "))
    print("\n")
    time.sleep(1)
    
    if choice == 1:
        print("Your choice is number 1")
        time.sleep(1)
        print("\n")
        print("What name would you love to add to the database? ")
        add_name = input("Type in name here: ")
        print("\n")
        time.sleep(1)
        data = open('c://Users/user/desktop/project/database.txt', 'a')
        data.write(add_name + "\n")
        data.close()
        print("\n")
        print(f"Adding {add_name} to the database")
        time.sleep(1)
        print("\n")
        print(f"{add_name} have been added to the database")
        time.sleep(1)
        print("\n")
        input("Press any key to go to the menu")
        time.sleep(1)
        
    elif choice == 2:
        print("Your choice is number 2")
        time.sleep(1)
        print("\n")
        print("Here are the list of names in the database.")
        print("\n")
        time.sleep(1)
        data = open('c://Users/user/desktop/project/database.txt')
        database = data.read()
        print(database)
        print("\n")
        input("Press any key to go to the menu")
        time.sleep(1)
        
    elif choice == 3:
        print("Your choice is number 3")
        time.sleep(1)
        print("Here are the list of names on the database: ")
        print("\n")
        time.sleep(1)
        data = open('c://Users/user/desktop/project/database.txt')
        database = data.read()
        print(database)

        data = open('c://Users/user/desktop/project/database.txt', 'r')
        lines = data.readlines()
        data.close()

        print("What name do you want to delete? ")
        name_to_delete = input("Type in name here: ")
        data = open('c://Users/user/desktop/project/database.txt', 'w')        
        for current_line in lines:
            if current_line != name_to_delete + "\n":
                data.write(current_line)
        data.close()        
        time.sleep(1)
        print(f"{name_to_delete} have been deleted.")
        print("\n")
        time.sleep(1)
        print(f"After deleting {name_to_delete}, here are the current list of names on the database:")
        print("\n")
        time.sleep(1)
        data = open('c://Users/user/desktop/project/database.txt')
        database = data.read()
        print(database)
        input("Press any key to go to the menu")
        time.sleep(1)
        
    elif choice == 4:
        print("Your choice is number 4")
        time.sleep(1)
        print("Bye.")
        break
