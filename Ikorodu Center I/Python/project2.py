""" PROJECT
"""
# Python program to find the multiplication table ( from 1 to 12) of a number.

# Take input from the user
num=int(input("Display multiplication table of:"))

#Use for loop to iterate 10 times
for i in range(1,13):
    print (num, "*",i,"=",num*i)
