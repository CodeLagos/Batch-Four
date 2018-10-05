#Python program to convert various units to each other
#Print App name, Creator's info and Supervisor's name to user
print("App Name: Unit Converter \nCreator: Adeyemi Henry (@yugach) \nEmail: \
deyemihenry11@gmail.com \nSupervisor's name: Rex Ben")
print()

#Print a brief description of the App to user
print('This App converts the units of various parameters after you entered the \
value. \nNote: Supported parameters include: Length, Temperature and Currency')

#Some space to let user catch their breath and prompt them to CLICK ENTER...
#..to continue
print()
enter = input('Click ENTER to continue: ')


#Initiating variable called 'response' as 1
response = '1'
while response ==  '1':
#Print category to user even as the "while Loop" as been set
###Note: The ".strip()" absolves any space after user input which may lead to...
#..an error. The ".lower() converts any uppercase the user inputs to lowercase..
#..also avoiding case sensitive errors
    catSelect = input('\nSelect Category \n1. Length \n2. Temperature \n3. \
Currency \n\nResponse: ')
#Using the 'if statement' in case of invalid response and the 'while loop'...
#..allows user to reselect    
    if catSelect != '1' and catSelect != '2' and catSelect != '3':
        print('\nINVALID RESPONSE')

#If response is 1, that's Length. Proceed by inputing its units to convert...
#.. from so user can enter by typing. store it in a variable called 'unit1'     
    if catSelect == '1':
        unit1 = input('Which unit would you like to convert from \nmm, cm, m, \
km, inch, ft \n: ').strip().lower()
#A 'while' condition in case of invalid input. Program doesn't proceed until...
#..user enters the right input
        while unit1 != 'mm' and unit1 != 'cm' and unit1 != 'm' and unit1 != '\
km' and unit1  != 'inch' and unit1 != 'ft':
            unit1 = input('\nInvalid input:\nEnter either mm, cm, m, km, inch \
or ft\n: ').strip().lower()

#Prompt user to enter the unit to convert to by typing it and store it in a ...
#..variable called 'unit2'
        unit2 = input('\nWhich unit would you like to convert to \nmm, cm, m, \
km, inch, ft \n: ').strip().lower()
#A 'while' condition in case of invalid input. Program doesn't proceed until...
#..user enters the right input
        while unit2 != 'mm' and unit2 != 'cm' and unit2 != 'm' and unit2 != '\
km' and unit2 != 'inch' and unit2 != 'ft':
            unit2 = input('\nInvalid input:\nEnter either mm, cm, m, km, inch \
or ft\n: ').strip().lower()

#Prompt user to enter value and store it in a variable called 'num1' meanwhile..
#..error and exception is also set in case of invalid input
        while True:
            try:
                num1 = float(input('\nEnter value\n: '))
                break
            except ValueError:
                print('\nPls, enter a number')
                    
                
    
##Calculations for the different units under the Length parameter
#Print result to user in 2decimal places

#Cal from cm to m
        if unit1 == 'cm' and unit2 == 'm':
            ans = float(num1)/100
            print(num1, 'cm is ', round(ans, 2), 'm', sep='')
#Cal from mm to cm            
        elif unit1 == 'mm' and unit2 == 'cm':
            ans = float(num1)/10
            print(num1, 'mm is ', round(ans, 2), 'cm', sep='')
#Cal from m to cm
        elif unit1 == 'm' and unit2 == 'cm':
            ans = float(num1)*100
            print(num1, 'm is ', round(ans, 2), 'cm', sep='')
#Cal from cm to mm
        elif unit1 == 'cm' and unit2 == 'mm':
            ans = float(num1)*10
            print(num1, 'cm is ', round(ans, 2), 'mm', sep='')
#Cal from mm to m
        elif unit1 == 'mm' and unit2 == 'm':
            ans = float(num1)/1000
            print(num1, 'mm is ', round(ans, 2), 'm', sep='')
#Cal from m to mm
        elif unit1 == 'm' and unit2 == 'mm':
            ans = float(num1)*1000
            print(num1, 'm is ', round(ans, 2), 'mm', sep='')
#Cal from km to m
        elif unit1 == 'km' and unit2 == 'm':
            ans = float(num1)*1000
            print(num1, 'km is ', round(ans, 2), 'm', sep='')
#Cal from m to km
        elif unit1 == 'm' and unit2 == 'km':
            ans = float(num1)/1000
            print(num1, 'm is ', round(ans, 2), 'km', sep='')
#Cal from mm to km
        elif unit1 == 'mm' and unit2 == 'km':
            ans = float(num1)/1000000
            print(num1, 'mm is ', round(ans, 2), 'km', sep='')
