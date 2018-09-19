#Name: Yusuf Priscilla
#Phone:09096982258
#center: ilupeju library, anthony ,town planning
#email:pyusuf841@gmail.com
#batch:4
print("welcome to my color shape world for kids")

print("select from 1-3 to choose a shape or 4 to view an adinkrahene(An adinkrahene is a symbol which significes leadership and charisma):")
print("1.Triangle")
print("2.Square")
print("3.filled Circle")
print("4.Adinkrahene")

choice=input("enter choice(1,2,3,4,):")

if(choice=="1"):
    #import the turtle module
    import turtle
    #write the code here
    turtle.setheading(120)
    turtle.pensize(10)
    
    print("pick a color of your choice")
    print("1.blue","red")
    print("2.red","white")
    print("3.blue","yellow")
    print("4.purple","orange")
    print("5.black","red")

    choice=input("entetr choice(1,2,3,4,5):")

    if(choice=="1"):
        turtle.color("blue","red")
    
    elif(choice=="2"):
        turtle.color("red","white"
                 )
    elif(choice=="3"):              
        turtle.color("blue","yellow")
    
    elif(choice=="4"):                 
        turtle.color("purple","orange")

    elif(choice=="5"):                 
        turtle.color("black","red")
    else:
        print("invalid selection")
    turtle.begin_fill
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.end_fill
    #end the program loop
    turtle.done()
    
elif(choice=="2"):
    #import the turtle module
    import turtle
    #write the code here
    turtle.pensize(10)

    print("pick a color of your choice")
    print("1.blue","red")
    print("2.red","white")
    print("3.blue","yellow")
    print("4.purple","orange")
    print("5.black","red")

    choice=input("entetr choice(1,2,3,4,5):")

    if(choice=="1"):
        turtle.color("blue","red")
    
    elif(choice=="2"):
        turtle.color("red","white"
                 )
    elif(choice=="3"):              
        turtle.color("blue","yellow")
    
    elif(choice=="4"):                 
        turtle.color("purple","orange")

    elif(choice=="5"):                 
        turtle.color("black","red")
    else:
        print("invalid selection")

    turtle.begin_fill
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    #end the program loop
    turtle.done()

elif(choice=="3"):
    #import the turtle module
    import turtle
    #write code here
    turtle.pensize(10)

    print("pick a color of your choice")
    print("1.blue","red")
    print("2.red","white")
    print("3.blue","yellow")
    print("4.purple","orange")
    print("5.black","red")

    choice=input("entetr choice(1,2,3,4,5):")

    if(choice=="1"):
        turtle.color("blue","red")
    
    elif(choice=="2"):
        turtle.color("red","white"
                 )
    elif(choice=="3"):              
        turtle.color("blue","yellow")
    
    elif(choice=="4"):                 
        turtle.color("purple","orange")

    elif(choice=="5"):                 
        turtle.color("black","red")
    else:
        print("invalid selection")

    
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    #end the program loop
    turtle.done()

elif(choice=="4"):
    #import the turtle module
    import turtle
    #write the code here
    turtle.penup()
    turtle.setposition(-200,200)
    turtle.pendown()
    print("pick a color of your choice")
    print("1.blue","red")
    print("2.red","white")
    print("3.blue","yellow")
    print("4.purple","orange")
    print("5.black","red")

    choice=input("enter choice(1,2,3,4,5):")

    if(choice=="1"):
        turtle.color("blue","red")
    
    elif(choice=="2"):
        turtle.color("red","white"
                 )
    elif(choice=="3"):              
        turtle.color("blue","yellow")
    
    elif(choice=="4"):                 
        turtle.color("purple","orange")

    elif(choice=="5"):                 
        turtle.color("black","red")
    else:
        print("invalid selection")

    turtle.begin_fill()
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    
    
    print("pick a color for what you want the color of your circle to be:")
    print("1.blue")
    print("2.red")
    print("3.lemon")
    print("4.purple")
    print("5.black")
    print("6.white")
    print("7.orange")
    print("8.yellow")
    print("9.green")
    print("10.brown")
    
    choice=input("enter choice(1,2,3,4,5,6,7,8,9,10):")

    if(choice=="1"):
        turtle.pencolor("blue")
    
    elif(choice=="2"):
        turtle.pencolor("red")
                 
    elif(choice=="3"):              
        turtle.pencolor("lemon")
    
    elif(choice=="4"):                 
        turtle.pencolor("purple")

    elif(choice=="5"):                 
        turtle.pencolor("black")

    elif(choice=="6"):                 
        turtle.pencolor("white")

    elif(choice=="7"):                 
        turtle.pencolor("orange")

    elif(choice=="8"):                 
        turtle.pencolor("yellow")

    elif(choice=="9"):                 
        turtle.pencolor("green")

    elif(choice=="10"):                 
        turtle.pencolor("brown")
        
    else:
        print("invalid selection")
    turtle.pensize(10)
    turtle.setposition(0,-80)
    turtle.pendown()
    turtle.circle(80)
    turtle.penup()
    turtle.setposition(0,-130)
    turtle.pendown()
    turtle.circle(130)
    turtle.penup()
    turtle.setposition(0,-180)
    turtle.pendown()
    turtle.circle(180)
    turtle.hideturtle()
    #end the program loop
    turtle.done()

else:
  print("invalid selection")


    

    
