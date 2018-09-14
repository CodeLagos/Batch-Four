#this program is for solving mathematical problem of shape
#name = jude-okoroafor-onyebuchi(okoroaforjudeonyebuchi@gmail.com
#date = 10-09-2018
#project code lagos

while True:
    #this program is to calculate the area of a rectangle
    print ("this program is to calculate the area of a rectangle")
    shape =int(input("choose the shape\n1)rectangle\n2)square\n3)triangle\n"))
    
    if(shape==1):
    
        #ask the user to enter the length
        length =int(input("enter the length of your rectangle: "))
    
        #ask the user to enter the breadth
        breadth =int(input("enter the breadth of your rectangle: "))
    
        #calculate the area of rectangle
        area=length*breadth
    
        #print the area
        print("the area of your rectangleis!",area)
    
    elif(shape==2):
    
        #ask the user to enter the length
        length= int(input("enter the length of your square: "))
    
        #ask the user to enter the breadth
        breadth= int(input("enter the breadth of your square: "))
    
        #calculate the area of your square
        area=length*breadth
    
        #print the area
        print("the area of your square!",area)

    elif(shape==3):
    
        #ask the user to enter the base
        base= int(input("enter the base of your triangle: "))

        #ask the user to enter the heigth
        heigth= int(input("enter the heigth of your triangle: "))
    
        #calculate the area of your triangle
        area=0.5*base*heigth

        #print the area
        print("the area of your triangle!",area)
    else:
        print('invalid input')  
        print()
    select=input('type "yes" to run the program again or "no"to end the program\n')
    if (select=="yes"):
             continue
    else:
        print('thanks for using this program')
        break
