#This program is a basic physics calculator
print("Name:Akinyosoye Folasayo\n Email:fola4ril@gmail.com \n Facilitator:Mr Dotun Onasanya \n Centre:Muster point Co-working Space,Ogba")

print("Welcome to the Basic Physics calculator")

print("Instruction:Give values in S. I units")

#Lists out the formulae available

formula=str(input("What do you want to calculate \n (a)Speed \n (b)Velocity \n (c)acceleration \n (d)Force\n")) 

#Waits for user to choose an option

if (formula=="a"):
	
   distance=float(input("Enter a value for distance"))
	
   time=float(input("Enter a value for time"))
	
   print("The formula for Speed=Distance/Time and its S.I unit is metre/second")
	
   Speed=distance*time
	
   print("The speed is", str(Speed) +"m/s")
	
   print("What else would you like to calculate")

#If user option is b 

elif (formula=="b"):
	
   displacement=float(input("Enter a value for displacement"))
	
   time=float(input("Enter a value for time")) 
	
   print("The formula for velocit is Displacement/Time,and its S. I unit is metre**2/second")
	
   Velocity=displacement/time
	
   print("The velocity is", str(Velocity) +"m**2/s")
	
   print("What else would you like to calculate")

#If user option is c

elif (formula=="c"):
	
   intvel=float(input("Enter inital velocity"))
	
   finvel=float(input("Enter final velocity"))
	
   time=float(input("Enter time"))
	
   print("The formula for acceleration is Change in velocity/time")
	
   acceleration=intvel-finvel/time
	
   print("The acceleration is",str(acceleration)+"m/s")
	
   print("What else would you like to calculate")

#if user option is D

elif (formula=="d"):
	
   mass=float(input("Enter the value of mass"))
	
   accel=float(input("Enter the value of acceleration"))
	
   print("The formula for Force is mass*acceleration")
	
   Force=mass*accel
	
   print("The force is",Force,"newton")
	
print("What else would you like to calculate")

formula=str(input("What do you want to calculate \n (a)Speed \n (b)Velocity \n (c)acceleration \n (d)Force\n"))

#Waits for user to choose an options
if (formula=="a"):
	
   distance=float(input("Enter a value for distance"))
	
   time=float(input("Enter a value for time"))
	
   print("The formula for Speed=Distance/Time and its S.I unit is metre/second")
	
   Speed=distance*time
	print("The speed is", str(Speed) +"m/s")
	
print("What else would you like to calculate")

#If user option is b

elif (formula=="b"):
	
   displacement=float(input("Enter a value for displacement"))
	
   time=float(input("Enter a value for time")) 
	
   print("The formula for velocit is Displacement/Time,and its S. I unit is metre**2/second")
	
   Velocity=displacement/time
	
   print("The velocity is", str(Velocity) +"m**2/s")
	
   print("What else would you like to calculate")

#If user option is c

elif (formula=="c"):
	
   intvel=float(input("Enter inital velocity"))
	
   finvel=float(input("Enter final velocity"))
	
   time=float(input("Enter time"))
	
   print("The formula for acceleration is Change in velocity/time")
	
   acceleration=intvel-finvel/time
	
   print("The acceleration is",str(acceleration)+"m/s")
	
   print("What else would you like to calculate")

#if user option is D

elif (formula=="d"):
	
   mass=float(input("Enter the value of mass"))
	
   accel=float(input("Enter the value of acceleration"))
	
   print("The formula for Force is mass*acceleration")
	Force=mass*accel
	
   print("The force is", str(Force)+"newton")
	
print("What else would you like to calculate")

	
