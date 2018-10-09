print("Name of Programmer :Malumi Favour")
print("Email address:favourmalumi@gmail.com")
print("Facilitator: Mr Dotun Onasanya")
print("The Purpose of the Program is to Help Waste Disposal Companies in charge of Waste Disposal in Large Areas")
#Print the purpose of the program
print("Waste Management Solution")

#Print the aim of the program
print("To ensure the environment is keep clean and free of dirts to prevent pollution")

#State the opportunity for Franchise
print ("Cleaning companies can create an account to Franchise")

#Create an account    
print("Fill in Your Details")

Company_Name = input("Company Name: ")

Manager_Name = input("Manager Name: ")

Company_Address = input("Address: ")

Mobile_number = input("Mobile Number: ")

Email_address = input("Email Address: ")

City = input("City: ")

Username = input("Username: ")

Password = input("Password: ")

#Create a Login for Users
print("LOGIN")
Username = input("Username: ")
Password = input("Password: ")

if (Username == "MalumiF" and Password == "1234"):
    print("Welcome On Board")
else:
    print("Username or Password wrong")
    while (Username != "MalumiF" and Password != "1234"):
        import mymodule
        mymodule.LOGIN()
        mymodule.WelcomeUser()
        mymodule.Location()
        mymodule.Choice()
        print("End")
        exit

#Welcome User
print("Welcome to Franchise with Wellness Waste Management Company")
print ("Looking Forward to a cordial business relationship with you")
#Print Opption to select more than one Location
print(" Do you want to select more than one location")
   
ResidentArea = input("(1) Yes (2) No \ Select: ")

#Print type of waste
print("Waste Type Disposal of Cleaning Company")

Option =input("1 Industrial Waste \n 2 Residential Yard waste \n Enter Value: ")
         
if (Option == "1" or "2"):
    print("For Effective Waste Management(Disposal), the Local Government Areas will be used as Municipalities for Distribution of work, Scheduling and Inspection")
    print("Local Government Areas")
    LGA = [ 'Agege', 'Alimosho', 'Ajeromi-ifelodun', 'Apapa', 'Amuwo-Odofin', 'Badagry', 'Epe', 'Eti-Osa', 'Ibeju/Lekki', 'Ifako_Ijaiye', 'Ikeja', 'Ikorodu', 'Kosofe', 'LagosIsland', 'LagosMainland', 'Shomolu', 'Mushin', 'Ojo', 'Oshodi-Isolo', 'Surulere']
    while (ResidentArea == "1"):
        def Location():
                for i in LGA:
                    print(i)

        Location()

        print("Select choice of LGA where operation of waste disposal will be implemented by company")
        def Choice():
            Choice = input(" 0'Agege' \n 1 'Alimosho' \n 2 'Ajeromi-ifelodun' \n 3 'Apapa' \n 4 'Amuwo-Odofin' \n 5 'Badagry' \n 6 'Epe' \n 7 'Eti-Osa' \n 8 'Ibeju/Lekki' \n 9 'Ifako_Ijaiye' \n 10 'Ikeja' \n 11 'Ikorodu' \n 12 'Kosofe' \n 13 'LagosIsland' \n 14 'LagosMainland' \n 15 'Shomolu' \n 16 'Mushin' \n 17 'Ojo' \n 18 'Oshodi-Isolo' \n 19 'Surulere' \n Enter input: ")
            if (Choice == '0'):
                print(LGA[0])

            elif (Choice == '1'):
                  print(LGA[1])

            elif (Choice == '2'):
                  print(LGA[2])

            elif (Choice == '3'):
                  print(LGA[3])
                    
            elif (Choice == '4'):
                  print(LGA[4])
                    
            elif (Choice == '5'):
                  print(LGA[5])
                    
            elif (Choice == '6'):
                  print(LGA[6])
                    
            elif (Choice == '7'):
                  print(LGA[7])
                    
            elif (Choice == '8'):
                  print(LGA[8])
                    
            elif (Choice == '9'):
                  print(LGA[9])
                    
            elif (Choice == '10'):
                  print(LGA[10])
                  print("Select Constituency")
                  import mymodule
                  mymodule.Ikeja()
                  print(" Do you want to select more than one location")
                  ResidentArea = input("(1) Yes (2) No \ Select: ")

                  if (ResidentArea == "1"):
                      print("Select Waste type disposal Cleaning Company")
                  else:
                      import mymodule
                      mymodule.ProgressReport()
                      exit
                         
            elif (Choice == '11'):
                  print(LGA[11])
                    
            elif (Choice == '12'):
                  print(LGA[12])
                          
            elif (Choice == '13'):
                  print(LGA[13])
                    
            elif (Choice == '14'):
                
                  print(LGA[14])
                    
            elif (Choice == '15'):
                  print(LGA[15])
                    
            elif (Choice == '16'):
                  print(LGA[16])
                    
            elif (Choice == '17'):
                  print(LGA[17])
                    
            elif (Choice == '18'):
                  print(LGA[18])
                    
            elif (Choice == '19'):
                  print(LGA[19])
            else:
                print("Select one")
            

                

                
                    
        Choice()


        #Go to 
