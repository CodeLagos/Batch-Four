#AREOLA OLUSHOLA MICHAEL CodeLagos 4.0 PROJECT

#This program calculate the Capital Allowances of Non-Current Assets
print("This program is to calculate the Capital Allowances of Non-Current Assets")

iabuilding = 0.15
aabuilding = 0.10
iaPlants = 0.5
aaPlants = 0.25
iaVehicles = 0.5
aaVehicles = 0.25
iaFurnitures = 0.25
aaFurnitures = 0.20
Year = 0


#Ask the user to enter the Year
YEAR =  int(input("choose the year \n1) 1 \n2) 2 \n3) 3 \n4) 4 \n5) 5 \n6) 6 \n7) 7 \n8) 8 \n9) 9 \n10) 10 \n) "))

if (YEAR==1) :
    
    #Ask the user to enter the Asset Type    
    Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

    if (Asset==1):
          #Ask the user to enter Cost of the building
          Cost = int(input("enter the Cost of your Building: "))

          #Calculate the Initial Allowance 
          Initial = Cost*iabuilding

          #Display the value of your calculation
          print("The initial Allowance of your Building is", Initial)

          #Calculate the Balance
          Balance = Cost-Initial

          #Display the value of your calculation
          print("The Balance after deducting Initial Allowance is ", Balance)

          #Calculate the Current Year Annual Allowance 
          Annual1 = Balance*aabuilding

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Building is", Annual1)

          #Calculate the Tax Written Down Value of Building
          Y1TWDVB = Cost-Initial-Annual1
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Building is", Y1TWDVB)

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

if (Asset==2):
          #Ask the user to enter Cost of the plant
          Cost = int(input("enter the Cost of your Plants: "))

          #Calculate the Initial Allowance 
          Initial = Cost*iaPlants

          #Display the value of your calculation
          print("The Initial Allowance of your Plants is", Initial)

          #Calculate the Balance
          Balance = Cost-Initial

          #Display the value of your calculation
          print("The Balance after deducting Initial Allowance is", Balance)
      
          #Calculate the Annual Allowance 
          Annual2 = Balance*aaPlants

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Plants is", Annual2)

          #Calculate the Tax Written Down Value of Building
          Y1TWDVP = Cost-Initial-Annual2
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Plants is", Y1TWDVP)

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

if (Asset==3):
          #Ask the user to enter Cost of the Vehicle
          Cost = int(input("enter the Cost of your Vehicles: "))

          #Calculate the Initial Allowance 
          Initial = Cost*iaVehicles

          #Display the value of your calculation
          print("The Initial Allowance of your Vehicles is", Initial)

          #Calculate the Balance
          Balance = Cost-Initial

          #Display the value of your calculation
          print("The Balance after deducting Initial Allowance is", Balance)

          #Calculate the Annual Allowance 
          Annual3 = Balance*aaVehicles
          
          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Vehicles is", Annual3)

          #Calculate the Tax Written Down Value of Vehicles
          Y1TWDVV = Cost-Initial-Annual3
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Vehicles is", Y1TWDVV)

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

if (Asset==4):
          #Ask the user to enter Cost of the Furnitures
          Cost = int(input("enter the Cost of your Furnitures: "))

          #Calculate the Initial Allowance 
          Initial = Cost*iaFurnitures

          #Display the value of your calculation
          print("The Initial Allowance of your Furnitures is", Initial)

          #Calculate the Balance
          Balance = Cost-Initial

          #Display the value of your calculation
          print("The Balance after deducting Initial Allowance is", Balance)

          #Calculate the Annual Allowance 
          Annual4 = Balance*aaFurnitures

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Furnitures is", Annual4)

          #Calculate the Tax Written Down Value of Furnitures
          Y1TWDVF = Cost-Initial-Annual4
          
          #Display the value of your calculation
          print("The Tax Written Down Value of Furnitures is", Y1TWDVF)

          #Calculate the Total Annual Allowance of All Assets 
          Y1TAA = (Annual1+Annual2+Annual3+Annual4)

          #Display the value of your calculation
          print("The Current Year Total Annual Allowance of All Assets is", Y1TAA)

          #Calculate the Total Tax Written Down Value of All Assets
          Y1TTWDVA = (Y1TWDVB+Y1TWDVP+Y1TWDVV+Y1TWDVF)
          
          #Display the value of your calculation
          print("The Tax Written Down Value of of All Assets is", Y1TTWDVA)

