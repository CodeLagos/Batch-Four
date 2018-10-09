print('Welcome to Lagos State Property Management site. \n')
print('Project done by Adepoju Temitope. \n Email: tpisafreeman@yahoo.com. \n')
print('Facilitator: Mr Dotun Onasanya. \n Center: GCL Hub Ikeja. \n')
print('This Project is on Property Management. \n')
restart=('Y')
chances = 5
while restart not in ('n','NO','no','N'):
    print('Please Press 1 For Properties For Sale List\n')
    print('Please Press 2 For Properties For Lease List\n')
    print('Please Press 3 To Login \n')
    print('Please Press 4 To Sign up\n')
    print('Please Press 5 To Exit\n')
    option = int(input('What Would you like to choose? \n'))
    if option == 1:
        print('Please Press 1 For Properties For Sale on the Mainland\n')
        print('Please Press 2 For Properties For Sale on the Island\n')
        option = int(input('What Would you like to choose?\n'))
        if option == 1:
            print("(1) Tastefully finished 3 bedroom flat in a block of 6 (all room ensuite) at IFAKO GBAGADA. PRICE: N20m (Certificate of Occupancy) UPPER FLOOR APARTMENT.\n (2) Functional school being run as a going concern at AMUWO ODOFIN, BY FESTAC. PRICE: N70m (Certificate of Occupancy). \n (3) Ambassadorial 5 bedroom detached house with BQ AT OMOLE PHASE 2, PRICE: N80m (Certificate of Occupancy)\n ")
            restart = input('Would You you like to go back? \n')
            if restart in ('n','NO','no','N'):
                print('Thank You')
                break
        if option == 2:
            print (" \n (1) Brand new 3 bedroom bungalow (85% completed, fitting left) at LABORA, BY ABIJO GRA, AJAH. PRICE N8M. \n (2) Brand new adorable 3 bedroom terrace house (finished to taste) at LEKKI GARDENS II, AJAH. PRICE: N27m. \n (3) Brand new 3 bedroom semi-detached house with BQ at LEKKI GARDENS II, AJAH. PRICE: N33m. \n (4) Tastefully finished 3 br terrace duplex with BQ by LAGOS BUSINESS SCH., AJAH. PRICE: N28m (Governor's Consent). \n (5) Well built 3 bedroom bungalow at CROWN ESTATE, AJAH. PRICE: N33m (Certificate of Occupancy). \n (6) Nicely finished 4 bedroom semi-detached house with BQ at BUDO PENINSULA ESTATE, AJAH. PRICE: N30m (Governor’s Consent)STRUCTURED PAYMENT ALLOWED. \n")
            restart = input('Would You you like to go back? \n')
            if restart in ('n','NO','no','N'):
                print('Thank You')
                break
    elif option == 2:
        print('Please Press 1 For Properties For Lease on the Mainland\n')
        print('Please Press 2 For Properties For Lease on the Island\n')
        option = int(input('What Would you like to choose?\n'))
        if option == 1:
            print("(1) 4 Bedroom Flat at Balogun Street, Alausa, Ikeja. N900, 000 P/A. \n (2) Open Planned Office Space at Allen Avenue, Ikeja. N2 Million P/A. \n (3) 3 (Nos) 3 Bedroom Luxury Flats at Sule Abuka Crescent, Opebi, Ikeja. N2 Million P/A. \n (4) Prime Fenced Land on 13.8 Acres along Happyhome Avenue, Apapa. N1,000 per Square Feet. \n (5) 3 Bedroom Terrace House at a Serene Area, Agidingbi. N1.6 Million P/A. \n ")
            restart = input('Would You you like to go back? \n')
            if restart in ('n','NO','no','N'):
                print('Thank You')
                break
        if option == 2:
            print (" \n (1) Office space for Lease at Marina, Lagos Island N22,000 per square meter per Annum.\n (2) Office space for Lease, Lewis street, Obalende, Lagos Island, N1,200,00 per Annum. \n (3)Office space for lease, Broad street, Lagos Island, N30,000 per Square meter per Annum. \n ")
            restart = input('Would You you like to go back? \n')
            if restart in ('n','NO','no','N'):
                print('Thank You')
                break
    elif option == 3:
        while chances >= 0:
            password =(input('Please Enter Your password: '))
            if password == ("admin1"):
                print('You entered your password Correctly\n')
                while restart not in ('n','NO','no','N'):
                    print("Please Press 1 For Mainland's Tenants informations \n")
                    print("Please Press 2 For Island's Tenants informations\n")
                    option = int(input('What Would you like to choose? \n'))
                    if option == 1:
                        print("Press 1 For Red Plaza Tenants \n")
                        print("Press 2 For Blue Plaza Tenants \n")
                        option = int(input('What Would you like to choose?'))
                        if option == 1:
                            print("Here are the lists of Occupants in Red Plaza \n")
                            print("Suite 1: Mr. Akinwunmi Ambode: Partitionable large room (Rent Period: 02/03/2018-01/03/2019), Rent: N750,000 \n")
                            print("Suite 2: Miss. Hintel Haltman: Partitionable large room (Rent Period: 01/01/2018-31/12/2018), Rent: N750,000 \n")
                            print("Suite 3: Mr. Idowu Phillips: Partitionable large room (Rent Period: 04/06/2018-03/06/2019), Rent: N750,000 \n")
                            print("Suite 4: Mrs Aisha Buhari: Partitionable large room (Rent Period: 02/03/2018-01/03/2019) Rent: N750,000 \n")
                            restart = input('Would You you like to go back? \n')
                            if restart in ('n','NO','no','N'):
                                print('Thank You')
                                break
                        if option == 2:
                            print("Here are the lists of Occupants in Blue Plaza \n")
                            print("Suite 1: Mr. Lai Mohammed: Partitionable large room (Rent Period: 01/08/2018-31/07/2019), Rent: N500,000 \n")
                            print("Suite 2: Miss. Temi Otedola: Partitionable large room (Rent Period: 02/03/2018-01/03/2019), Rent: N500,000 \n")
                            print("Suite 3: Dr. Chris Ngige: Partitionable large room (Rent Period: 04/03/2018-03/03/2019), Rent: N500,000 \n")
                            print("Suite 4: Mr. Babatunde Raji Fashola: Partitionable large room (Rent Period: 31/01/2018-30/01/2019) Rent: N500,000 \n")
                            restart = input('Would You you like to go back? \n ')
                            if restart in ('n','NO','no','N'):
                                print('Thank You')
                                break
                    if option == 2:
                        print("Press 1 For Aerodrome Building, Eko Atlantic City \n")
                        print("Press 2 For Lekki Garden's Tenants \n")
                        option = int(input('What Would you like to choose?'))
                        if option == 1:
                            print("Here are the lists of Occupants in Aerodrome Building, Eko Atlantic City \n")
                            print("Ground Floor: Mr. Temitope Adepoju (Rent Period: 31/01/2018-30/01/2019), Rent: N1,500,000 \n")
                            print("First Floor: Mr. Dotun Onasanya (Rent Period: 02/03/2018-01/03/2019), Rent: N1,500,000 \n")
                            print("Second Floor: Dr. Olubukola Saraki (Rent Period: 30/03/2018-29/03/2019), Rent: N1,500,000 \n")
                            print("Third Floor: Asiwaju Bola Tinubu (Rent Period: 01/01/2018-31/12/2019), Rent: N1,500,000 \n")
                            print("Fourth Floor: Asiwaju Bola Tinubu (Rent Period: 01/01/2018-31/12/2019), Rent: N1,500,000 \n")
                            print("Fifth Floor: Asiwaju Bola Tinubu (Rent Period: 01/01/2018-31/12/2019), Rent: N1,500,000 \n")
                            restart = input('Would You you like to go back? \n')
                            if restart in ('n','NO','no','N'):
                                print('Thank You')
                                break
                        if option == 2:
                            print("Here are the lists of Occupants in Lekki Gardens \n")
                            print("Building 1: Stealth Security Company (Rent Period: 04/10/2017-03/10/2018), Rent: N2,500,000 \n")
                            print("Building 2: Dangote Cement Company (Rent Period: 04/10/2017-03/10/2018), Rent: N2,500,000 \n")
                            print("Building 3: Architeknik Construction Company (Rent Period: 04/10/2017-03/10/2018), Rent: N2,500,000 \n")
                            print("Building 4: Goodnews Cars (Rent Period: 04/10/2017-03/10/2018), Rent: N2,500,000 \n")
                            restart = input('Would You you like to go back? \n ')
                            if restart in ('n','NO','no','N'):
                                print('Thank You')
                                break
            else:
                print("invalid Password")
    elif option == 4:
        company_name=(input("Please Enter Your Company Name: \n"))
        cac_no=(input("Please Enter your Company CAC Number: \n"))
        company_address= (input("Please Enter your Company Address: \n"))
        company_mail=(input("Please Enter your Company Email: \n"))
        password=(input("Please Enter a Password: \n"))
        Re_password=(input("Please Re-Enter your Password: \n"))
        if password == Re_password:
            print("Password Match")
        else:
            print("Password does not Match")
        print("Company Name: ", company_name)
        print("\n Company's CAC Number: ", cac_no)
        print("\n Your Company Address: ", company_address)
        print("\n Your Company E-Mail Address: ", company_mail)
        print("\n Thank You for signing up with the Lagos state Property Management")
        print("\n Your Account has been created. \n kindly check your mail box for a link to activate your Account")
        restart = input(' Would You you like to go back? \n')
        if restart in ('n','NO','no','N'):
            print('Thank You')
            break
    elif option == 5:
                print('Thank you for using our service')
                break
        
            
        
