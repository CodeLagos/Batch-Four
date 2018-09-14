 #Designed by Bello Oladimeji
#Email : b.oladimeji@yahoo.com
#CodeLagos 4.0


print("Welcome to the Mathematical Problem Solver\n")
while True:
    prob = input("Please select a mathematical problem to solve\n1. Number series\n2. Area of shapes\n3. Highest Common Factor(H.C.F)\n4. Lowest common multiple(L.C.M)\n5. Simple interest\n6. Factorial\n")
    if prob =="2":
        z= input("please choose between\n1. triangle\n2. rectangle\n3. parralellogram\n4. Circle\n")
        if (z == "1"):
            b=input("Enter the base of the triangle: ")
            h=input("Enter the height of the triangle:  ")
            T=int(b)*int(h)
            AT= int(T)/2
            print("The Area of the triangle is ",AT,"cm2")
    
        elif (z == "2"): 
            w=input("Enter the width of the rectangle: ")
            hi=input("Enter the height of the rectangle: ")
            R=int(w)*int(hi)
            print("The Area of the rectangle is ",R,"cm2")
        
        elif (z == "3"):
             ba=input("Enter the width of the parralellogram: ")
             hie=input("Enter the height of the parralellogram: ")
             P=int(ba)*int(hie)
             print("The Area of the paralellogram is ",P,"cm2")

        elif (z=="4"):
            r=float(input("Enter the radius of the circle: "))
            ac= round((3.14159*r*r),2)
            print("The Area of the circle is ",ac,"cm2")
        else:
            print("please choose between 1-4 as indicated above")
           
    elif prob =="1":
        z= input("please choose between \n1. Prime numbers\n2. Fibonacci series\n3. Even numbers\n4. Odd numbers\n5. Factors of a number\n")
    
        if (z=="2"):
            f=int(input("Input series range\n"))
            a,b =1,2
            while a<(f+1):
                print (a, end="")
                a,b = b , a+b
                print()
            
        elif  z=="3":
            num =int(input("Input lower range(from): \n"))
            num2 =int(input("Input higher range(to): \n"))
            print("The even numbers from",num,"to",num2,"are:")
            for n in range(num,num2+1):
                if n%2==0:
                    print(n)
                

        elif z=="4":
            num =int(input("Input lower range(from): \n"))
            num2 =int(input("Input higher range(to): \n"))
            print("The odd numbers from",num,"to",num2,"are:")
            for n in range(num,num2+1):
                if n%2!=0:
                    print(n)
                

        elif z=="1":
            num =int(input("Input lower range(from): \n"))
            num2 =int(input("Input higher range(to): \n"))
            print("The prime numbers from",num,"to",num2,"are:")
            for num in range (num,num2+1):
                if num > 1:
                    for i in range (2,num):
                        if(num%i)==0:
                           break
                    else:
                        print(num)

        elif z=="5":
            num =int(input("Input number: \n"))
            print("The factors of",num,"are:")
            for i in range (1,num+1):
                if num%i==0:
                    print(i)
                    
                    
        else:
            print("please choose between 1-5 as indicated above")

    elif prob=="3":
        num2 = int(input("Enter any lowest number: "))
        num = int(input("Enter any highest number: "))
        a=num
        b=num2
        while b!=0:
                c=a%b
                a=b
                b=c
        print ("The highest common factor is ",a)

    elif prob=="5":
        principal = float(input("Please enter the principal amount: "))
        rate = float(input("Please enter the interest rate: "))
        time = int(input("Please enter the timeframe in months: "))
        interest =(principal*rate*time)/100
        round(interest,2)
        total = principal + interest
        print("the interest after",time,"months is #",interest)
        print("The total amuont after ",time,"months is #",total)
    
    elif prob=="6":
        num =int(input("Input number: \n"))
        factorial=1
        if num<0:
            print("Sorry, factorial doesnot exist for negative numbers")
        elif num==0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num+1):
                factorial = factorial * i
            print("The factorial of",num,"is",factorial)

    elif prob =="4":
        num = int(input("Enter  highest number: "))
        num2 = int(input("Enter  lowest number: "))
        if num%num2==0:
            lcm=num
            print("The L.C.M of",num,"and",num2,"is --",lcm)
        else:
            lcm=num*num2
            print("The L.C.M of",num,"and",num2,"is --",lcm)

    else:
        print("please choose between 1-6 as indicated above")
    if str(input('\nDo you want to Solve another mathematical problem, yes or no?\n')).lower() == 'yes':
            continue
    else:
            print('Bye\nThanks for your time')
            break
    
    
    
        
                
        
        
        
    


    


    
