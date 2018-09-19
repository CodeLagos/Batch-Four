#trying to make something that helps with saving money
#Wilson Arimah
amount=float(input("what is the amount of money you wish to save? "))
income=float(input("what is your monthly income? "))
time=float(input("how long do you want to save (for in month)? "))

#this is the total amount of money saved if you do not spend any
x=income*time
#this is how much you would need to save monthly
y=amount/time
'''

print(x,y,z,w)
'''

if x>=amount:
    print("you can save that amount of money, you just need to save %f each month. " %y)


else:
    print("Sorry the amount of money you wish to save is not possible. ")
























