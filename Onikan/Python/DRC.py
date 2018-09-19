
#Ogunnowo Oluwaseye
import datetime
print ("This is a Disease Reference Catalogue (DRC) program. In order to recieve a preliminary diagnosis on any possible infection or disease that you may have, using this software, you must answer all questions asked honestly and provide truthfull information")
print ("Disclaimer: This is by NO means, a complete diagnosis. Suspected illnesses should be sufficiently tested for at an accreddited hospital. However, this reference program can provide you with professional information.")
print (" ")
print (" ")
print (" ")
name=input("What's your full name?")
age=input("Alright, how old are you?")
kg=float(input("What do you weigh in kilogramms, please type only numbers"))
visit=input("Have you visited the hospital recently?: Type Y for yes and N for no ")
if (visit=='y' or visit=='Y'):
    hos=input("What is the name of the Hosptial?")
print (" ")
print (" ")
print ("!!!INSTRUCTION: In this section, provide truthfull answers as to whether you have encountered the following symptoms recently and other necessary queries. Don't answer blindly, read the questions well. Let all replies here be in LOWER CASE")
print (" ")
print (" ")
a1=input("Are you coughing? Type Y for Yes and N for No")
a2=input("If you said yes, has your coughing occurred for a long time now? If you said no, ignore this question. Type Y for Yes and N for No")
ax=input("Again, if you agreed to have cough, do you cough up mucus? If you disagreed, ignore this question. Type Y for Yes and N for No")
az=input("if you agreed to cough up mucus: is the colour green (Type g), yellow (y) or red (r)? If you disagreed or ignored that question, ignore this question aswell." )
a3=input("Do you experience any one of these:sorethroat, runny or blocked nose, loss of taste? Type Y for yes and N for No")
a4=input("Do you have headaches? Type Y for Yes and N for No")
a5=input("Do you have joint aches? Type Y for Yes and N for No")
a6=input("Do you have body aches? Type Y for Yes and N for No")
a7=input("Feel the sides of your neck. Do you have an elevated temperature? Type Y for Yes and N for No")
a8=input("Are you vomiting? Type Y for Yes and N for No")
a9=input("Have you suddenly started visiting the toilet more often? Type Y for Yes and N for No")
a10=input("Is your excrement (poo) watery or slimier than usual? Type Y for Yes and N for No")
a10x=input("If you agreed that your excrement is watery, do you find blood stains on your excrement or is it generally reddy? If you disagreeg, ignore this. Type Y for Yes and N for No")
a11=input("Do you have stomach aches? Type Y for Yes and N for No")
a12=input("Have you fainted recently? Type Y for Yes and N for No")
a13=input("Have you experienced sudden weight loss? Type Y for Yes and N for No")
a14=input("Do you have night sweats? Type Y for Yes and N for No")
a15=input("Look at you palms, are they rinkled? Type Y for Yes and N for No")
a16=input("Have you lost your apetite? Type Y for Yes and N for No")
a17=input("Do you feel excessively thirsty? Type Y for Yes and N for No")
a18=input("Are your eyes or skin yellow? Type Y for Yes and N for No")
a19=input("Are you experiencing dizziness? Type Y for Yes and N for No")
a20=input("Do you feel a pounding sensation in your head or chest? Type Y for Yes and N for No")
a23=input("Do you have chest pain Type Y for Yes and N for No")
a21=input("Do you often need to sit down? Type Y for Yes and N for No")
a22=input("Do you have difficulty breathing? Type Y for Yes and N for No")

print (" ")
print (" ")
print (" ")
print (" ")
print (" ")

print("Alright",name+", you lkely have one or more of the following: ")
print (" ")
if (a1=='y' and a3=='y' and ax=='y' or ax=='g' or ax=='y'):
    print ("> Cold")
if (a4=='y' and a7=='y') or (a4=='y' and a7=='y' and a14=='y') or (a4 and a7 and a5=='y'):
    print ("> Malaria")
if (a4=='y' and a5=='y' and (a7=='y' or a8=='y' or a6=='y')):
    print ("> Dengue Fever")
if (a1=='y' and a3=='y' and ax=='y' and az=='r' and (a2=='y' or a22=='y' or a23=='y')):
    print ("> Tuberculosis")
if (a15=='y' and a10=='y' and a9=='y'):
    print ("> Cholera")
if (a18=='y' and a7=='y') or (a18=='y' and a7=='y' and a8=='y' and (a5=='y' or a6=='y') and a16=='y'):
    print ("> Yellow Fever")
