#Aworinde kolawole David
#Kolawole96@yahoo.com
#Electricity bill calculator
#Rexben

#A programm to determine an estimate for electricity bill per month
#this prototype for estimating electricity bill can be further improved by more research to obtain reasonable value for result
#also more appliances could be added to meet all client needs and improve on accuraccy of result obtainable.

#This programm take the user through all variables that are needed to calculate thier electricity bill,
#it is expected that the user provides accurate data to enable better result during use,
#The user is asked to provide avarage electricity availability per day (in hours),
#the user is further taken through common home appliances in which they are expected to enter the number of these appliance they use
#the electricity consumeed for the month is automatically calculated in kilowatt per hour (Kwh)
#The programm prompt the user to select the electricity district responsible for billing
#lastly select house category, if user's house is not in an estate it falls underthe bungalow category.
#the total bill is calculated automatically
#user advised to follow instructions carefully to enable smooth and easy use
#THANKS to you all

while True:
    try:
#prompt user to enter to number of average availability of electricity daily in hours         
        electric=int(input('please enter the average hours of electricity availability per day.....:'))
        totalelectric=electric*30  
#prompt user to enter number of appliance being user and average hours of usage for some appliannce
        
        def TV(Tvwatt,n):
            return (Tvwatt*n)    
        Tvwatt=57
        n=int(input('please enter number of Tvs you use:'))
        Tv=Tvwatt*n
      
        def AC(radwatt,n):
            return (radwatt*n)
        radwatt=1000
        n=int(input('please enter number of Ac you use:'))
        Ac=radwatt*n
        
        def ref(refwatt,n):
            return (refwatt*n)
        refwatt=250
        n=int(input('please enter number of refigerators you use:'))
        Refrigerator=refwatt*n

        def waterpump(wpwatt,n):
            return (wpwatt*n)
        wpwatt=300
        n=int(input('please enter number of pumping machine you use:'))
        p=int(input('please enter your average use in hours of this appliance per month:'))
        Pm=(wpwatt*n*p)

        def washm(rwmwatt,n):
            return (wmwatt*n)
        wmwatt=500
        n=int(input('please enter number of washing machine you use:'))
        p=int(input('please enter your average use in hours of this appliance per month:'))
        Wm=(wmwatt*n*p)

        def iron(irwatt,n):
            return (irwatt*n)
        irwatt=1000
        n=int(input('please enter number of irons you use:'))
        p=int(input('please enter your average use in hours of this appliance per month:'))
        Iron=(irwatt*n*p)

        def blender(bldwatt,n):
            return (blwatt*n)
        blwatt=300
        n=int(input('please enter number of blenders you use:'))
        blend=blwatt*n

        def kettle(ekwatt,n):
            return (ekwatt*n)
        ekwatt=1200
        n=int(input('please enter number of Electric kettle/water heater you use:'))
        p=int(input('please enter your average use in hours of this appliance per month:'))
        Kettle=(ekwatt*n*p)

        def fan(fanwatt,n):
            return (fanwatt*n)
        fanwatt=25
        n=int(input('please enter number of fans you use:'))
        Fan=fanwatt*n

        def microwave(mvwatt,n):
            return (mvwatt*n)
        mvwatt=600
        n=int(input('please enter number of microwave ovens you use:'))
        p=int(input('please enter your average use in hours of this appliance per month:'))
        Micro=(mvwatt*n*p)        

        def charger(chwatt,n):
            return (chwatt*n)
        chwatt=15
        n=int(input('please enter number of chargers you use:'))
        Charger=chwatt*n
        
        def Bulb(bbwatt,n):
            return (bbwatt*n)
        bbwatt=26
        n=int(input('please enter number of bulbs you use:'))
        bulb=bbwatt*n
        
        def speakers(sdwatt,n):
            return (sdwatt*n)
        sdwatt=75
        n=int(input('please enter number of sound systems you use:'))
        soundsystem=sdwatt*n

#calculating the total rating in kwh for rarely used appliance
        def rare():
            return (rarekwh)
        rarekwh=((Pm+Wm+Iron+Kettle+Micro)*60)/1000
        
#calculating the total sum of appliance rating in watts
        total=(Tv)+(Ac)+(Refrigerator)+(blend)+(Fan)+(Charger)+(bulb)+(soundsystem)
        print(total)
#coverting total value to kilowatt per hour (kwh)        
        kwh=((total*60)/1000)*electric
#calculating the total consumption in kwh per month        
        consumed=round((rarekwh+kwh),2)
        print('you consumed',consumed,'kwh of electricity this month')
      
#prompt user to select electricity district
#prompt user to select house category        
        location=int(input('select your electricity district\n1. Abuja(ABEDC)\n2. Benin(BEDC)\n3. Enugu(ENEDC)\n4. Ibadan(IBEDC)\n5. Jos(JEDC)\n6. Kaduna(KEDC)\n7. Kano(KEDC)\n8. Ikeja(IE)\n9. Ph(PEDC)\n10. Eko(EKEDC)\nResponse:'))
        if location==1:         
            houseType=int(input('(ABEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(24.3*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                Estate=round(46.23*consumed,2)
                print('your electricity bill for this month is NGN',Estate,)
        elif location==2:
            houseType=int(input('(BEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(24.08*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(38.56*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        elif location==3:      
            houseType=int(input('(ENEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(27.13*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(45.4*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        elif location==4:      
            houseType=int(input('(IBEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==4:
                bungalow=round(23.09*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(41.31*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        elif location==5:      
            houseType=int(input('(JEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(26.93*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(43.9*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        elif location==6:      
            houseType=int(input('(KDEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(26.37*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(44.5*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        elif location==7:      
            houseType=int(input('(KEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(20.26*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(38.38*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        elif location==8:      
            houseType=int(input('(IE) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(21.3*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(36.49*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        elif location==9:      
            houseType=int(input('(PHEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(24.9*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(48.35*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
        else:
            location==10     
            houseType=int(input('(EKEDC) please select the type of house you live in\n1. Bungalow\n2. Estate\nResponse: '))    
            if houseType==1:
                bungalow=round(24*consumed,2)
                print('your electricity bill for this month is NGN',bungalow,)
            else:
                 Estate=round(39*consumed,2)
                 print('your electricity bill for this month is NGN',Estate,)
                 break
    except ValueError as e:        
        print('please input whole number')
        print(e)
    except NameError as c:
        print('please input whole number')
        print(c)
