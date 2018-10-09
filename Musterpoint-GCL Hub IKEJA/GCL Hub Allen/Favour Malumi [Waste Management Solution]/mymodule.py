
def WelcomeUser():
        print("Welcome to Franchise with Wellness Waste Management Company")
        print ("Looking Forward to a cordial business relationship with you")

        #Print type of waste
        print("Waste Type Disposal of Cleaning Company")

        Option =input("1 Industrial Waste \n 2 Residential Yard waste \n Enter Value: ")
         
        if (Option == "1" or "2"):
            print("For Effective Waste Management(Disposal), the Local Government Areas will be used as Municipalities for Distribution of work, Scheduling and Inspection")
            print("Local Government Areas")
            print("LGA = [ 'Agege', 'Alimosho', 'Ajeromi-ifelodun', 'Apapa', 'Amuwo-Odofin', 'Badagry', 'Epe', 'Eti-Osa', 'Ibeju/Lekki', 'Ifako_Ijaiye', 'Ikeja', 'Ikorodu', 'Kosofe', 'LagosIsland', 'LagosMainland', 'Shomolu', 'Mushin', 'Ojo', 'Oshodi-Isolo', 'Surulere']")


        return WelcomeUser

def LOGIN():
    Username = input("Username: ")
    Password = input("Password: ")
    
    return LOGIN


def Schedule():
    Time_Schedule = input("Time Schedule \n 7am - 7pm Monday \n 7am - 7pm Tuesdays \n 7am - 7pm Wednesdays \n 7am - 7pm Thursdays \n 7am - 7pm Fridays \n Execption of Public Holidays - 7am - 7pm (Saturdays)")
    print (Time_Schedule)
    print("Select One")
    Time = input()



def Ikeja1():
    Ikeja1 = input(" 1 'Airport/Onipetesi/Inilekere' \n 2 'Ipodo/Seriki Aro' \n 3 'Ojodu / Agidingbi / Omole' \n 4 'Alausa / Oregun / Olusosun' \n 5 'Anifowoshe / Ikeja' \n Select: ")
    Constituency1 = ["Airport/Onipetesi/Inilekere\n", "Ipodo/Seriki Aro\n", "Ojodu / Agidingbi / Omole\n", "Alausa / Oregun / Olusosun\n", "Anifowoshe / Ikeja"]
    if (Ikeja1 == '1'):
        print(Constituency1[0])
        print("Choose one")
        ResidentialArea = input()
        print("Schedule for Waste Disposal")
        Schedule()
        print(" Continue and update your progress report")
    
    elif (Ikeja1 == '2'):
          print(Constituency1[1], "\nChooseone")
          print("Choose one")
          input()
          print("Schedule for Waste Disposal")
          Schedule()
          print(" Continue and update your progress report")
          
          
    elif (Ikeja1 == '3'):
          print(Constituency1[2])
          print("Choose one")
          input()
          print("Schedule for Waste Disposal")
          Schedule()
          print(" Continue and update your progress report")
          
          
    elif (Ikeja1 == '4'):
          print(Constituency1[3])
          print("Choose one")
          input()
          print("Schedule for Waste Disposal")
          Schedule()
          print(" Continue and update your progress report")
          print("Goodbye")
          
    elif (Ikeja1 == '5'):
          print(Constituency1[4])
          print("Choose one")
          input()
          print("Schedule for Waste Disposal")
          Schedule()
          print(" Continue and update your progress report")
          print("Goodbye")
    else:
        Ikeja()


def Ikeja2():
    Ikeja2 = input(" 1 'Onigbongbon'\n 2 'Oke Ira/Aguda' \n 3 'Adekunle / Adeniyi jones / Ogba' \n 4 'Wasimi / Opebi / Allen' \n 5 'GRA / Police barracks' ")
    Constituency2 = ['Onigbongbon','Oke Ira/Aguda','Adekunle / Adeniyi jones / Ogba','Wasimi / Opebi / Allen','GRA / Police barracks' ]
    if (Ikeja2 == '1'):
        print(Constituency2[0])
    elif (Ikeja2 == '2'):
          print(Constituency2[1])
          print("Choose one")
          input()
    elif (Ikeja2 == '3'):
          print(Constituency2[2])
          print("Choose one")
          input()
    elif (Ikeja2 == '4'):
          print(Constituency2[3])
          print("Choose one")
          input()
    elif (Ikeja2 == '5'):
          print(Constituency2[4])
          print("Choose one")
          input()
    else:
        exit


