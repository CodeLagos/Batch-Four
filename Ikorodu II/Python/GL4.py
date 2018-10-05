
#Algorithm for BANDERA LOTTO

#Display Lotto name and print Menu list.

#Import a random module

#Use a while loop.

#Enter 5 different integer numbers.

#Call a variable "x" and collect the numbers of possible winning numbers.

#Impute a variable "j" in range of the integer number "n"

#Append value of x.

#print winning numbers.

#Give value to respective winning numbers.

print(30 * "-", "BANDERA LOTTERY MENU")
print("1. [Play Pick - 5 NUMBERS\n2. #1,000,000 FOR FIRST NO WIN ONLY\n3. #800,000 FOR 2ND NO WIN ONLY\n4. #500,000 FOR 3RD NO WIN ONLY\n5. #200,000 FOR 4TH NO WIN ONLY\n6. #100,000 FOR 5TH NO WIN ONLY\n7. SELECT BETWEEN 1 & 99\n8. MINIMUM STAKE IS #5,000\nWISING YOU BEST LUCK!!!]")
print(75 * "-")

import random

while True:

    a = int(input("Enter 1st number = "))
    b = int(input("Enter 2nd number = "))
    c = int(input("Enter 3rd number = "))
    d = int(input("Enter 4th number = "))
    e = int(input("Enter 5th number = "))

    x = []
    n = int(input("Enter number '5' for 5 possible winning numbers = "))

    print()

    for j in range(n):
        x.append(random.randint(1, 99))
    print("Winning numbers are", x)

    print()
    if a in x: print("#1,000,000 - Win value of 1st number = ", a)
    if b in x: print("#800,000 - Win value of 2nd number = ", b)
    if c in x: print("#500,000 - Win value of 3rd number = ", c)
    if d in x: print("#200,000 - Win value of 4th number = ", c)
    if e in x: print("#100,000 - Win value of 5th number = ", c)
    

    else:
        print("No winning number")
    
        
        
            
            
    
 






















       
