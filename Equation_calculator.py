print ("Name: KUSIMO, Mojeed Akintunde")
print ("Email: mkusimo90@gmail.com")
print ("Phone: 07088116539")
print ("Class: Python")
print ("Function: This program is for solving equations")

#program asks for users name
user = input ("\nHi there! May I know you please: ")
print ("Welcome",user)
while True:
    import math
    #program asks user for the equation to solve
    task1 = input ("\nWhat type of equation would you like to solve?\n 1. Linear Equation\n 2. Quadratic Equation\n 3. Cubic Equation\n Choice: ")

    if task1 == "1":
        #program asks user the type of linear equation to solve 
        task2 = input ("What type of linear equation?\n 1. a1x + b1y = c1\n    a2x + b2y = c2\n 2. a1x + b1y + c1z = d1\n    a2x + b2y + c2z = d2\n    a3x + b3y + c3z = d3\n Choice: ")
        if task2 == "1":
            #program requesting for values to solve simultaneous 2 equations
            print ("Please enter the value of the following:\n")
            a1 = float (input ("a1 = "))
            b1 = float (input ("b1 = "))
            c1 = float (input ("c1 = "))
            a2 = float (input ("a2 = "))
            b2 = float (input ("b2 = "))
            c2 = float (input ("c2 = "))
            #solving simultaneous equation
            a1a2 = a1 * a2
            b1a2 = b1 * a2
            a2a1 = a2 * a1
            b2a1 = b2 * a1
            c1a2 = c1 * a2
            c2a1 = c2 * a1

            if a1a2 and a2a1 < 0 or a1a2 and a2a1 > 0:
                d1 = a1a2 - a2a1
                d2 = b1a2 - b2a1
                d3 = c1a2 - c2a1
                y = d3/d2
                x = (c2a1 - (b2a1*y))/a2a1

                print ("x = ", round (x,2)," and y = ",round (y,2))
                
            else:
                d1 = a1a2 + a2a1
                d2 = b1a2 + b2a1
                d3 = c1a2 + c2a1
                y = d3/d2
                x = (c2a1 - (b2a1*y))/a2a1

                print ("x = ", round (x,2)," and y = ",round (y,2))

        #program requesting for values to solve simultaneous 3 equations
        elif task2 == "2":
            print ("Please enter the value of the following:\n")
            a1 = float (input ("a1 = "))
            b1 = float (input ("b1 = "))
            c1 = float (input ("c1 = "))
            d1 = float (input ("d1 = "))
            a2 = float (input ("a2 = "))
            b2 = float (input ("b2 = "))
            c2 = float (input ("c2 = "))
            d2 = float (input ("d2 = "))
            a3 = float (input ("a3 = "))
            b3 = float (input ("b3 = "))
            c3 = float (input ("c3 = "))
            d3 = float (input ("d3 = "))

            #solving simultaneous equation using matrix 
            e = a1 * ((b2*c3) - (b3*c2)) - b1 * ((a2*c3) - (a3*c2)) + c1 * ((a2*b3) - (a3*b2))
            ex = d1 * ((b2*c3) - (b3*c2)) - b1 * ((d2*c3) - (d3*c2)) + c1 * ((d2*b3) - (d3*b2))
            ey = a1 * ((d2*c3) - (d3*c2)) - d1 * ((a2*c3) - (a3*c2)) + c1 * ((a2*d3) - (a3*d2))
            ez = a1 * ((b2*d3) - (b3*d2)) - b1 * ((a2*d3) - (a3*d2)) + d1 * ((a2*b3) - (a3*b2))

            x = ex/e
            y = ey/e
            z = ez/e

            print ("x = ", round (x,2),", y = ",round (y,2), " and z = ", round (z,2))
            
        else:
            print ("What you entered is not available in the options")

    #program requesting for values to solve quadratic equation
    elif task1 == "2":
        print ("Please fill the following using this format:\n ax2 + bx + c = 0\n")
        a = float (input ("a = "))
        b = float (input ("b = "))
        c = float (input ("c = "))

        #for imaginary roots
        if b**2 < 4 * a * c:
            d = math.sqrt (-(b**2-(4 * a * c)))
            e = -b/(2*a)
            f = d/(2*a)
            print ("The roots are", round (e,2), "+", round (f,2),"i and ", round (e,2), "-", round (f,2),"i")

        #for real roots    
        else:
            x1 = (-b + math.sqrt (b**2 - (4 * a * c)))/(2*a)
            x2 = (-b - math.sqrt (b**2 - (4 * a * c)))/(2*a)
            print ("The roots are", round (x1,2), " and ", round (x2,2))

    #program requesting for values to solve cubic equation using discriminants
    elif task1 == "3":
        print ("Please fill the following using this format:\n ax3 + bx2 + cx + d = 0\n")
        a = float (input ("a = "))
        b = float (input ("b = "))
        c = float (input ("c = "))
        d = float (input ("d = "))

        f = ((3*(c/a)) - (b**2/a**2))/3
        g = ((2*(b**3/a**3)) - ((9*b*c)/a**2) + ((27*d)/a))/27
        h = ((g**2)/4) + ((f**3)/27)
        #for 3 different real numbers
        if h < 0:
            i = math.sqrt (((g**2)/4) - h)
            j = i**(1/3)
            k = math.acos (-(g/(2*i)))
            l = j * -1
            m = math.cos (k/3)
            n = (math.sqrt(3)) * (math.sin(k/3))
            p = (b/(3*a)) * -1

            x1 = (2*j*m) - (b/(3*a))
            x2 = (l * (m+n)) + p
            x3 = (l * (m-n)) + p
         
            print ("The roots are: ",round (x1,2),",",round (x2,2)," and ",round (x3,2))

        #for 1 or 2 real roots
        elif h > 0:
            r = -(g/2) + (math.sqrt(h))
            s = r**(1/3)
            t = +(g/2) + (math.sqrt(h))
            u = -t**(1/3)

            x1 = (s+u) - (b/(3*a))
            x20 = -(s+u)/2 - (b/(3*a))
            x21 = ((s-u) * 3**(1/2))/2
            x30 = -(s+u)/2 - (b/(3*a))
            x31 = ((s-u) * 3**(1/2))/2

            print ("The roots are: ",round (x1,2),",",round (x20,2),"+" ,round (x21,2),"i and ",round (x30,2),"-" ,round (x31,2),"i")

        # for 3 equal and real roots
        else: 
            x1 = ((d/a)**(1/3)) * -1
            x2 = ((d/a)**(1/3)) * -1
            x3 = ((d/a)**(1/3)) * -1

            print ("The roots are: ",round (x1,2),",",round (x2,2)," and ",round (x3,2))

    else:
        print ("What you entered is not available in the options")
        
    close = input ("\nWould you like to exit?\n 1.Yes\t 2. No\n Choice:")
    if close == "2":
        continue
    
    elif close == "1":
        print ("Have a nice day,",user)
        break
    
    else:
        print ("What you entered is not available in the options")
                
        