#Ask the user to enter the Year
YEAR =  int(input("choose the year \n1) 1 \n2) 2 \n3) 3 \n4) 4 \n5) 5 \n6) 6 \n7) 7 \n8) 8 \n9) 9 \n10) 10 \n) "))
    
if (YEAR==2):
    
#Ask the user to enter the Asset Type    
    Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

    if (Asset==1):
          #Tax Written Down Value Brought forward
          print("The Tax Written Down Value of your Building is", Y1TWDVB)

          #Calculate the Annual Allowance 
          Annual1 = Y1TWDVB/9

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Building is", Annual1)

          #Calculate the Accumulated Annual Allowance of Building till date
          AAA = Annual1*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Building is", AAA)

          #Calculate the Tax Written Down Value of Building
          Y2TWDVB = Y1TWDVB-Annual1
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Building is", Y2TWDVB)


#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==2):
          
          #Tax Written Down Value of Plants Brought forward
          print("The Tax Written Down Value of your Plants is", Y1TWDVP)

          #Calculate the Annual Allowance of plants 
          Annual2 = Y1TWDVP/3

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Plants is", Annual2)

          #Calculate the Accumulated Annual Allowance of Plants till date
          AAA = Annual2*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Plants is", AAA)

          #Calculate the Tax Written Down Value of your Plants
          Y2TWDVP = Y1TWDVP-Annual2
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Plants is", Y2TWDVP)
          


#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
           
if (Asset==3):
          #Tax Written Down Value of Vehicles Brought forward
          print("The Tax Written Down Value of your Vehicles is", Y1TWDVV)

          #Calculate the Annual Allowance 
          Annual3 = Y1TWDVV/3

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Vehicles is", Annual3)

          #Calculate the Accumulated Annual Allowance of Vehicles till date
          AAA = Annual3*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Vehicles is", AAA)

          #Calculate the Tax Written Down Value of your Vehicles
          Y2TWDVV = Y1TWDVV-Annual3
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Vehicles is", Y2TWDVV)
          

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==4):

          #Tax Written Down Value of Furnitures Brought forward
          print("The Tax Written Down Value of your Furnitures is", Y1TWDVF)

          #Calculate the Annual Allowance 
          Annual4 = Y1TWDVF/4

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Furnitures is", Annual4)

          #Calculate the Accumulated Annual Allowance of Furnitures till date
          AAA = Annual4*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Furnitures is", AAA)

          #Calculate the Tax Written Down Value of Furnitures
          Y2TWDVF = Y1TWDVF-Annual4
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Furnitures is", Y2TWDVF)
          

          #Calculate the Total Annual Allowance of All Assets 
          Y2TAA = (Annual1+Annual2+Annual3+Annual4)

          #Display the value of your calculation
          print("The Current Year Total Annual Allowance of All Assets is", Y2TAA)

          #Calculate the Total Tax Written Down Value of All Assets
          Y2TTWDVA = (Y2TWDVB+Y2TWDVP+Y2TWDVV+Y2TWDVF)
          
          #Display the value of your calculation
          print("The Tax Written Down Value of of All Assets is", Y2TTWDVA)


  
#Ask the user to enter the Year
YEAR =  int(input("choose the year \n1) 1 \n2) 2 \n3) 3 \n4) 4 \n5) 5 \n6) 6 \n7) 7 \n8) 8 \n9) 9 \n10) 10 \n) "))
    
if (YEAR==3):
    
#Ask the user to enter the Asset Type    
    Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

    if (Asset==1):
          #Tax Written Down Value Brought forward
          print("The Tax Written Down Value of your Building is", Y2TWDVB)

          #Calculate the Annual Allowance 
          Annual1 = Y2TWDVB/8

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Building is", Annual1)

          #Calculate the Accumulated Annual Allowance of Building till date
          AAA = Annual1*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Building is", AAA)

          #Calculate the Tax Written Down Value of Building
          Y3TWDVB = Y2TWDVB-Annual1
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Building is", Y3TWDVB)


