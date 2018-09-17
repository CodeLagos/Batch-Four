#Name: Oluwakemi Agboola
#Email: kemi_tosin@yahoo.com
#Phone number: 07087346204
#Class: Python_Batch 4 Morning
#Centre: Ilupeju

print("Hello user, Welcome to Student GP Calculator")
name=input("Please enter your name: ")
u1=int(input("Enter the number of units for ACC 110: "))
u2=int(input("Enter the number of units for ACC 111: "))
u3=int(input("Enter the number of units for ACC 112: "))
units=u1+u2+u3
print("Your total units for this semester is",units)
g1=int(input("Enter the grade for ACC 110 (0 to 5): "))
g2=int(input("Enter the grade for ACC 111 (0 to 5): "))
g3=int(input("Enter the grade for ACC 112 (0 to 5): "))
print("Hello",name+", Your Grade Point Average for this semester is ",round((((u1*g1)+(u2*g2)+(u3*g3))/units),2),"out of 5.0")
