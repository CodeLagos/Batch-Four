import sys

#This programs helps in calculating the value of any resistor provided the user enters valid color code of a standard resistor
#The program request the user to input the four color available on a resistor and rather than the user
# to start cracking their brain or using a multimeter to check for the value, the program can just calculate the value



#defining function for the first band
def first(color1):
    
    if color1=="Black":
        value1=0
    elif color1=="Brown":
        value1=1
    elif color1== "Red":
        value1=2
    elif color1== "Orange":
        value1= 3
    elif color1=="Yellow":
        value1= 4
    elif color1=="Green":
        value1= 5
    elif color1== "Blue":
        value1= 6
    elif color1=="Violet":
        value1= 7
    elif color1== "Grey":
        value1= 8
    elif color1== "White":
        value1= 9
    else:
        value1="unknown"
    return value1
def second(color1):
    
    if color1=="Black":
        value1=0
    elif color1=="Brown":
        value1=1
    elif color1== "Red":
        value1=2
    elif color1== "Orange":
        value1= 3
    elif color1=="Yellow":
        value1= 4
    elif color1=="Green":
        value1= 5
    elif color1== "Blue":
        value1= 6
    elif color1=="Violet":
        value1= 7
    elif color1== "Grey":
        value1= 8
    elif color1== "White":
        value1= 9
    else:
        value1="unknown"
    return value1

def multiplier (color):
    if color=="Black":
        value1=1
    elif color=="Brown":
        value1= pow(10, 1)
    elif color== "Red":
        value1=pow(10, 2)
    elif color== "Orange":
        value1= pow(10, 3)
    elif color=="Yellow":
        value1= pow(10, 4)
    elif color=="Green":
        value1= pow(10, 5)
    elif color== "Blue":
        value1= pow(10, 6)
    elif color=="Violet":
        value1= pow(10, 7)
    elif color== "Grey":
        value1= pow(10, 8)
    elif color== "White":
        value1= pow(10, 9)
    else:
        value1="unknown"
    return value1

def tolerance (color):

    if color=="Gold":
        value = 5
    elif color=="Silver":
        value = 10
    else:
        value="unknown"
    return value 


def weight(value):
    if value < 1000:
        print("The resistance value is: ", value,"ohms")
    elif value < 10000:
        print("The resistance value is: ", value/pow(10,4)," K")
    elif value < 100000:
        print("The resistance value is: ", value/pow(10,5)," M")
    else:
        print ("unknown")


def resistor():
    intro()
    print("\n############################################################################# \n")
    band1 = input("Enter the first color: ")
    band2 = input("Enter the second band color: ")
    mult = input("Enter the multiplier: ")
    tol = input("Enter the tolerance color: ")

    # lis =["Black", "black","BLACK", "Brown", "brown", "BROWN", "Red", "red", "RED", "Orange", "orange", "ORANGE", "Yellow", "yellow", "YELLOW", "Green", "green", "GREEN", "Blue", "blue", "BLUE", "Violet", "violet", "VIOLET", "Grey", "grey", "GREY", "White", "white", "WHITE", "Gold", "gold", "GOLD", "Silver","silver", "SILVER"]
    # for band1 in lis and band2 in lis and mult in lis and tol in lis:

    #stripping off the entered values from white spaces
    band1 = band1.strip()
    band2 = band2.strip()
    mult = mult.strip()
    tol = tol.strip()

    #converting the entered values to sentence case
    band1 = band1.title()
    band2 = band2.title()
    mult = mult.title()
    tol= tol.title()    

    if band1.isalpha() and band2.isalpha() and mult.isalpha() and tol.isalpha():
        band1_value = str(first(band1)) + str(second(band2))
        resistance = int(band1_value) * multiplier(mult)
        max_value = resistance + (tolerance(tol)/100)
        min_value = resistance - (tolerance(tol)/100)
        print ("\n")
        #print (weight(resistance))
        print ("The minimun resistance value is : ", min_value, "\n" + " ohms")
        print ("The maximum resistance value is : ", max_value, "\n" + " ohms")
    else:
        print("Either one or more of the value inputed is not a color")

    retry()

def retry():
    choice = input("Do you want to try again? Y/N \n")
    choice = choice.lower()
    if choice == 'y':
        resistor()

    elif choice == 'n':
        sys.exit()
    else:
        print("Invalid input")
        retry()

def intro():
    print("This program calculate the value of a resistor using the standard color code")
    print("This program is created by: Ajumoko Ibrahim Temitope")
    print("Email: ajumokoibrahimtemitope@gmail.com")
    print("Facilitator: Mr. Dotun")


resistor()
