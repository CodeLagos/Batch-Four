#Adedoja Kalejaye
#kalybabe24@gmail.com
#Mr. Dotun
#print out the purpose of the program

# ("a menu based program")
print ('WELCOME TO ARC_HUB MOBILE ENTERPRISE ')
print ('HOME FOR ALL DATA & CABLE SUBSCRIPTIONS\n  (where we offer quality data services with best offers you can afford)\n      Thanks for contacting us.')
print ('How may we be of service to you?\nKindly select the options below for us to serve you better.\n')

Order_Request = input('Order Request: \n Data \n VTU \n Pay Bills\n')

if Order_Request == 'Data':
    print ('Proceed to  data selection')
    
elif Order_Request == 'VTU':
    print ('Currently unavailable')
    
else:
    print ('Data access denied, pls check your connection.')

Data_selection = input ('Select Data: \n MTN  \n Airtel \n GLO \n ETISALAT\n')

if Data_selection == 'MTN':
    print ('Select a Data size')
    MTN_Data = input ('Available Data: \n(a) 1gb = N750 \n(b) 2gb = N1300 \n(c) 5gb = N3000\n')
    if MTN_Data == 'a':
            print ('Proceed to Payment')
    else:
            print ('Proceed to Payment')
            
elif Data_selection == 'Airtel':
    print ('Select from below')
    Airtel_Data = input ('Available Data: \n(a) 1.5gb = N1000 \n(b) 3.5gb = N1500 \n(c) 7gb = N3500\n')
    if Airtel_Data =='a':
            print ('Proceed to Payment')
    else:
            print ('Proceed to Payment')
            
elif Data_selection == 'GLO':
    print ('make a selection')
    GLO_Data = input ('Available Data: \n(a) 2gb = N1000 \n(b) 8.5gb = N3000\n')
    if GLO_Data =='a':
            print ('Proceed to Payment')
    elif GLO_Data == 'b':
           print ('Proceed to Payment') 
    else:
            print ('Choose a valid option')
            
else:
        print ('select from the price range')
        ETISALAT_Data = input ('Data Price: \n(a) 1gb = N850 \n(b) 5gb = N3400\n')
        if ETISALAT_Data == 'a':
            print ('Proceed to make Payment')
        else:
            print ('Make Payment')

        
PAYMENT_OPTIONS = input ('Payment Options: \n (1) ATM/WALLET \n (2) Internet/Online Banking \n (3)Cash Deposit\n')

if PAYMENT_OPTIONS == '1':
        print ('Payment received. Transaction Processing......')
elif PAYMENT_OPTIONS == '2':
        print ('Please wait while your Transaction is processing.......')
else:
        print ('Waiting for message alert from your bank while your transaction is been processed')

print ('Transaction Successful. \n Thank you For choosing ARC_HUB MOBILE ENTERPRISE. \n  Have a good day!\n')        
     