#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==2):
          
          #Tax Written Down Value of Plants Brought forward
          print("The Tax Written Down Value of your Plants is", Y2TWDVP)

          #Calculate the Annual Allowance of plants 
          Annual2 = Y2TWDVP/2

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Plants is", Annual2)

          #Calculate the Accumulated Annual Allowance of Plants till date
          AAA = Annual2*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Plants is", AAA)

          #Calculate the Tax Written Down Value of your Plants
          Y3TWDVP = Y2TWDVP-Annual2
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Plants is", Y3TWDVP)
          


#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
           
if (Asset==3):
          #Tax Written Down Value of Vehicles Brought forward
          print("The Tax Written Down Value of your Vehicles is", Y2TWDVV)

          #Calculate the Annual Allowance 
          Annual3 = Y2TWDVV/2

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Vehicles is", Annual3)

          #Calculate the Accumulated Annual Allowance of Vehicles till date
          AAA = Annual3*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Vehicles is", AAA)

          #Calculate the Tax Written Down Value of your Vehicles
          Y3TWDVV = Y2TWDVV-Annual3
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Vehicles is", Y3TWDVV)
          

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==4):

          #Tax Written Down Value of Furnitures Brought forward
          print("The Tax Written Down Value of your Furnitures is", Y2TWDVF)

          #Calculate the Annual Allowance 
          Annual4 = Y2TWDVF/3

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Furnitures is", Annual4)

          #Calculate the Accumulated Annual Allowance of Furnitures till date
          AAA = Annual4*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Furnitures is", AAA)

          #Calculate the Tax Written Down Value of Furnitures
          Y3TWDVF = Y2TWDVF-Annual4
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Furnitures is", Y3TWDVF)
          

          #Calculate the Total Annual Allowance of All Assets 
          Y3TAA = (Annual1+Annual2+Annual3+Annual4)

          #Display the value of your calculation
          print("The Current Year Total Annual Allowance of All Assets is", Y3TAA)

          #Calculate the Total Tax Written Down Value of All Assets
          Y3TTWDVA = (Y3TWDVB+Y3TWDVP+Y3TWDVV+Y3TWDVF)
          
          #Display the value of your calculation
          print("The Tax Written Down Value of of All Assets is", Y3TTWDVA)

#Ask the user to enter the Year
YEAR =  int(input("choose the year \n1) 1 \n2) 2 \n3) 3 \n4) 4 \n5) 5 \n6) 6 \n7) 7 \n8) 8 \n9) 9 \n10) 10 \n) "))
    
if (YEAR==4):
    
#Ask the user to enter the Asset Type    
    Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

    if (Asset==1):
          #Tax Written Down Value Brought forward
          print("The Tax Written Down Value of your Building is", Y3TWDVB)

          #Calculate the Annual Allowance 
          Annual1 = Y3TWDVB/7

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Building is", Annual1)

          #Calculate the Accumulated Annual Allowance of Building till date
          AAA = Annual1*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Building is", AAA)

          #Calculate the Tax Written Down Value of Building
          Y4TWDVB = Y3TWDVB-Annual1
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Building is", Y4TWDVB)


#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==2):
          
          #Tax Written Down Value of Plants Brought forward
          print("The Tax Written Down Value of your Plants is", Y3TWDVP)

          #Calculate the Annual Allowance of plants 
          Annual2 = Y3TWDVP/1

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Plants is", Annual2)

          #Calculate the Accumulated Annual Allowance of Plants till date
          AAA = Annual2*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Plants is", AAA)

          #Calculate the Tax Written Down Value of your Plants
          Y4TWDVP = Y3TWDVP-Annual2
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Plants is", Y4TWDVP)

        

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
           
if (Asset==3):
          #Tax Written Down Value of Vehicles Brought forward
          print("The Tax Written Down Value of your Vehicles is", Y3TWDVV)

          #Calculate the Annual Allowance 
          Annual3 = Y3TWDVV/1

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Vehicles is", Annual3)

          #Calculate the Accumulated Annual Allowance of Vehicles till date
          AAA = Annual3*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Vehicles is", AAA)

          #Calculate the Tax Written Down Value of your Vehicles
          Y4TWDVV = Y3TWDVV-Annual3
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Vehicles is", Y4TWDVV)
          

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==4):

          #Tax Written Down Value of Furnitures Brought forward
          print("The Tax Written Down Value of your Furnitures is", Y3TWDVF)

          #Calculate the Annual Allowance 
          Annual4 = Y3TWDVF/2

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Furnitures is", Annual4)

          #Calculate the Accumulated Annual Allowance of Furnitures till date
          AAA = Annual4*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Furnitures is", AAA)

          #Calculate the Tax Written Down Value of Furnitures
          Y4TWDVF = Y3TWDVF-Annual4
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Furnitures is", Y4TWDVF)
          
          #Calculate the Total Annual Allowance of All Assets 
          Y4TAA = (Annual1+Annual2+Annual3+Annual4)

          #Display the value of your calculation
          print("The Current Year Total Annual Allowance of All Assets is", Y4TAA)

          #Calculate the Total Tax Written Down Value of All Assets
          Y4TTWDVA = (Y4TWDVB+Y4TWDVP+Y4TWDVV+Y4TWDVF)
          
          #Display the value of your calculation
          print("The Tax Written Down Value of of All Assets is", Y4TTWDVA)