#Cal from mm to inch
        elif unit1 == 'mm' and unit2 == 'inch':
            ans = float(num1)/25.4
            print(num1, 'mm is ', round(ans, 2), 'inch', sep='')
#Cal from inch to mm
        elif unit1 == 'inch' and unit2 == 'mm':
            ans = float(num1)*25.4
            print(num1, 'inch is ', round(ans, 2), 'mm', sep='')
#Cal from mm to ft
        elif unit1 == 'mm' and unit2 == 'ft':
            ans = float(num1)/304.8
            print(num1, 'mm is ', round(ans, 2), 'ft', sep='')
#Cal from ft to mm
        elif unit1 == 'ft' and unit2 == 'mm':
            ans = float(num1)*304.8
            print(num1, 'ft is ', round(ans, 2), 'mm', sep='')
#Cal from cm to km
        elif unit1 == 'cm' and unit2 == 'km':
            ans = float(num1)/100000
            print(num1, 'cm is ', ans, 'km', sep='')
#Cal from km to cm
        elif unit1 == 'km' and unit2 == 'cm':
            ans = float(num1)*100000
            print(num1, 'km is ', ans, 'cm', sep='')
#Cal from cm to inch
        elif unit1 == 'cm' and unit2 == 'inch':
            ans = float(num1)/2.54
            print(num1, 'cm is ', round(ans, 2), 'inch', sep='')
#Cal from inch to cm
        elif unit1 == 'inch' and unit2 == 'cm':
            ans = float(num1)*2.54
            print(num1, 'inch is ', round(ans, 2), 'cm', sep='')
#Cal from cm to ft
        elif unit1 == 'cm' and unit2 == 'ft':
            ans = float(num1)/30.48
            print(num1, 'cm is ', round(ans, 2), 'ft', sep='')
#Cal from ft to cm
        elif unit1 == 'ft' and unit2 == 'cm':
            ans = float(num1)*30.48
            print(num1, 'ft is ', round(ans, 2), 'cm', sep='')
#Cal from m to inch
        elif unit1 == 'm' and unit2 == 'inch':
            ans = float(num1)*39.37
            print(num1, 'm is ', round(ans, 2), 'inch', sep='')
#Cal from inch to m
        elif unit1 == 'inch' and unit2 == 'm':
            ans = float(num1)/39.37
            print(num1, 'inch is ', round(ans, 2), 'm', sep='')
#Cal from m to ft
        elif unit1 == 'm' and unit2 == 'ft':
            ans = float(num1)*3.28
            print(num1, 'm is ', round(ans, 2), 'ft', sep='')
#Cal from ft to m
        elif unit1 == 'ft' and unit2 == 'm':
            ans = float(num1)/3.28
            print(num1, 'ft is ', round(ans, 2), 'm', sep='')
#Cal from km to mm
        elif unit1 == 'km' and unit2 == 'mm':
            ans = float(num1)*1000000
            print(num1, 'km is ', ans, 'mm', sep='')
#Cal from km to inch
        elif unit1 == 'km' and unit2 == 'inch':
            ans = float(num1)*39370.0787
            print(num1, 'km is ', round(ans, 2), 'inch', sep='')
#Cal from inch to km
        elif unit1 == 'inch' and unit2 == 'km':
            ans = float(num1)/39370.0787
            print(num1, 'inch is ', round(ans, 2), 'km', sep='')
#Cal from km to ft
        elif unit1 == 'km' and unit2 == 'ft':
            ans = float(num1)*3280.8399
            print(num1, 'km is ', round(ans, 2), 'ft', sep='')
#Cal from ft to km
        elif unit1 == 'ft' and unit2 == 'km':
            ans = float(num1)/3280.8399
            print(num1, 'ft is ', round(ans, 2), 'km', sep='')
#Cal from inch to ft
        elif unit1 == 'inch' and unit2 == 'ft':
            ans = float(num1)/12
            print(num1, 'inch is ', round(ans, 2), 'ft', sep='')
#Cal from ft to inch
        elif unit1 == 'ft' and unit2 == 'inch':
            ans = float(num1)*12
            print(num1, 'ft is ', ans, 'inch', sep='')
#Cal from mm to mm
        elif unit1 == 'mm' and unit2 == 'mm':
            ans = float(num1)*1
            print(num1, 'mm is ', ans, 'mm', sep='')
#Cal from cm to cm
        elif unit1 == 'cm' and unit2 == 'cm':
            ans = float(num1)*1
            print(num1, 'cm is ', ans, 'cm', sep='')
#Cal from m to m
        elif unit1 == 'm' and unit2 == 'm':
            ans = float(num1)*1
            print(num1, 'm is ', ans, 'm', sep='')
