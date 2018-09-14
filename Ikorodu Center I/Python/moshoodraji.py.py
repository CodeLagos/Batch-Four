import time
# project BY = MOSHOOD RAJI(moshoodr53@gmail.com)
# facilitator = Mr idris
print("This program helps companies ascertain monthly pay of there employee")
total = 0
name = input ("Enter name: \n")
dd=int(input("Enter working days \n"))
for v in range(dd):
    pay =float(1000)
    bonus =float(300)
    half_b=float(150)
    half_day =float(500)
    prod_max = 500
    prod_min = 300
    prod = int(input ("Enter production unit: \n"))
    if (prod) < (prod_min):
        pay = half_day 
        print("initial pay is," + str(pay))
    elif (prod) == (prod_min):
        pay = pay + bonus
        print("initial pay is," + str(pay))
    elif (prod) == (prod_max):
        pay = pay + bonus + bonus
        print("initial pay is," + str(pay))
    elif(prod) > (prod_max):
        pay = pay + bonus + bonus + bonus
        print("initial pay is," + str(pay))
    elif (prod) < (prod_max) != (prod_min):
        pay = pay + bonus + half_b
        print("initial pay is," + str(pay))
    else:
        print("All entries are wrong!!")
    total = pay + total 
    print("overall",total)
print((name) + " pay for the month is," + str(total))
