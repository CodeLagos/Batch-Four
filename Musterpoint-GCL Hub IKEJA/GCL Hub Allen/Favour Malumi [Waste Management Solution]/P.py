def Ikeja1():
                    Ikeja1 = input(" 1 'Airport/Onipetesi/Inilekere' \n 2 'Ipodo/Seriki Aro' \n 3 'Ojodu / Agidingbi / Omole' \n 4 'Alausa / Oregun / Olusosun' \n 5 'Anifowoshe / Ikeja'")
                    if (Ikeja1 == '1'):
                        print(Constituency1[0])
                    elif (Ikeja1 == '2'):
                        print(Constituency1[1])
                    elif (Ikeja1 == '3'):
                        print(Constituency1[2])
                    elif (Ikeja1 == '4'):
                        print(Constituency1[3])
                    elif (Ikeja1 == '5'):
                        print(Constituency1[4])
                    else:
                        Choice()
Ikeja1()

def Ikeja(): 
                       Constituency1 = [ 'Airport/Onipetesi/Inilekere','Ipodo/Seriki Aro','Ojodu / Agidingbi / Omole','Alausa / Oregun / Olusosun','Anifowoshe / Ikeja']
                       Constituency2 = [ 'Onigbongbon','Oke Ira/Aguda','Adekunle / Adeniyi jones / Ogba','Wasimi / Opebi / Allen','GRA / Police barracks' ]
                       print("Select  constituency")
                       Constituencies = input(" 1 Constituency1 \n 2 Constituency2 \n Enter Value: ")
                       if (Constituencies == '1'):
                           print("Constituency1")
                           for i in Constituency1:
                               print(i)
                               print("Select the Area")
                           else:
                               print("Constituency2")

Ikeja()


LGA = [ 'Agege', 'Alimosho', 'Ajeromi-ifelodun', 'Apapa', 'Amuwo-Odofin', 'Badagry', 'Epe', 'Eti-Osa', 'Ibeju/Lekki', 'Ifako_Ijaiye', 'Ikeja', 'Ikorodu', 'Kosofe', 'LagosIsland', 'LagosMainland', 'Shomolu', 'Mushin', 'Ojo', 'Oshodi-Isolo', 'Surulere' ]

def Location():
        for i in LGA:
              print(i)

Location()

         
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
        Location()

            

            
                
Choice()


#
