Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from turtle import*
>>> screen = Screen()
>>> screen.setup(400,400)
>>> screen.bgcolor('#A7E30E')
>>> color('#FA057F')
>>> # This is CodeLagos python programming Course for  2018 Batch 4.
>>> #This is a python project program on how to calculate age in seconds
>>> #Ask user his age
>>> print("Enter your age:")
Enter your age:
>>> 55
55
>>> user_age = input("Enter your age:")
Enter your age:55
>>> user_age
'55'
>>> int(user_age)
55
>>> int(user_age)*365*24*60*60
1734480000
>>> seconds = int(user_age)*365*24*60*60
>>> seconds
1734480000
>>> print("you have lived for{} seconds.".format(seconds))
you have lived for1734480000 seconds.
