#CodeLagos Lekki Centre, Python Class.
#Created by: NUHU JOHN. E-mail: nuhujohn97@gmail.com

#Display the Welcome Message
print("Welcome to the CGPA Calculator!\nCreated by Nuhu John!")

#Display the Instruction
print("This is a Program to calculate the CGPA of 5 Courses in 2 Semesters")

#Ask user to enter Grade Points of 5 courses in 1st semester
GP1=int(input("Please enter Grade Point:"))
GP2=int(input("Please enter Grade Poont:"))
GP3=int(input("Please enter Grade Point:"))
GP4=int(input("Please enter Gradr Point:"))
GP5=int(input("Please enter Grade Point:"))

#Calculate Total Grade Points
TGP1=GP1 + GP2 + GP3 + GP4 + GP5

#Prompt user to Input Credit Units
print("Please Input Credit Unit")

#Ask user to enter Credit Units of 5 courses in 1st semester
CU1=int(input("Please enter Credit Unit:"))
CU2=int(input("Please enter Credit Unit:"))
CU3=int(input("Please enter Credit Unit:"))
CU4=int(input("Please enter Credit Unit:"))
CU5=int(input("Please enter Credit Unit:"))

#Calculate Total Credit Unit
TCU1=CU1 + CU2 + CU3 + CU4 + CU5

print("Your Total Credit Unit is:",TCU1)

#Calculate GPA of 1st semester
GPA1=(GP1*CU1) + (GP2*CU2) + (GP3*CU3) + (GP4*CU4) + (GP5*CU5)

print("Your Total Grade Point is:",GPA1)

#Calculate Total Grade Point Average
TGPA1=GPA1/TCU1

#Roundup GPA to 1 decimal place
TGPA1=round(TGPA1,1)

#Display First Semester Grade Point Average
print("Your 1st Semester GPA is:",TGPA1)

#Prompt the user to continue to 2nd semester
print("Please enter Grade Points & Credit Units of 2nd Semester")

#Ask user to enter Grade Point of 5 course in 2nd semester
GP6=int(input("Please enter Grade Point:"))
GP7=int(input("Please enter Grade Point:"))
GP8=int(input("Please enter Grade Point:"))
GP9=int(input("Please enter Grade Point:"))
GP10=int(input("Please enter Grade Point:"))

#Calculater the Total Grade Points of 2nd Semester
TGP2=GP6 + GP7 + GP8 + GP9 + GP10

#Prompt user to input Credit Units
print("Please Input Credit Units")

#Ask user to enter Credit Units of 5 courses in 2nd semester
CU6=int(input("Please enter Credit Unit:"))
CU7=int(input("Please enter Credit Unit:"))
CU8=int(input("Please enter Credit Unit:"))
CU9=int(input("Please enter Credit Unit:"))
CU10=int(input("Pleade enter Credit Unit:"))

#Calculate the Total Credit Units
TCU2=CU6 + CU7 + CU8 + CU9 + CU10

print("Your Total Credit Unit is:",TCU2)

#Calculate 2nd semester GPA
GPA2=(GP6*CU6) + (GP7*CU7) + (GP8*CU8) + (GP9*CU9) + (GP10*CU10)

print("Your Total Grade Point is:",GPA2)

#Calculate the Total Grade Point Average of 2nd semester.
TGPA2=GPA2/TCU2

TGPA2=round(TGPA2,1)

#Display Second Semester Grade Point Average
print("Your 2nd Semester GPA is:",TGPA2)

#Calculate Cumulative Grade Point Avetage.
CGPA=(TGPA1+TGPA2)/2

#Round up to 1 decimal place
CGPA=round(CGPA,1)

#Diplay the Cumulative Grade Point Average
print("Your CGPA is:",CGPA)

#Assign Class of Degree
if((CGPA>=4.50) and (CGPA<=5.00)):
    print("You have;","FIRST CLASS")
elif((CGPA>=3.50) and (CGPA<=4.49)):
    print("You have;","SECOND CLASS UPPER")
elif((CGPA>=2.50) and (CGPA<=3.49)):
    print("You have;","SECOND CLASS LOWER")
elif((CGPA>=2.50) and (CGPA<=3.49)):
    print("You have;","THIRD CLASS")
elif((CGPA>=1.00) and (CGPA<=1.49)):
    print("You have;","PASS")
elif((CGPA>=0.00) and (CGPA<=0.99)):
    print("You have;","FAIL")
else:
    print("Grade Unknow")
