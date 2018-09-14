#Taofeek Akande (seni4success@yahoo.com)

print("Welcome to Digital Medical Centre")
print("To know your Body Mass Index(BMI), follow the instruction below")
name1 = input("What is your name: ")
weight_kg1 = float(input("Weight: "))
height_m1 = float(input("Height: "))

name2 = input("What is your name: ")
weight_kg2 = float(input("Weight: "))
height_m2 = float(input("Height: "))

name3 = input("What is your name: ")
weight_kg3 = float(input("Weight: "))
height_m3 = float(input("Height: "))

def bmi_calculator(name, weight_kg, height_m):
    bmi = weight_kg / (height_m**2)
    print(name, "BMI ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, weight_kg1, height_m1)
result2 = bmi_calculator(name2, weight_kg2, height_m2)
result3 = bmi_calculator(name3, weight_kg3, height_m3)

print(result1)
print(result2)
print(result3)