if (a9=='y' and a10=='y' and (a4=='y' or a7=='y' or a13=='y' or a8=='y' or a11=='y' or a16=='y') and a17=='y'):
    print ("> Food Poisoning")
if (a9=='y' and a10=='y' and (a4=='y' or a7=='y' or a13=='y' or a8=='y' or a11=='y' or a16=='y') and a17=='y' and a10x=='y'):
    print ("> Dysentry")
if (a19=='y' and a21=='y' and (a21=='y' or a22=='y')):
    print ("> Symptoms of elevated blood pressure")
if (a19=='y' and a21=='y' and (a21=='y' or a22=='y' and a12)):
    print ("> Symptoms associated with Hypertension")
if ((a7=='y' or a4=='y' or a8=='y' or a9=='y' or a10x=='y' or a6=='y' and a11=='y' and a10=='y')):
    print ("> Typhoid Fever")
if (a1=='y' or a3=='y' or ax=='y' and az=='y' or az=='g' and a23=='y'):
    print ("> Pneumonia")
else:
    print ("Error, your result is inconclusive. This may mean that your illness is not recognized in the database or you may be experiencing normal syptoms of allergy or general fatigue, or tiredness or you did not agree to any symptoms")

print ("This is your preliminary diagnosis")
print ("                                               ")
print (" ")
print ("...................................................................................................................................................")
print ( "======================================================MEDICAL REPORT=========================================================================")
print ("This report can be printed out and included an in email. It should be handled by your doctor.")
print (" ")
dt= datetime.datetime.now()
print ("Date and time:",(dt))
print (" ")
print ("Patnent's Name:",name)
print ("Patient's Age:",age)
print ("Patient's Weight:",kg,"kg")
if (visit=='y' or visit=='Y'):
    print ("Recent Hospital Visits: Yes")
if (visit=='n' or visit=='N'):
    print ("Recent Hospital Visits: None")
if (visit=='y' or visit=='Y'):
    print ("Name of Hospital:",hos)
print (" ")
print (" ")
print (" ")
print ("SYMPTOMS EXPERIENCED")
if (a1=='y'):
    print ("- Cough")
if (a2=='y'):
    print ("- Cough is prolonged")
if (a1=='y' and ax=='y'):
    print ("- Expectoration")
if (a1=='y' and ax=='y' and az=='r'):
    print ("- Prolonged coughing with expectoration of blood stained sputum")
if (a1=='y' and ax=='y' and az=='g'):
    print ("- Prolonged coughing with expectoration of green sputum")
if (a1=='y' and ax=='y' and az=='y'):
    print ("- Prolonged coughing with expectoration of yellow sputum")
if (a3=='y'):
    print ("- Inflammatory response symptoms")
if (a4=='y'):
    print ("- Headache")
if (a5=='y'):
    print ("- Joint aches")
if (a6=='y'):
    print ("- Body aches")
if (a7=='y'):
    print ("- High temperature")
if (a8=='y'):
    print ("- Vomiting")
if (a9=='y'):
    print ("- Diarrhoea")
if (a9=='y' and a10=='y'):
    print ("- Watery diarrhoea")
if (a9=='y' and a10=='y' and a10x=='y'):
    print ("- Blood stained diarrhoea")
if (a11=='y'):
    print ("- Stomach aches")
if (a12=='y'):
    print ("- Fainting")
if (a13=='y'):
    print ("- Weight loss")
if (a14=='y'):
    print ("- Night sweats")
if (a15=='y'):
    print ("- Wrinkled skin")
if (a16=='y'):
    print ("- Loss of apetitie")
if (a17=='y'):
    print ("- excessive thirst")
if (a18=='y'):
    print ("- Jaundice")
if (a19=='y'):
    print ("- Diziness")
if (a20=='y'):
    print ("- Pounding sensation in head and/or chest")
if (a21=='y'):
    print ("- Fatigue")
if (a22=='y'):
    print ("- Difficulty breathing")

print (" ")
print (" ")
print ("PRELIMINARY DIAGNOSIS")
print ("Combination of one or more of: ")
print (" ")
if (a1=='y' and a3=='y' and ax=='y' and ax=='g' or ax=='y'):
    print ("- Cold")
if (a4=='y' and a7=='y') or (a4=='y' and a7=='y' and a14=='y') or (a4 and a7 and a5=='y'):
    print ("- Malaria")
if (a4=='y' and a5=='y' and (a7=='y' or a8=='y' or a6=='y')):
    print ("- Dengue Fever")
