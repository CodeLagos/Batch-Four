#Welcome user
print('Welcome to ABOUTNAIJA\nThis program can give you so much information about Nigeria and the States within, including the Federal Capital Territory')
#Prompt user for username
username=input('Please enter your username: ')
#With the use of a while loop, ensure repetition of the program pending when the user decides to abort
repeat=input('Please type 1 to proceed, otherwise press any other character to terminate program: ')

while repeat=='1':
    select1=input('make your choice from the options by typing in the number associated with your choice.\ntype 1 if you want information about Nigeria\nType 2 if you want information about a particular state in Nigeria\nType 3 if you wish to terminate the program\n__')
    #with the use of ‘if’ structure, allow user to choose whether he/she wants information about the country or particular state.
    if select1=='1':
        #Prompt user for the particular informatio he/she requires
        naija=input('Type A for General information about Nigeria\nType B for information about the History of Nigeria\nType C for information about the various cultures in Nigeria\nType D for informatio about the Economy of Nigereia\nType E for information about the Etymology of the name - Nigeria\nType F for informatio aout the Geography of Nigeria\nType G for information about the Government and Politics of Nigeria\nType H for informatio about the Nigerian Society\nType I for information about Tourism in Nigeria\nType J for information about Social Issues in Nigeria\n__')
        print()
        if naija.lower()=='a':
            nigeria=open('Nigeria_General.txt')
            print('GENERAL INFORMATION ABOUT NIGERA\n')
            for line in nigeria:
                print(line)
            print('source: wikipedia.com')
            nigeia.close()
        elif naija.lower()=='b':
            print('HISTORY OF NIGERIA\n')
            nigeria=open('Nigeria_History.txt')
            for line in nigeria:
                print(line)
            print('source: wikipedia.com')
            nigeria.close()
        elif naija.lower()=='c':
            print('NIGERIA PEOPLES AND CULTURE\n')
            nigeria=open('Nigeria_Culture.txt')
            for line in nigeria:
                print(line)
            print('source: wikipedia.com')
            nigeria.close()
        elif naija.lower()=='d':
            print('ECONOMY OF NIGERIA\n')
            nigeria=open('Nigeria_Economy.txt')
            for line in nigeria:
                print(line)
            print('source: wikipedia.com')
            nigeria.close()
        elif naija.lower()=='e':
            print('ETYMOLOGY OF NIGERIA\n')
            nigeria=open('Nigeria_Etymology.txt')
            for line in nigeria:
                print(line)
            print('source: wikipedia.com')
            nigeria.close()
        elif naija.lower()=='f':
            print('GEOGRAPHY OF NIGERIA\n')
            nigeria=open('Nigeria_Geography.txt')
            for line in nigeria:
                print(line)
            nigeria.close()
            print('source: wikipedia.com')
        elif naija.lower()=='g':
            print('GOVERNMENT AND POLITICS IN NIGERIA\n')
            nigeria=open('Nigeria_Government_and_Politics.txt')
            for line in nigeria:
                print(line)
            nigeria.close()
            print('source: wikipedia.com')
        elif naija.lower()=='h':
            print('THE NIGERIAN SOCIETY\n')
            nigeria=open('Nigeria_Society.txt')
            for line in nigeria:
                print(line)
            nigeria.close()
            print('source: wikipedia.com')
        elif naija.lower()=='i':
            print('TOURISM IN NIGERIA\n')
            nigeria=open('Nigeria_Tourism.txt')
            for line in nigeria:
                print(line)
            nigeria.close()
            print('source: wikipedia.com')
        elif naija.lower()=='j':
            print('SOCIAL ISSUES IN NIGERIA\n')
            nigeria=open('Nigeria_Social_Issues.txt')
            for line in nigeria:
                print(line)
            nigeria.close()
            print('source: wikipedia.com')
    elif select1=='2':
        #Prompt user for the state user is interested in if state is selected.
        state=input('Which of the states would you like to learn about?\nChoose your option from the list by typing the name of the state in full, exactly as it appears.\nAbia - Adamawa - Akwa Ibom - Anambra - Bauchi - Bayelsa - Benue - Borno - Cross River - Delta - Ebonyi - Edo - Ekiti - Enugu - Gombe - Imo- Jigawa - Kaduna - Kano - Katsina - Kebbi - Kogi - Kwara - Lagos - Nasarawa - Niger - Ogun - Ondo - Osun - Oyo - Plateau - Rivers - Sokoto - Taraba - Yobe - Zamfara - FCT\n__').lower()
        if state=='abia'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='adamawa'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Economy, E - Local Government Areas, F - Notable People, G - Sites of Interest\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ADAMAWA STATE\n')
                adamawa=open('Adamawa_General.txt')
                for line in adamawa:
                    print(line)
                adamawa.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('GEOGRAPHY OF ADAMAWA STATE\n')
                adamawa=open('Adamawa_Geography.txt')
                for line in adamawa:
                    print(line)
                adamawa.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('HISTORY OF ADAMAWA STATE\n')
                adamawa=open('Adamawa_History.txt')
                for line in adamawa:
                    print(line)
                adamawa.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('ECONOMY OF ADAMAWA STATE\n')
                adamawa=open('Adamawa_Economy.txt')
                for line in adamawa:
                    print(line)
                adamawa.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ADAMAWA STATE\n')
                adamawa=open('Adamawa_LGA.txt')
                for line in adamawa:
                    print(line)
                adamawa.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('NOTABLE PEOPLE IN ADAMAWA STATE\n')
                adamawa=open('Adamawa_Notable_People.txt')
                for line in adamawa:
                    print(line)
                adamawa.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('SITES OF INTEREST IN ABIA STATE\n')
                adamawa=open('Adamawa_Sites_of_Interest.txt')
                for line in adamawa:
                    print(line)
                adamawa.close()
                print('source: wikipedia.com')
            else:
                print('invalid entry')
                
        if state=='akwa Ibom'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - Demography, B - Education, C - General Information, D - History, E - Local Government Areas, F - Major Cities, G - Ministries, Departments and Agencies, H - Notable People, I - Politics\n__').lower()
            if info=='a'.lower():
                print('DEMOGRAPHIC INFORMATION ABOUT AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_Demography.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('EDUCATION IN AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_Education.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('GENERAL INFORMATION ABOUT AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('HISTORY OF AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_History.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('MAJOR CITIES IN AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_Major_Cities.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('MINISTRIES, DEPARTMENTS AND AGENCIES IN AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_MDAs.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='h'.lower():
                print('NOTABLE PEOPLE IN AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_Notable_People.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='i'.lower():
                print('POLITICS IN AKWA IBOM STATE\n')
                abia=open('Akwa_Ibom_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='Anambra'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - Cities and Administrative Divisions, B - Culture and Tourism, C - Education, D - General information, E - Geography, F - History, G - Local Government Areas, H - Natural Resources, I - Notable People, J - Politics, K - Urbanization and Structural Planning in Anambra State\n__').lower()
            if info=='a'.lower():
                print('CITIES AND ADMINISTRATIVE DIVISIONS IN ANAMBRA STATE\n')
                abia=open('Anambra_Cities_and_Administrative_Divisions.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('CULTURE AND TOURISM IN ANAMBRA STATE\n')
                abia=open('Anambra_Culture&Tourism.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('EDUCATION IN ANAMBRA STATE\n')
                abia=open('Anambra_Education.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('GENERAL INFORMATION ABOUT ANAMBRA STATE\n')
                abia=open('Anambra_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('GEOGRAPHY OF ANAMBRA STATE\n')
                abia=open('Anambra_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('HISTORY OF ANAMBRA STATE\n')
                abia=open('Anambra_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('LOCAL GOVENMENT AREAS IN ANAMBRA STATE\n')
                abia=open('Anambra_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='h'.lower():
                print('NATURAL RESOURCES IN ANAMBRA STATE\n')
                abia=open('Anambra_Natural_Resources.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='i'.lower():
                print('NOTABLE PEOPLE IN ANAMBRA STATE\n')
                abia=open('Anambra_Notable_People.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='j'.lower():
                print('POLITICS IN ANAMBRA STATE\n')
                abia=open('Anambra_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='k'.lower():
                print('URBANIZATION AND STRUCTURAL PLANNING IN ANAMBRA STATE\n')
                abia=open('Anambra_Urbanization_and_Structural_Planning.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='Bauchi'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - Etymology, B - General Information, C - Geography, D - History, E - Local Government Areas, F - Population\n__').lower()
            if info=='a'.lower():
                print('ETYMOLOGY OF BAUCHI STATE\n')
                abia=open('Bauchi_Etymology.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('GENERAL INFORMATION ABOUT BAUCHI STATE\n')
                abia=open('Bauchi_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('GEOGRAPHY OF BAUCHI STATE\n')
                abia=open('Bauchi_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('HISTORY OF BAUCHI STATE\n')
                abia=open('Bauchi_History.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN BAUCHI STATE\n')
                abia=open('Bauchi_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='bayelsa'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - Diaspora, B - Economy, C - Education, D - General Information, E - Geography, F - History, G - , H - Local Government Areas, I - Notable People\n__').lower()
            if info=='a'.lower():
                print('BAYELSA IN DIASPORA STATE\n')
                abia=open('Bayelsa_Diaspora.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('EONOMY OF BAYELSA STATE\n')
                abia=open('Bayelsa_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('EDUCATION IN BAYELSA STATE\n')
                abia=open('Bayelsa_Education.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('GENERAL INFORMATION ABOUT BAYELSA STATE\n')
                abia=open('Bayelsa_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('GEOGRAPHY OF BAYELSA STATE\n')
                abia=open('Bayelsa_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('HISTORY OF BAYELSA STATE\n')
                abia=open('Bayelsa_History.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('LOCAL GOVERNMENT AREAS OF BAYELSA STATE\n')
                abia=open('Bayelsa_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='h'.lower():
                print('NOTABLE PEOPLE OF BAYELSA DESCENT\n')
                abia=open('Bayelsa_Notable_Peope.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='benue'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - Capital, B - Economy, C - Education, D - General, E - Geology and Environment, F - History, G - Local Government Areas, H - People and Culture\n__').lower()
            if info=='a'.lower():
                print('CAPITAL CITY OF BENUE STATE\n')
                abia=open('Benue_Capital.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('ECONOMY OF BENUE STATE\n')
                abia=open('Benue_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('EDUCATION IN BENUE STATE\n')
                abia=open('Benue_Education.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('GENERAL INFORMATION ABOUT BENUE STATE STATE\n')
                abia=open('Benue_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('GEOLOGY AND ENVIRONMENT OF BENUE STATE\n')
                abia=open('Benue_Geology_and_Environment.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('HISTORY OF BENUE STATE\n')
                abia=open('Benue_History.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('LOCAL GOVERNMENT AREAS IN BENUE STATE\n')
                abia=open('Benue_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='h'.lower():
                print('PEOPLE AND CULTURE OF BENUE STATE\n')
                abia=open('Benue_People_and_Culture.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='borno'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - History, C - Local Government Areas, D - Religion\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT BORNO STATE\n')
                abia=open('Borno_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('HISTORY OF BORNO STATE\n')
                abia=open('Borno_History.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('LOCAL GOVERNMENT AREAS IN BORNO STATE\n')
                abia=open('Borno_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('RELIGION IN BORNO STATE\n')
                abia=open('Borno_Religion.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='Cross River'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                print('source: wikipedia.com')
                
        if state=='Delta'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Ebonyi'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='edo'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='ekiti'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='enugu'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='gombe'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Imo'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Jigawa'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Kaduna'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Kano'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Katsina'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Kebbi'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        if state=='Kogi'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Kwara'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Lagos'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Nasarawa'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Niger'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Ogun'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Ondo'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Osun'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Oyo'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Plateau'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Rivers'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Sokoto'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Taraba'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Yobe'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='Zamfara'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()

        if state=='FCT'.lower():
            info=input('chose the info you want from the list by typing the associated alphabet\nA - General information, B - Geography, C - History, D - Infracstructure, E - Local Government Areas, F - Politics, G - Travel information, H - Universities and Colleges\n__').lower()
            if info=='a'.lower():
                print('GENERAL INFORMATION ABOUT ABIA STATE\n')
                abia=open('Abia_General.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='b'.lower():
                print('GEOGRAPHY OF ABIA STATE\n')
                abia=open('Abia_Geography.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='c'.lower():
                print('HISTORY OF ABIA STATE\n')
                abia=open('Abia_History.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='d'.lower():
                print('ECONOMY AND INFRACSTRUCTURAL DEVELOPMENT OF ABIA STATE\n')
                abia=open('Abia_Infracstructure_Economy.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='e'.lower():
                print('LOCAL GOVERNMENT AREAS IN ABIA STATE\n')
                abia=open('Abia_LGA.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='f'.lower():
                print('POLITICS IN ABIA STATE\n')
                abia=open('Abia_Politics.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='g'.lower():
                print('TRAVEL INFORMATION IN ABIA STATE\n')
                abia=open('Abia_Travel.txt')
                for line in abia:
                    print(line)
                abia.close()
            elif info=='h'.lower():
                print('UNIVERSITIES AND COLLEGES IN ABIA STATE\n')
                abia=open('Abia_Universities_Colleges.txt')
                for line in abia:
                    print(line)
                abia.close()
                
        
    else:
        print('invalid response')


#Prompt user for the kind of information required, those available will include: political information, population information, geographical information and industrial information.
#Read information from relevant file
#Display information
#Ensure to prompt user for selection for the while loop check
    repeat=input('\nPlease type 1 to continue, otherwise press any other character to terminate program: ')
print('\nYou have chosen to exit\nThanks for your time. Goodbye')

