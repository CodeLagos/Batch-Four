#Health system diagnostic program
print("Health system diagnostic program")
name=input("Please enter your name:\n")
dio=input(" For full diagnosis press 1: \n For quick diagnosis press 2: \n")
if dio=='2':
    print("Start your selection from top to bottom")
    print("Please select four(4) options/sympthoms")
    print("Please select all options at once adding a cormer(,)after your option e.g a,b,c. \n")
    Sympthoms=input(" CHOOSE YOUR SYMPTHOMS:  \n (a) Headache\Body pain \n (b) fatigue \n (c) vomiting\Loss of Appetite \n (d) diarrhoea\n (e) weakness\Sweating \n (f) heart burn \n (g) chest and abdomen pain \n (h) non healing sore \n (i) lump in the breast \n (j) nausea \n ")
    if Sympthoms.lower()=="a,b,c,e,j":
        print(name," you have malaria")
        print("TREATMENT:AMALA TAB or ATHESONATE TAB")
        print("If symthoms persist after the drug usage, Please consult your doctor")
        print("Thanks for your patronage")
    elif Sympthoms.lower()=="a,b,c,d,j":
        print(name," You have typhoid")
        print("TREATMENT: ")
        print("If symthoms persist after the drug usage, Please consult your doctor")
        print("Thanks for your patronage")
    elif Sympthoms.lower()=="a,h,i":
        print(name,"you have breast cancer")
        print("TREATMENT: ")
        print("If symthoms persist after the drug usage, Please consult your doctor")
        print("Thanks for your patronage")
    elif Sympthoms.lower()=="f,g":
        print(name," you have stomach alcer")
        print("TREATMENT:  ")
        print("If symthoms persist after the drug usage, Please consult your doctor")
        print("Thanks for your patronage")
    else:
        print("Please take full diagnosis")
        print("Please answer all questions with yes or no\n")
        print("Do you have up to four or more of this sympthoms?")
        mal=input("(1) Body pain \n (2) Migrine \n (3) Shaking chills \n (4) Sweating \n (5) Nausea \n (6) Aches \n (7) Cytopenia \n") 
        if mal.lower()=='yes':
            print(name,"you have malaria")
            print("TREATMENT:AMALA TAB or ATHESONATE TAB")
            print("If symthoms persist after the drug usage, Please consult your doctor")
            print("Thanks for your patronage")
        elif mal.lower()=="no":
            print("Do you have up to four or more of this sympthoms?")
            Ty=input("(1) Vomiting \n (2) Loss of Appetite \n (3) Fatigue \n (4) Headache \n (5) Rash \n (6) Diarrhoea \n (7) Cholera \n (8) stomach pain \n (9) Constipation \n ")
            if Ty.lower()=='yes':
                print(name," you have Typhiod")
                print("Consult your doctor")
            elif Ty.lower()=='no':
                print("Do you have up to four or more of this sympthoms?")
                BC=input("(1) Lump in the breast \n (2) Inverted nipple  \n (3) Discomfort \n (4) Redness or swallen lymphnodes \n (5) Non healing sore \n (6) Blood in the Urine  \n (7) Unexplaind anemia \n (8) Headache \n (9) Hoarseness \n ")
                if BC.lower()=='yes':
                    print(name," you have Breast Cancer")
                    print("Consult your doctor")
                elif BC.lower()=="no":
                    print("Do you have up to four or more of this sympthoms?")
                    SU=input("(1) Pain in the cheast \n (2) Weight loss \n (3) Bloating \n (4) Burping \n (5) Nausea \n (6) Heart burn \n")
                    if SU.lower()=='yes':
                        print(name," you have Stomach Ulcer")
                        print("Consult your doctor")
                    elif SU.lower()=="no":
                        print(" Please see your doctor")
                    else:
                        print("Invalid input\n please input yes or no")
                else:
                    print("Invalid input \n please input yes or no")
            else:
                print("Invalid input\n please input yes or no ")
        else:
            print("Invalid input\n please input yes or no")
elif dio=='1':
    print("Please take full diagnosis")
    while True:
        print("Please answer all questions with yes or no\n")
        print("Do you have up to four or more of this sympthoms?")
        mal=input("(1) Body pain \n (2) Migrine \n (3) Shaking chills \n (4) Sweating \n (5) Nausea \n (6) Aches \n (7) Cytopenia \n") 
        if mal.lower()=='yes':
            print(name," you have malaria.")
            print("TREATMENT:AMALA TAB or ATHESONATE TAB")
            print("If symthoms persist after the drug usage, Please consult your doctor")
            print("Thanks for your patronage")
        elif mal.lower()=="no":
            print("Do you have up to four or more of this sympthoms?")
            Ty=input("(1) Vomiting \n (2) Loss of Appetite \n (3) Fatigue \n (4) Headache \n (5) Rash \n (6) Diarrhoea \n (7) Cholera \n (8) stomach pain \n (9) Constipation \n ")
            if Ty.lower()=='yes':
                print(name," you have Typhiod")
                print("TREATMENT: ")
                print("If symthoms persist after the drug usage, Please consult your doctor")
                print("Thanks for your patronage")
            elif Ty.lower()=='no':
                print("Do you have up to four or more of this sympthoms?")
                BC=input("(1) Lump in the breast \n (2) Inverted nipple  \n (3) Discomfort \n (4) Redness or swallen lymphnodes \n (5) Non healing sore \n (6) Blood in the Urine  \n (7) Unexplaind anemia \n (8) Headache \n (9) Hoarseness \n ")
                if BC.lower()=='yes':
                    print(name," you have Breast Cancer")
                    print("TREATMENT: ")
                    print("If symthoms persist after the drug usage, Please consult your doctor")
                    print("Thanks for your patronage")
                elif BC.lower()=="no":
                    print("Do you have up to four or more of this sympthoms?")
                    SU=input("(1) Pain in the cheast \n (2) Weight loss \n (3) Bloating \n (4) Burping \n (5) Nausea \n (6) Heart burn \n")
                    if SU.lower()=='yes':
                        print(name," you have Stomach Ulcer")
                        print("TREATMENT: ")
                        print("If symthoms persist after the drug usage, Please consult your doctor")
                        print("Thanks for your patronage")
                    elif SU.lower()=="no":
                        print(" Please see your doctor")
                    else:
                        print("Invalid input\n")
                else:
                    print("Invalid input\n")
            else:
                print("Invalid input\n")
        else:
            print("Invalid input\n")

        if input("Do you want to run this diagonsis again\n yes or no\n")=="yes":
            continue
        else:
            print("Good bye")
            break;
