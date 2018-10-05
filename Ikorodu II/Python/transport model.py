#Name: Lawal Solomon Adeniyi
#Center: Ikorodu II
#Supervisor: RexBen
#This program uses the transportation model via the least cost method to compute BRT management
#The app will estimate how much the transport company can make from maximizing buses attached to locations
#The app can also be used to determine the number of buses assigned to each location

#Assume bus capacity is 70 based on 50 seater and 20 standing but at same price


#Define the basic distances (All distances are in Km)
#Assume buses can come from the parks that are at Ogolonto and Marina
#Assume that the pickup points where passengers access buses are Ikorodu, Ketu, Maryland, Fadeyi and CMS
ogolonto_to_ikorodu = 100
ikorodu_to_ketu = 600
ketu_to_maryland = 400
maryland_to_fadeyi = 500
fadeyi_to_cms = 300
marina_to_cms = 150

#Define the operational cost for mobilizing transportation from each location based on each passenger
#All costs are in Naira
cost_ogolonto_to_ikorodu = 1000
cost_ikorodu_to_ketu = 2000
cost_ketu_to_maryland = 1500
cost_maryland_to_fadeyi = 1500
cost_fadeyi_to_cms = 1000
cost_marina_to_cms = 500

#Define the price of transportation for passengers from one location to another
#All prices are in Naira
price_ikorodu_to_ketu = 100
price_ikorodu_to_maryland = 150
price_ikorodu_to_fadeyi = 200
price_Ikorodu_to_cms = 25
price_cms_to_ikorodu = 250
price_cms_to_ketu = 200
price_cms_to_maryland = 150
price_cms_to_fadeyi = 100

#Define the average number of passengers each location can cater for at a time
#The values are in terms of people
ikorodu_passenger = 850
ketu_passenger = 400
maryland_passenger = 250
fadeyi_passenger = 280
cms_passenger = 550

#Assume the number of buses available in for each rotation are given below
marina_buses = 30
ogolonto_buses = 50

#Initialise available buses to determine how many buses should be sent based on available passengers
ikorodu_bus = 0
cms_bus =0

def send_ikorodu_bus():
    marina_buses = 30
    ogolonto_buses = 50
    ikorodu_bus = 0
    cms_bus =0
    if ikorodu_passenger <= 150 and ogolonto_buses >= 1:
        ikorodu_bus += 1
        ogolonto_buses -=1
        print("The transport company is sending ",ikorodu_bus, " buses immediately")
    elif ikorodu_passenger <= 250 and ogolonto_buses <= 2:
        ikorodu_bus += 2
        ogolonto_buses -=2
        print("The transport company is sending ",ikorodu_bus, " buses immediately")
    elif ikorodu_passenger <= 650 and ogolonto_buses >= 6:
        ikorodu_bus += 6
        ogolonto_buses -=6
        print("The transport company is sending ",ikorodu_bus, " buses immediately")
    elif ikorodu_passenger >= 550 and ogolonto_buses >= 5:
        ikorodu_bus += 5
        ogolonto_buses -=5
        print("The transport company is sending ",ikorodu_bus, " buses immediately")
    elif ikorodu_passenger >= 450 and ogolonto_buses >= 4:
        ikorodu_bus += 4
        ogolonto_buses -=4
        print("The transport company is sending ",ikorodu_bus, " buses immediately")
    elif ikorodu_passenger >= 350 and ogolonto_buses >= 3:
        ikorodu_bus += 3
        ogolonto_buses -=3
        print("The transport company is sending ",ikorodu_bus, " buses immediately")
    elif ikorodu_passenger >= 250 and ogolonto_buses >= 2:
        ikorodu_bus += 2
        ogolonto_buses -=2
        print("The transport company is sending ",ikorodu_bus, " buses immediately")
    elif ikorodu_passenger >= 150 and ogolonto_buses >= 1:
        ikorodu_bus += 1
        ogolonto_buses -=1
        print("The transport company is sending ",ikorodu_bus, " bus immediately")
    else:
        ikorodu_bus += 0
        print("Sorry, it is either that the transport company either doesnt have enough buses available presently"
              "Or wait till the available passengers are up to 150")