#Cal from km to km
        elif unit1 == 'km' and unit2 == 'km':
            ans = float(num1)*1
            print(num1, 'km is ', ans, 'km', sep='')
#Cal from inch to inch
        elif unit1 == 'inch' and unit2 == 'inch':
            ans = float(num1)*1
            print(num1, 'inch is ', ans, 'inch', sep='')
#Cal from ft to ft
        elif unit1 == 'ft' and unit2 == 'ft':
            ans = float(num1)*1
            print(num1, 'ft is ', ans, 'ft', sep='')
                
#A little space to catch my breath.
        print()
    


#If response is 2, that's Temperature. Input its units so user can select by...
#..typing it and pressing enter. store it in a variable called unit1
    elif catSelect == '2':
#Prompt user to select from units to convert from
        unit1 = input('Which unit would you like to convert from \nF, C, K \n:\
').strip().lower()
#A 'while' condition in case of invalid input. Program doesn't proceed until...
#..user enters the right input
        while unit1 != 'f' and unit1 != 'c' and unit1 != 'k':
            unit1 = input('Inavid input:\n\nEnter either f, c, or k\nEnsure \
Caps Lock is off\nWhich unit would you like to convert from \nF, C, K\n: ').strip().lower()

#Prompt user to enter the unit to convert to by typing  and store in a ....
#..variable called 'unit2
        unit2 = input('Which unit would you like to convert to \nF, C, K \n: ').strip().lower()
        while unit2 != 'f' and unit2 != 'c' and unit2 != 'k':
            unit2 = input('Inavid input:\n\nEnter either f, c, or k\nEnsure \
Caps Lock is off\nWhich unit would you like to convert to \nF, C, K\n: ').strip().lower()

#Prompt user to enter value and store it in a variable called 'num1' meanwhile..
#..error and exception is also set in case of invalid input
        while True:
            try:
                num1 = float(input('\nEnter degrees of temperature\n: '))
                break
            except ValueError:
                print('\nPls, enter a number')
        
        
##Calculations for the different units under the Temperature parameter
#Print result to user

#Cal for Fahrenheit to Celsius
        if unit1.lower() == 'f' and unit2.lower() == 'c':
            ans = float(num1 - 32)*(5/9)
            print(num1, 'F is ', round(ans, 2), 'C', sep='')
#Cal for Celsius to Fahrenheit
        elif unit1.lower() == 'c' and unit2.lower() == 'f':
            ans = float(num1 * 9/5) + 32
            print(num1, 'C is ', round(ans, 2), 'F', sep='')
#Cal for Fahrenheit to Kelvin
        elif unit1.lower() == 'f' and unit2.lower() == 'k':
            ans = float(num1 + 459.67) * 5/9
            print(num1, 'F is ', round(ans, 2), 'K', sep='')
#Cal for Fahrenheit to Fahrenheit
        elif unit1.lower() == 'f' and unit2.lower() == 'f':
            ans = float(num1)*1
            print(num1, 'F is ', round(ans, 2), 'F', sep='')
#Cal for Celsius to Kelvin
        elif unit1.lower() == 'c' and unit2.lower() == 'k':
            ans = float(num1 + 273.15)
            print(num1, 'C is ', round(ans, 2), 'K', sep='')
#Cal for Kelvin to Celsius
        elif unit1.lower() == 'k' and unit2.lower() == 'c':
            ans = float(num1 - 273.15)
            print(num1, 'K is ', round(ans, 2), 'C', sep='')
#Cal for Celsius to Celsius
        elif unit1.lower() == 'c' and unit2.lower() == 'c':
            ans = float(num1)*1
            print(num1, 'C is ', round(ans, 2), 'C', sep='')
#Cal for Kelvin to Fahrenheit
        elif unit1.lower() == 'k' and unit2.lower() == 'f':
            ans = float(num1 * 9/5) - 459.67
            print(num1, 'K is ', round(ans, 2), 'F', sep='')
#Cal for Kelvin to Kelvin
        elif unit1.lower() == 'k' and unit2.lower() == 'k':
            ans = float(num1)*1
            print(num1, 'K is ', round(ans, 2), 'K', sep='')

#A space to catch my breath. Print anwser to user rounding up to 2decimal places
        print()



#If response is 3, that's Currency.
    elif catSelect == '3':
#A "def function" to collect amount value input from user
        def amount(userAmount):

#Prompt user to select which currency they want to convert from
            currencyFromSelect = int(input('\nSelect currency to convert from \
\n1. Naira \n2. Dollars \n3. Pounds \n4. Yen \nresponse: '))
            while currencyFromSelect != 1 and currencyFromSelect != 2 and currencyFromSelect != 3 and currencyFromSelect != 4:
                currencyFromSelect = int(input('Invalid selection: \
\nEnter 1 for Naira \nEnter 2 for Dollars \nEnter 3 for  Pounds \nEnter 4 for \
Yen \nresponse: '))
                
            if currencyFromSelect == 1:
#Prompt user to select currency they want to convert to
                currencyToSelect = int(input('\nSelect currency to convert to \
\n1. Naira \n2. Dollars \n3. Pounds \n4. Yen \nresponse: '))
                            
#If currencyFromSelect is 1, that's Naira
#Calculations from "Naira" to other currencies
                if currencyToSelect == 1:
                    print(amountValue, 'naira is ', amountValue*1, 'Naira', sep='')
                elif currencyToSelect == 2:
                    print(amountValue, 'naira is ', round((amountValue/359), 2), 'Dollars', sep='')
                elif currencyToSelect == 3:
                    print(amountValue, 'naira is ', round((amountValue/467.27), 2), 'Pounds', sep='')
                elif currencyToSelect == 4:
                    print(amountValue, 'naira is ', round((amountValue/3.25), 2), 'Yen', sep='')
                else:
                    print('Invalid entry')

#If currencyFromSelect is 2, that's Dollars
            elif currencyFromSelect == 2:
#Prompt user to select which currency they want to convert to
                currencyToSelect = int(input('\nSelect currency to convert to \
\n1. Naira \n2. Dollars \n3. Pounds \n4. Yen \nresponse: '))
#Calculations from "Dollar" to other currencies
                if currencyToSelect == 1:
                    print(amountValue, 'dollar is ', amountValue*359, 'Naira', sep='')
                elif currencyToSelect == 2:
                    print(amountValue, 'dollar is ', amountValue*1, 'Dollars', sep='')
                elif currencyToSelect == 3:
                    print(amountValue, 'dollar is ', round((amountValue/1.30), 2), 'Pounds', sep='')
                elif currencyToSelect == 4:
                    print(amountValue, 'dollar is ', round((amountValue*110.84), 2), 'Yen', sep='')
                else:
                    print('Invalid entry')


#If currencyFromSelect is 3, that's Pounds
            elif currencyFromSelect == 3:
#Prompt user to select which currency they want to convert to
                currencyToSelect = int(input('\nSelect currency to convert to \
\n1. Naira \n2. Dollars \n3. Pounds \n4. Yen \nresponse: '))
#Calculations from "Pounds" to other currencies
                if currencyToSelect == 1:
                    print(amountValue, 'pounds is ', round((amountValue*467.27), 2), 'Naira', sep='')
                elif currencyToSelect == 2:
                    print(amountValue, 'pounds is ', round((amountValue*1.30), 2), 'Dollars', sep='')
                elif currencyToSelect == 3:
                    print(amountValue, 'pounds is ', round((amountValue*1), 2), 'Pounds', sep='')
                elif currencyToSelect == 4:
                    print(amountValue, 'pounds is ', round((amountValue*143.95), 2), 'Yen', sep='')
                else:
                    print('Invalid entry')


#If currencyFromSelect is 4, that's Yen
            elif currencyFromSelect == 4:
#Prompt user to select which currency they want to convert to
                currencyToSelect = int(input('\nSelect currency to convert to \
\n1. Naira \n2. Dollars \n3. Pounds \n4. Yen \nresponse: '))
#Calculations from "Yen" to other currencies
                if currencyToSelect == 1:
                    print(amountValue, 'yen is ', round((amountValue*3.25), 2), 'Naira', sep='')
                elif currencyToSelect == 2:
                    print(amountValue, 'yen is ', round((amountValue/110.84), 2), 'Dollars', sep='')
                elif currencyToSelect == 3:
                    print(amountValue, 'yen is ', round((amountValue/143.95), 2), 'Pounds', sep='')
                elif currencyToSelect == 4:
                    print(amountValue, 'yen is ', round((amountValue*1), 2), 'Yen', sep='')
                else:
                    print('Invalid entry')



#Error and exception in case of invalid input for amount value from user
#Code from 'def function' to amount from user and store in a variable called..
#.."amountValue"
        while True:
            try:
                amountValue = float(input('\nEnter amount to be converted: '))
                amount(amountValue)
                break
            except ValueError:
                print('\nInvalid input: Pls enter a number')
        



#In case of an invalid response, prompt user to enter 1 if they wish to ....
#..contiue with the program, or enter any other key to end it
    response=input('\n\nEnter 1 to continue, else enter any other \
character to terminate the program\n: ')

#Farewell if response is not 1
    if response != '1':
        print('\nGood Bye \n\nSpecial thanks to boss Rex Ben. \nMany thanks to \
all the other participants. \nCode Lagos you ROCK!!!!\nThank you o \nSigned by \
Yugach')