if (a1=='y' and a3=='y' and ax=='y' and az=='r' and (a2=='y' or a22=='y' or a23=='y')):
    print ("- Tuberculosis")
if (a15=='y' and a10=='y' and a9=='y'):
    print ("- Cholera")
if (a18=='y' and a7=='y') or (a18=='y' and a7=='y' and a8=='y' and (a5=='y' or a6=='y') and a16=='y'):
    print ("- Yellow Fever")
if (a9=='y' and a10=='y' and (a4=='y' or a7=='y' or a13=='y' or a8=='y' or a11=='y' or a16=='y') and a17=='y'):
    print ("- Food Poisoning")
if (a9=='y' and a10=='y' and (a4=='y' or a7=='y' or a13=='y' or a8=='y' or a11=='y' or a16=='y') and a17=='y' and a10x=='y'):
    print ("- Dysentry")
if (a19=='y' and a21=='y' and (a21=='y' or a22=='y')):
    print ("- Symptoms of elvated blood pressure")
if (a19=='y' and a21=='y' and (a21=='y' or a22=='y' and a12)):
    print ("- Symptoms associated with Hypertension")
if ((a7=='y' or a4=='y' or a8=='y' or a9=='y' or a10x=='y' or a6=='y' and a11=='y' and a10=='y')):
    print ("- Typhoid Fever")
if (a1=='y' or a3=='y' or ax=='y' and az=='y' or az=='g' and a23=='y'):
    print ("- Pneumonia")
else:
    print ("Error, the result was inconclusive. This may mean that your illness is not recognized in the database or you may be experiencing normal syptoms of allergy or general fatigue, or tiredness, or you have no symptoms")


print (" ")
print (" ")
print ("SUGGESTED TREATMENT")
print (" ")
print ("All medications should be used under doctor's supervision")
print (" ")
if (a1=='y' and a3=='y' and ax=='y' and ax=='g' or ax=='y'):
    print ("- Bed rest, Cough Syrup, Piriton, Piriton Exppectorant, Strepsils, Lozenges, Vitamin C.")
if (a4=='y' and a7=='y') or (a4=='y' and a7=='y' and a14=='y') or (a4 and a7 and a5=='y'):
    print ("- Antimalarial: Glomether injections or Lonart tablets, Quinin IV, PCM injections")
if (a4=='y' and a5=='y' and (a7=='y' or a8=='y' or a6=='y')):
    print ("- Ibuprofen, PCM injections, fluid replacement")
if (a1=='y' and a3=='y' and ax=='y' and az=='y' and (a2=='y' or a22=='y' or a23=='u')):
    print ("- Antibiotics and antituberculars: Streptomycin, Rifampicin etc. Bed rest ")
if (a15=='y' and a10=='y' and a9=='y'):
    print ("- Fluid replacement, antibiotics: Levofloxacin, Tetracycline etc.")
if (a18=='y' and a7=='y') or (a18=='y' and a7=='y' and a8=='y' and (a5=='y' or a6=='y') and a16=='y'):
    print ("- Currently no cure for Yellow Fever if found. Ibuprofen, PCM injections, Oral Rehydration")
if (a9=='y' and a10=='y' and (a4=='y' or a7=='y' or a13=='y' or a8=='y' or a11=='y' or a16=='y') and a17=='y'):
    print ("- Antibiotics: Levofloxacin, Oral rehydration")
if (a9=='y' and a10=='y' and (a4=='y' or a7=='y' or a13=='y' or a8=='y' or a11=='y' or a16=='y') and a17=='y' and a10x=='y'):
    print ("- Antibiotics: Levofloxacin, Oral rehydration")
if (a19=='y' and a21=='y' and (a21=='y' or a22=='y')):
    print ("- Diuretics, Beta blockers, Renin inhibitors")
if (a19=='y' and a21=='y' and (a21=='y' or a22=='y' and a12)):
    print ("- Diuretics, Beta blockers, Renin inhibitors")
if ((a7=='y' or a4=='y' or a8=='y' or a9=='y' or a10x=='y' or a6=='y' and a11=='y' and a10=='y')):
    print ("- Amoxicillin, Levofloxacin, IV rehydration if needed")
if (a1=='y' or a3=='y' or ax=='y' and az=='y' or az=='g' and a23=='y'):
    print ("- Antibiotics: Penicillin, Oral rehydration")
else:
    print ("No treatment required")
    
print (" ")
print (" ")
print ("This program is a copyright of Seye, created with Python vs. 3.6.5, 2018")


    








        