def send_cms_bus():
    if cms_passenger >= 550 & marina_buses >= 5:
        cms_bus += 5
        print("The transport company is sending ",cms_bus, " buses immediately")
    elif cms_passenger >= 450 & marina_buses >= 4:
        cms_bus += 4
        print("The transport company is sending ",cms_bus, " buses immediately")
    elif ikorodu_passenger >= 350 & marina_buses >= 3:
        cms_bus += 3
        print("The transport company is sending ",cms_bus, " buses immediately")
    elif ikorodu_passenger >= 250 & marina_buses >= 2:
        cms_bus += 2
        print("The transport company is sending ",cms_bus, " buses immediately")
    elif ikorodu_passenger >= 100 & marina_buses >= 1:
        cms_bus += 1
        print("The transport company is sending ",cms_bus, " bus immediately")
    else:
        cms_bus += 0
        print("Sorry, it is either that the transport company either doesnt have enough buses available presently"
              "Or wait till the available passengers are up to 100")

def send_ketu_bus():
    ketu_bus = 5
    if ketu_passenger >= 150 & ketu_bus>0:
        buses = ketu_passenger//150
        if buses <= 5:
            ikorodu_bus -= buses
            print("The transport company is sending ",buses, " buses immediately")
        if buses > 5:
            print("The transport company is immediately sending five buses though it may not be sufficient for everyone"
              "\nplease bear with us")
        elif buses < 0:
            print("The transport company will send a bus once passengers are up to 150")
    else:
        print("Something is wrong with your entry")
        

def send_maryland_bus():
    maryland_bus = 5
    if maryland_passenger >= 150 & maryland_bus>0:
        buses = maryland_passenger//150
        if buses <= 5:
            maryland_bus -= buses
            print("The transport company is sending ",buses, " buses immediately")
        if buses > 5:
            print("The transport company is immediately sending five buses though it may not be sufficient for everyone"
              "\nplease bear with us")
        elif buses < 0:
            print("The transport company will send a bus once passengers are up to 150")
    else:
        print("Something is wrong with your entry")

def send_fadeyi_bus():
    fadeyi_bus = 5
    if fadeyi_passenger >= 150 & fadeyi_bus>0:
        buses = fadeyi_passenger//150
        if buses <= 5:
            fadeyi_bus -= buses
            print("The transport company is sending ",buses, " buses immediately")
        if buses > 5:
            print("The transport company is immediately sending five buses though it may not be sufficient for everyone"
              "\nplease bear with us")
        elif buses < 0:
            print("The transport company will send a bus once passengers are up to 150")
    else:
        print("Something is wrong with your entry")



#Define the price of transportation for passengers from one location to another
#All prices are in Naira

#Define bus administrator function
def expenditure():
    cost_ogolonto_to_ikorodu = 1000
    cost_ikorodu_to_ketu = 2000
    cost_ketu_to_maryland = 1500
    cost_maryland_to_fadeyi = 1500
    cost_fadeyi_to_cms = 1000
    cost_marina_to_cms = 500
    sent_ogolontobuses = int(input("How many buses have you sent from Ogolonto today? \nResponse: "))
    sent_Marinabuses = int(input("How many buses have you sent from Marina today? \nResponse: "))
    ikorodu_ketu = int(input("How many buses have you sent from Ikorodu to Ketu? \nResponse: "))
    ketu_maryland = int(input("How many buses have you sent from Ketu to Maryland? \nResponse: "))
    maryland_fadeyi = int(input("How many buses have you sent from Maryland to Fadeyi? \nResponse: "))
    fadeyi_cms = int(input("How many buses have you sent from Fadeyi to CMS? \nResponse: "))
    ketu_ikorodu = int(input("How many buses have you sent from Ketu to Ikorodu? \nResponse: "))
    maryland_ketu = int(input("How many buses have you sent from Maryland to Ketu? \nResponse: "))
    fadeyi_maryland = int(input("How many buses have you sent from Fadeyi to Maryland? \nResponse: "))
    cms_fadeyi = int(input("How many buses have you sent from CMS to Fadeyi? \nResponse: "))

    ogolonto_expenditure1=(cost_ogolonto_to_ikorodu*sent_ogolontobuses)+(ikorodu_ketu*cost_ikorodu_to_ketu)+(cost_ketu_to_maryland*ketu_maryland)
    ogolonto_expenditure2=(cost_maryland_to_fadeyi*maryland_fadeyi)+(cost_fadeyi_to_cms*fadeyi_cms)
    marina_expenditure1=(cost_marina_to_cms*sent_Marinabuses)+(ketu_ikorodu*cost_ikorodu_to_ketu)+(maryland_ketu*cost_ketu_to_maryland)
    marina_expenditure2=(cost_maryland_to_fadeyi*fadeyi_maryland)+(cost_fadeyi_to_cms*cms_fadeyi)
    expenditure = ogolonto_expenditure1+ogolonto_expenditure2+marina_expenditure1+marina_expenditure2
    print("The total daily expenditure for Today is ",expenditure, " Naira.")

