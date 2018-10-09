#Name: Nkeonye I. Benedict
#Email: benedictiknkeonye@gmail.com
#Class Facilitator: Mr. Dotun Onasanya
#Project Objective: This program is to find the measures of central tendencies for a set of numbers in a statistics-related problem. All you have to do is enter the list of numbers you want to work on
#Project Name: The Simple Statistics Calculator



def main():

    name = input('Please enter your name: ').title()

    print('Hello ', name,  '\nWelcome To The Simple Statistics Calculator')
    

    instruction = 'Please follow the prompts correctly'
    print(instruction.title())

    side_note = "This program will make mean, median, mode, standard deviation and variance very easy!"
    print(side_note)


    #Collection Of Numbers
    #This section creates an empty list to store the numbers in
    data = [] 
    print("\nFirst, we need to enter some numbers!")

    num=input("\nType your first number: ")

    #This while loop is continuously enabling the collection of more numbers
    while num:
        data.append(float(num)) #Converts num into a float so we can do division
        print("\n",data)
        num = input("Add another number, or press enter to move on: ")
    #End of data collection


    #Sort the data collected
    data.sort()
    print("\nHere's the list in numerical order:\n", data)


    #The Arithmetic Mean
    total = sum(data)
    length = len(data)
    mean = total/length
    mean = round(mean, 3)
    print("\nThe Arithmetic Mean Is: ", mean)


    #The Median
    oddness = length%2
    half = length//2
    if oddness == 1:
        print("\nThe Median is:",data[half])
    else:
        low = float(data[half-1])
        high = float(data[half])
        print("The Median is half way between", low, "and", high)
        print("That makes it:",low+(high-low)/2)


        
    #The mode
        
    #Still using the same list
    apps = []

    #A for loop to run through all our collected numbers
    for item in data:

    #The tally variable helps us to 'count' the numbers     
        tally = data.count(item)  

    #The data entered into a tuple cannot be changed; Tuples are immutable arrays    
    #The values variable below makes a tuple that is the number of hits paired with the described number
        values = (tally, item)
        
    #Only add one entry for each number in the set
        if values not in apps:
            apps.append(values)

    #This reverses the data sorted earlier        
    apps.sort(reverse=True)
    if apps[0][0]>apps[1][0]:
        print("\n The Mode is: ", apps[0][1], "as the number recorded", apps[0][0], "apps.")
    else:
        print("These set of data has no mode")


    #The Standard Deviation and Variance

    #Importing The Statistics Module
    import statistics

    #Implementing the Standard Deviation method
    SD = statistics.stdev(data)
    SD = round(SD, 3)
    print('\nThe Standard Deviation of the data is ', SD)

    #Implementing the Standard Deviation method
    Var = statistics.variance(data)
    Var = round(Var, 3)
    print('\nThe Variance of the data is ', Var)


    print('\n\n Thank you for using my Mini Statistics Program')


    restart = input('\nWould you like to solve another set of data? \n yes or no: ').lower()
    if restart == 'yes':
        main()
    else:
        exit()






main()
    
    
