def Ikeja(): 
           Constituency1 = [ 'Airport/Onipetesi/Inilekere','Ipodo/Seriki Aro','Ojodu / Agidingbi / Omole','Alausa / Oregun / Olusosun','Anifowoshe / Ikeja']
           Constituency2 = [ 'Onigbongbon','Oke Ira/Aguda','Adekunle / Adeniyi jones / Ogba','Wasimi / Opebi / Allen','GRA / Police barracks' ]
           for i in Constituency2:
               print(i)
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

    print("Select  constituency")
    Constituencies = input(" 1 Constituency1 \n 2 Constituency2 \n Enter Value: ")
    if (Constituencies == '1'):
        print("Constituency1")
        for i in Constituency1:
            print(i)
            print("Select the Area")
            ikeja1()
    else:
        print("Constituency2")

    Ikeja()