def income():
    bus_capacity = 70
    price_ikorodu_to_ketu = 100
    price_ikorodu_to_maryland = 150
    price_ikorodu_to_fadeyi = 200
    price_Ikorodu_to_cms = 25
    price_cms_to_ikorodu = 250
    price_cms_to_ketu = 200
    price_cms_to_maryland = 150
    price_cms_to_fadeyi = 100
    
    ikorodu_ketu = int(input("How many buses have you sent from Ikorodu to Ketu? \nResponse: "))
    ketu_maryland = int(input("How many buses have you sent from Ketu to Maryland? \nResponse: "))
    maryland_fadeyi = int(input("How many buses have you sent from Maryland to Fadeyi? \nResponse: "))
    fadeyi_cms = int(input("How many buses have you sent from Fadeyi to CMS? \nResponse: "))
    ketu_ikorodu = int(input("How many buses have you sent from Ketu to Ikorodu? \nResponse: "))
    maryland_ketu = int(input("How many buses have you sent from Maryland to Ketu? \nResponse: "))
    fadeyi_maryland = int(input("How many buses have you sent from Fadeyi to Maryland? \nResponse: "))
    cms_fadeyi = int(input("How many buses have you sent from CMS to Fadeyi? \nResponse: "))

    ogolonto_income1=(ikorodu_ketu*price_ikorodu_to_ketu)+(price_ketu_to_maryland*ketu_maryland)
    ogolonto_income2=(price_maryland_to_fadeyi*maryland_fadeyi)+(price_fadeyi_to_cms*fadeyi_cms)
    marina_income1=(ketu_ikorodu*price_ikorodu_to_ketu)+(maryland_ketu*price_ketu_to_maryland)
    marina_income2=(price_maryland_to_fadeyi*fadeyi_maryland)+(price_fadeyi_to_cms*cms_fadeyi)
    income = (ogolonto_income1+ogolonto_income2+marina_income1+marina_income2)*bus_capacity
    print("\nThe total daily income for Today is ",income," Naira.")

def daily_report():
    income()
    expenditure()
    

def admin_function():
    function = input("Welcome Administrator, Please What do you want to do?"
                "\n1 Daily Expenditures \n2 Daily Income \n3 Daily Report"
                "\nResponse: ")
    while True:
        try:
            if function == '1':
                expenditure()
            if function == '2':
                income()
            if function == '3':
                daily_report()
            break
        except ValueError as e:
            print("\nNon-numeric data found; insert integers only")
            print(e)
        except IOError as e:
            print("\nAn error occurred trying to read the file; insert integers only")
            print(e)
        except UnicodeDecodeError as e:
            print("\nThis input is not acceptable; insert integers only")
            print(e)
        except EOFError as e:
            print("\nYou just hit an end-of-file condition; insert integers only")
            print(e)
        except KeyboardInterrupt as e:
            print("\nYou cancelled the operation; insert integers only")
            print(e)
        except ImportError as e:
            print("\nNo module found; insert integers only")
            print(e)
    


