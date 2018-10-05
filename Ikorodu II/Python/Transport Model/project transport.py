#collect input from the users
#inputs = destinations of users
#check if the users is going to a particular place
#print the price and the distance of the destination
import sys
def transportation():
 print("list of available routes \nIkorodu \nVictoria Island \nOshodi \nBerger  \nIkeja  ")
 current_location = input("your current location")
 destination = input("your destination")
 if current_location.lower() == 'ikorodu' and destination.lower() == "ikeja":
    print("your transportation cost form ikorodu to ikeja is N5000")

 elif current_location.lower() == "ikorodu" and destination.lower() == "victoria island":
     print("your transportation cost form ikorodu to victoria island is N5000 ")

 elif current_location.lower() == "ikorodu" and destination.lower() == "oshodi":
     print("your transportation cost form ikorodu to Oshodi is N7000 ")

 elif current_location.lower() == "ikorodu" and destination.lower() == "berger":
     print("your transportation cost form ikorodu to oshodi is N4000 ")

 elif current_location.lower() == "victoria island" and destination.lower() == "oshodi":
     print("your transportation cost form victoria island to oshodi is N10000 ")

 elif current_location.lower() == "victoria island" and destination.lower() == "berger":
     print("your transportation cost form victoria island to berger is N8000 ")

 elif current_location.lower() == "victoria island" and destination.lower() == "ikorodu":
     print("your transportation cost form victoria island to ikorodu is N8500 ")

 elif current_location.lower() == "victoria island " and destination.lower() == "ikeja":
     print("your transportation cost form victoria island to ikeja is N5000 ")

 elif current_location.lower() == "berger" and destination.lower() == "victoria island":
     print("your transportation cost form berger to victoria island is N3000 ")

 elif current_location.lower() == "berger" and destination.lower() == "oshodi":
     print("your transportation cost form berger to oshodi is N2000 ")

 elif current_location.lower() == "berger" and destination.lower() == "ikeja":
     print("your transportation cost form berger to ikeja is N2000 ")
 else:
    print("check and enter the available routes ")
 print("")
transportation()
while True:
  
 
 Continuity = input('do you want to try other available route? \n enter yes to continue or no to abort')
 if Continuity.lower() == 'yes':
     transportation()
 else:
     sys.exit()
     
 
    

