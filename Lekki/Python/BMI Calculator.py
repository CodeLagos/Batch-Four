#Stephanie uwadiare
#stephanieuwadiare@gmail.com
#Codelagos
#Body Mass Index (BMI)

#BMI=Weight(kg)/Height**2(m**2)

#Ask user to input weight
weight=float(input("Please enter Your Weight:"))

#Ask user to input height
height=float(input("Please enter Your Height:"))

#Calculate the BMI
bmi=weight/(height*height)

#Round up the BMI to 1 decimal place 
bmi=round(bmi,1)

#Display BMI
print("Your BMI is:",bmi)

#Assign conditions
if(bmi<18.5):
    print("Underweight")
elif((bmi>=18.5) and (bmi<=24.9)):
    print("Normal")
elif((bmi>=25) and (bmi<=29.9)):
    print("Overweight")
else:
    print("Obese")
