#NAME:PRAISE E. ANEGBE
#COURSE:PYTHON PROGRAMMING
#PROJECT TITLE:HUMAN MEDICAL GENOTYPE CHART FOR INTENDING COUPLES
#INSTITUTION:CODE_LAGOS 18'
#CENTRE:ONIKAN YOUTH CENTRE, LAGOS ISLAND, LAGOS STATE, NIGERIA
#BATCH:'4' (AFTERNOON SESSION)
#DATE PRESENTED:12/09/2018

#Human genotype known are: AA, AS, SS, SC and CC
#Let 'y' represent the Male gender and 'x' to represent the Female gender.
y= (input("Genotype Male"))
x= (input("Genotype Female"))

if(y=="AA" and x=="AA"):
    print("Can Marry")

elif(y=="AA" and x=="AS"):
    print("Can Marry")

elif(y=="AS" and x=="AS"):
    print("Not Advised to Marry")

elif(y=="SS" and x=="AA"):
    print("Can Marry")

elif(y=="SS" and x=="SS"):
    print("Not Advised to Marry")

elif(y=="SC" and x=="CC"):
    print("Not Advised to Marry")

elif(y=="AS" and x=="SC"):
    print("Not Advised to Marry")

elif(y=="AS" and x=="SS"):
    print("Not Advised to Marry")

elif(y=="AS" and x=="CC"):
    print("Not Advised to Marry")
    
elif(y=="AA" and x=="SC"):
    print("Can Marry")

elif(y=="AA" and x=="CC"):
    print("Can Marry")

elif(y=="AA" and x=="SS"):
    print("Can Marry")

else:
    print("Please Consult your Medical Doctor for advise and other possible option")
    