#Ask the user to enter the Year
YEAR =  int(input("choose the year \n1) 1 \n2) 2 \n3) 3 \n4) 4 \n5) 5 \n6) 6 \n7) 7 \n8) 8 \n9) 9 \n10) 10 \n) "))
    
if (YEAR==5):
    
#Ask the user to enter the Asset Type    
    Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))

    if (Asset==1):
          #Tax Written Down Value Brought forward
          print("The Tax Written Down Value of your Building is", Y4TWDVB)

          #Calculate the Annual Allowance 
          Annual1 = Y4TWDVB/6

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Building is", Annual1)

          #Calculate the Accumulated Annual Allowance of Building till date
          AAA = Annual1*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Building is", AAA)

          #Calculate the Tax Written Down Value of Building
          Y5TWDVB = Y4TWDVB-Annual1
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Building is", Y5TWDVB)


#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==2):
          
          #Tax Written Down Value of Plants Brought forward
          print("The Tax Written Down Value of your Plants is", Y4TWDVP)

          #Calculate the Annual Allowance of plants 
          Annual2 = Y4TWDVP/1

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Plants is", Annual2)

          #Calculate the Accumulated Annual Allowance of Plants till date
          AAA = Annual2*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Plants is", AAA)

          #Calculate the Tax Written Down Value of your Plants
          Y5TWDVP = Y4TWDVP-Annual2
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Plants is", Y5TWDVP)
          


#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
           
if (Asset==3):
          #Tax Written Down Value of Vehicles Brought forward
          print("The Tax Written Down Value of your Vehicles is", Y4TWDVV)

          #Calculate the Annual Allowance 
          Annual3 = Y4TWDVV/1

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Vehicles is", Annual3)

          #Calculate the Accumulated Annual Allowance of Vehicles till date
          AAA = Annual3*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Vehicles is", AAA)

          #Calculate the Tax Written Down Value of your Vehicles
          Y5TWDVV = Y4TWDVV-Annual3
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Vehicles is", Y5TWDVV)
          

#Ask the user to enter the Asset Type    
Asset =  int(input("choose the Asset Type \n1) Building \n2) Plants \n3) Vehicles \n4) Furnitures \n) "))
       
if (Asset==4):

          #Tax Written Down Value of Furnitures Brought forward
          print("The Tax Written Down Value of your Furnitures is", Y4TWDVF)

          #Calculate the Annual Allowance 
          Annual4 = Y4TWDVF/1

          #Display the value of your calculation
          print("The Current Year Annual Allowance of your Furnitures is", Annual4)

          #Calculate the Accumulated Annual Allowance of Furnitures till date
          AAA = Annual4*YEAR

          #Display the value of your calculation
          print("The Total Accumulated Annual Allowance of your Furnitures is", AAA)

          #Calculate the Tax Written Down Value of Furnitures
          Y5TWDVF = Y4TWDVF-Annual4
          
          #Display the value of your calculation
          print("The Tax Written Down Value of your Furnitures is", Y5TWDVF)
          

          #Calculate the Total Annual Allowance of All Assets 
          Y5TAA = (Annual1+Annual2+Annual3+Annual4)

          #Display the value of your calculation
          print("The Current Year Total Annual Allowance of All Assets is", Y5TAA)

          #Calculate the Total Tax Written Down Value of All Assets
          Y5TTWDVA = (Y2TWDVB+Y5TWDVP+Y5TWDVV+Y5TWDVF)
          
          #Display the value of your calculation
          print("The Tax Written Down Value of of All Assets is", Y5TTWDVA)