def Ikeja():
    Constituency1 = input("Constituency1: 'Airport/Onipetesi/Inilekere'\n'Ipodo/Seriki Aro'\n'Ojodu / Agidingbi / Omole'\n'Alausa / Oregun / Olusosun'\n'Anifowoshe / Ikeja'")
    Constituency2 = input("Constituency2: 'Onigbongbon'\n'Oke Ira/Aguda'\n'Adekunle / Adeniyi jones / Ogba'\n'Wasimi / Opebi / Allen'\n'GRA / Police barracks' ")
    Constituencies = input(" 1 Constituency1 \n 2 Constituency2 \n Enter Value: ")
    print (Constituency1)
    print (Constituency2)
    print(Constituencies)
    if (Constituencies == '1'):
        print("Constituency1")
        print("Select the Area")
        Ikeja1()
    else:
        print("Constituency2")
        Ikeja2()
    return Ikeja







LGA = [ 'Agege', 'Alimosho', 'Ajeromi-ifelodun', 'Apapa', 'Amuwo-Odofin', 'Badagry', 'Epe', 'Eti-Osa', 'Ibeju/Lekki', 'Ifako_Ijaiye', 'Ikeja', 'Ikorodu', 'Kosofe', 'LagosIsland', 'LagosMainland', 'Shomolu', 'Mushin', 'Ojo', 'Oshodi-Isolo', 'Surulere' ]         
def Location():
        for i in LGA:
            print(i)
    





def Choice():
    Choice = input(" 0 'Agege' \n 1 'Alimosho' \n 2 'Ajeromi-ifelodun' \n 3 'Apapa' \n 4 'Amuwo-Odofin' \n 5 'Badagry' \n 6 'Epe' \n 7 'Eti-Osa' \n 8 'Ibeju/Lekki' \n 9 'Ifako_Ijaiye' \n 10 'Ikeja' \n 11 'Ikorodu' \n 12 'Kosofe' \n 13 'LagosIsland' \n 14 'LagosMainland' \n 15 'Shomolu' \n 16 'Mushin' \n 17 'Ojo' \n 18 'Oshodi-Isolo' \n 19 'Surulere' \n Enter input: ")
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


   


GA = [ 'Agege', 'Alimosho', 'Ajeromi-ifelodun', 'Apapa', 'Amuwo-Odofin', 'Badagry', 'Epe', 'Eti-Osa', 'Ibeju/Lekki', 'Ifako_Ijaiye', 'Ikeja', 'Ikorodu', 'Kosofe', 'LagosIsland', 'LagosMainland', 'Shomolu', 'Mushin', 'Ojo', 'Oshodi-Isolo', 'Surulere']



def Merge():
    Location()
    print("Select choice of LGA where operation of waste disposal will be implemented by company")
    Choice()


    return Merge

def ProgressonTask():
        print("Select Task Progress Level")
        TaskAchieved = input (" \n (1) 0% \n (2) 25% \n (3) 50% (4) 100% \n Task Progress Level: ")
        while(TaskAchieved != "5"):
                
                if(TaskAchieved == "1"):
                        print("Task has not begun")
                elif(TaskAchieved == "2"):
                        print(" Task Progress Level is Quarter")
                elif(TaskAchieved == "3"):
                        print("Task Progress Level is Half")
                elif(TaskAchieved == "4"):
                        print("Task Progress Level is Three-quarter")
                elif(TaskAchieved == "5"):
                        print("Task Progress Level is Complete")
                else:
                        exit
                        continue
        return ProgressonTask





def ProgressReport():
        print("Go to Progress Report page")
        print("Welcome to Your Progress Report Page")
        print("Register your task for the week")
        Task =input("Task: \nLocation:  \nSchedule: ")
        Task1= []
        Task1.append('Airport; Mondays' )
        print(Task1)
        print("List of Progress Percentage of Completion of Task")
        PercentageCompletion = [ "0%", "25%", "50%", "75%", "100%" ]
        for i in PercentageCompletion:
                print(i)
        ProgressonTask()
        exit
        return ProgressReport()      



