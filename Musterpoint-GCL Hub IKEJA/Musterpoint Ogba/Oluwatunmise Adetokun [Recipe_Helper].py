print ("Name: Oluwatunmise Adetokun")
print ("Email: oakinset@gmail.com")

print ("Instructor: Dotun Onasanya")
print ("Center: MusterPoint Co-Working Space, Ogba")

print ("Program: Recipe Helper")
print ("This program provides the ingredients needed for predefined foods")

def options():
    print('''Please enter the food you would like to cook: Type 'done' to exit
    > Rice
    > Spaghetti
    > Jollof_Rice
    > Dodo
    > Stew
    > Eba''')
def menu1():
    print("Would you like to continue? a)Yes b)No")
def thanks():
    print("Thank you. The program will now exit")
    
options()
foods = {'Rice' : ["rice", "salt"], 'Spaghetti' : ["spaghetti", "salt", "oil"],'Dodo' : ["plantain", "salt", "oil"], 'Stew' : ["onions", "pepper", "salt", "meat", "tomato", "seasoning"], 'Eba' : ['Garri']}

option = str(input())
while (option.lower() != 'done'):
    if (option in foods.keys()):
        print ("To cook", option, "you'll need the following ingredients:\n",foods[option])
        menu1()
        menu = str(input())
        if (menu.lower() == 'a'):
            options()
            option = str(input())
        elif (menu.lower() == 'b'):
            thanks()
            break
            quit
        else:
            print ("Invalid Choice. Please re-select option...")
            option()
    else:
        print ("The food requested is not predefined.\nPlease select another option:")
        options()
        option = str(input())