#Define bus passenger function
def user_menu():
    passcode = input("\nWelcome to the Passenger end of the Blue Bus Transport App, Please What do you want to do?"
                "\n1 Request for Bus \n2 Request for bus fare"
                "\nResponse: ")
    if passcode == '1':
        bus_request = int(input("\nWhat is your present location? Please, this app works for Buses at Ikorodu and CMS only"
                            "\nSelect one of the options below"
                            "\n1 Ikorodu \n2 CMS \n\nResponse: "))
        destination = int(input("\nWhere is your destination? Select one of the options below"
                            "\n1 Ikorodu \n2 Ketu \n3 Maryland"
                            "\n4 Fadeyi \n5 CMS \n\nResponse: "))
        if bus_request == 1 and destination == 2:
            ikorodu_passenger = int(input("How many passengers are presently on the queue going to Ketu? /nResponse: "))
            send_ikorodu_bus()
        elif bus_request == 1 and destination == 3:
            ikorodu_passenger = int(input("How many passengers are presently on the queue going to Maryland? /nResponse: "))
            send_ikorodu_bus()
        elif bus_request == 1 & destination == 4:
            ikorodu_passenger = int(input("How many passengers are presently on the queue going to Fadeyi? /nResponse: "))
            send_ikorodu_bus()
        elif bus_request == 1 and destination == 5:
            ikorodu_passenger = int(input("How many passengers are presently on the queue going to CMS? /nResponse: "))
            send_ikorodu_bus()
        
        elif bus_request == 2 and destination == 1:
            cms_passenger = int(input("How many passengers are on the queue going to Ikorodu? /nResponse: "))
            send_cms_bus()
        elif bus_request == 2 and destination == 3:
            cms_passenger = int(input("How many passengers are on the queue going to Maryland? /nResponse: "))
            send_cms_bus()
        elif bus_request == 3 and destination == 4:
            cms_passenger = int(input("How many passengers are on the queue going to Fadeyi? /nResponse: "))
            send_cms_bus()
        elif bus_request == 2 and destination == 5:
            cms_passenger = int(input("How many passengers are on the queue going to CMS? /nResponse: "))
            send_cms_bus()
        else:
            print("Your response have errors; Incorrect input!!!")
    
    if passcode == '2':
         bus_request = int(input("What is your present location? Please, this app works for Buses at Ikorodu and CMS only"
                            "\nSelect one of the options below"
                            "\n1 Ikorodu \n2 CMS \n\nResponse: "))
         destination = int(input("Where is your destination? Select one of the options below"
                            "\n1 Ikorodu \n2 Ketu \n3 Maryland"
                            "\n4 Fadeyi \n5 CMS \n\nResponse: "))
         if bus_request == 1 and destination == 2:
             print("Your fare from Ikorodu to Ketu is 100 Naira")
         elif bus_request == 1 and destination == 3:
            print("Your fare from Ikorodu to Maryland is 150 Naira")
         elif bus_request == 1 and destination == 4:
            print("Your fare from Ikorodu to Fadeyi is 200 Naira")
         elif bus_request == 1 and destination == 5:
            print("Your fare from Ikorodu to CMS is 250 Naira")
         elif bus_request == 2 and destination == 1:
            print("Your fare from CMS to Ikorodu is 250 Naira")
         elif bus_request == 2 and destination == 1:
            print("Your fare from CMS to Ketu is 200 Naira")
         elif bus_request == 2 and destination == 3:
            print("Your fare from CMS to Maryland is 150 Naira")
         elif bus_request == 2 and destination == 4:
            print("Your fare from CMS to Fadeyi is 100 Naira")            
         else:
            print("Your input is incorrect")
    return False

#Define bus administrator login
def admin_log():
    trial = 0
    while trial < 4:
        pin = input('Welcome to the administrative end of the Blue Bus Transport App, Please Enter the 4 Digit Pin: ')
        if pin == '1111':
            print("Pin accepted!")
            return admin_function()
        else:
            print("Invalid pin")
            trial += 1
    print("Too many incorrect tries. Could not log you in")
    return False
        
    
#Develop the Main Menu
def main_menu():
    try:
        user = int(input("You are welcome to the Blue Bus Transport App \nPlease select 1 if you are a bus administrator and 2 if you are a passenger"
                         "\nResponse: "))
        if user == 1:
            admin_log()
        elif user == 2:
            user_menu()
        else:
            print("Something is wrong with your input, check your entry!!!")
    except ValueError as e:
            print("\nNon-numeric data found; insert integers only")
            print(e)
    except IOError as e:
            print("\nAn error occurred trying to read the file; insert integers only")
            print(e)
    except UnicodeDecodeError as e:
            print("\nThis input is not acceptable; insert integers only")
            print(e)
    except EOFError as e:
            print("\nYou just hit an end-of-file condition; insert integers only")
            print(e)
    except KeyboardInterrupt as e:
            print("\nYou cancelled the operation; insert integers only")
            print(e)
    except ImportError as e:
            print("\nNo module found; insert integers only")
            print(e)
main_menu()


    


    


