#NAME: OKWUMBU CHUKWUDI DAVID
#SUPERVISOR: MR IDRIS
#EMAIL: chuxdave1307@gmail.com
#CONTACT: 08160767651

#PROJECT ON CBT FOR UNIVERSITY OF LAGOS (FACULTY OF ENVIRONMENTAL SCIENCE) (Msc Construction Management) 



print('                   (CODE LAGOS 4 PROJECT)  \n\n')






        #*************UNIVERSITY OF LAGOS*****************#
 
print('                    UNIVERSITY OF LAGOS                ')
print('              FACULTY OF ENVIRONMENTAL SCIENCE            ')
print('                Msc CONSTRUCTION MANAGEMENT            ')
print('                  CBT EXAMINATION 2018/2019              \n \n')

import time
import datetime


print('DATE:',datetime.datetime.now().strftime("%y-%m-%d\nTIME: %H:%M \n \n"))




#Those that are registered are allowed to partake in this entrance exam.
#LOGIN with your REGISTRATION NUMBER.
#If your REGISTRATION NUMBER is correct, it will display your personal details.
#You are given only 5 attempt to enter the correct REGISTRATION NUMBER.
#If you enter the WRONG REGISTRATION NUMBER, you wont be able to write this exam.
#All candidates has various TYPE, Therefore ensure you choose the type you are answering in the space provided
#Answer all questions,each questions carries 10 marks.
#Your total score will be diplayed once you are done with the exam.

#GOODLUCK!


for i in range (5):
    regnum=input('               ENTER REGISTRATION NUMBER  :  ' )
    if regnum== ('179052047') :
       
        print('CANDIDATE NAME: OKWUMBU CHUKWUDI DAVID')
        print('EXAMINATION NO: 179052047')
        print('SEX           : MALE')
        print('EXAM CENTRE   : CBT HALL')
        print('TIME ALLOWED   : 30 MINS \n \n')
        print('INSTRUCTIONS FOR CANDIDATES: Make sure you read all questions carefully before choosing your options letter A-D on the keyboard.\n\n')
        print('                         TYPE A \n\n')
        print('CHOOSE THE WORDS THAT BEST COMPLETES EACH OF THE FOLLOWING SENTENCES.\n\n')
        
       
    
        #Initialize the score variable
        score=10
        Question1=input('(1) What type are you answering.......\n (a) TYPE A \n (b) TYPE B \n (c) TYPE C \n (d) TYPE D \n ')
        if (Question1.lower()=='a'):
            print(' ')
            score=score + 0
        else:
            print(' ')
            score = (score + 0)-10
        Question2=input('(2) Fredrick taylor introduced a system of working known as......... \n (a) Line organisation \n (b)Line and staff organisation \n (c) functional orgnisation \n (d) effective organisation \n ')
        if (Question2.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question3=input('(3)Final technical authority of a project lies with ..........\n (a) Assistant Engineer \n (b) Executive Engineer \n (c) Chief Engineer \n (d) Supervisor \n ')
        if (Question3.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question4=input('(4) The performamce of task in CPM is known as......... \n (a) Dummy \n (b) Event \n (c) Activity \n (d) Contract \n')
        if (Question4.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question5=input('(5) Completion of an activity on CPM network diagram is generally known as......... \n (a) Event \n (b) node \n (c) connector \n (d) All of the above \n')
        if (Question5.lower()=='d'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question6=input('(6) Various activities of a project are shown on a bar chart by.......... \n (a) vertical lines \n (b) horizontal lines \n (c) dots \n (d) crosses \n')
        if (Question6.lower()=='b'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question7=input('(7) Time and progress chart of construction is also known as...... \n (a) Bar Chartt \n (b) Gantt Chart \n (c) Critical path method \n (d) All of the above \n')
        if (Question7.lower()=='d'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question8=input('(8) Henry Gantt developed Bar Chart for planning and scheduling of project in......\n (a) 1880 \n (b) 1900 \n (c) 1920 \n (d) 1940 \n')
        if (Question8.lower()=='b'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question9=input('(9) Construction team means......... \n (a) An Engineer \n (b)An Architect \n (c) A Client \n (d) All of the above \n')
        if (Question9.lower()=='d'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question10=input('(10) The estimated time required to perform an activity is known as \n (a) Event \n (b) dummy \n (c) duration \n (d) float \n')
        if (Question10.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        print('Total score =' , score)
        if score==100:
            print('EXCELLENT\nCONGRATULATIONS YOU HAVE BEEN PROVISIONALLY ADMITTED')
        elif score==80:
            print('VERY GOOD\nCONGRATULATIONS YOU HAVE BEEN PROVISIONALLY ADMITTED')
        elif score==60:
            print('GOOD\nNOT ADMITTED')
        elif score==50:
            print('PASS\nNOT ADMITTED')
        elif score<50:
            print('BAD\nNOT ADMITTED')
        break

    elif regnum== ('179052048'):
        

        print('CANDIDATE NAME: OPALEYE LUKMAN')
        print('EXAMINATION NO: 179052048')
        print('SEX           : MALE')
        print('EXAM CENTRE   : CBT HALL')
        print('TIME ALLOWED   : 30 MINS \n \n')
        print('INSTRUCTIONS FOR CANDIDATES: Make sure you read all questions carefully before choosing your options letter A-D on the keyboard.\n\n')
        print('                         TYPE B \n\n')
        print('CHOOSE THE WORDS THAT BEST COMPLETES EACH OF THE FOLLOWING SENTENCES.\n\n')
           
        
        #Initialize the score variable
        score=10
        Question1=input('(1) What type are you answering.......\n (a) TYPE A \n (b) TYPE B \n (c) TYPE C \n (d) TYPE D \n ')
        if (Question1.lower()=='b'):
            print(' ')
            score=score + 0
        else:
            print(' ')
            score = (score + 0)-10
        Question2=input('(2) Completion of an activity on CPM network diagram is generally known as......... \n (a) Event \n (b) node \n (c) connector \n (d) All of the above \n')
        if (Question2.lower()=='d'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question3=input('(3) Henry Gantt developed Bar Chart for planning and scheduling of project in......\n (a) 1880 \n (b) 1900 \n (c) 1920 \n (d) 1940 \n')
        if (Question3.lower()=='b'):
            print(' ')
            score=score + 10
        else:
            print(' ')
        Question4=input('(4) The performamce of task in CPM is known as......... \n (a) Dummy \n (b) Event \n (c) Activity \n (d) Contract \n')
        if (Question4.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question5=input('(5) The estimated time required to perform an activity is known as \n (a) Event \n (b) dummy \n (c) duration \n (d) float \n')
        if (Question5.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
        Question6=input('(6) Fredrick taylor introduced a system of working known as......... \n (a) Line organisation \n (b)Line and staff organisation \n (c) functional orgnisation \n (d) effective organisation \n ')
        if (Question6.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question7=input('(7) Construction team means......... \n (a) An Engineer \n (b)An Architect \n (c) A Client \n (d) All of the above \n')
        if (Question7.lower()=='d'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question8=input('(8) Time and progress chart of construction is also known as...... \n (a) Bar Chartt \n (b) Gantt Chart \n (c) Critical path method \n (d) All of the above \n ')
        if (Question8.lower()=='d'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question9=input('(9)Final technical authority of a project lies with ..........\n (a) Assistant Engineer \n (b) Executive Engineer \n (c) Chief Engineer \n (d) Supervisor \n ')
        if (Question9.lower()=='c'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        Question10=input('(10) Various activities of a project are shown on a bar chart by.......... \n (a) vertical lines \n (b) horizontal lines \n (c) dots \n (d) crosses \n')
        if (Question10.lower()=='b'):
            print(' ')
            score=score + 10
        else:
            print(' ')
            score= (score + 10)-10
        print('Total score =' , score)
        if score==100:
            print('EXCELLENT\nCONGRATULATIONS YOU HAVE BEEN PROVISIONALLY ADMITTED')
        elif score==80:
            print('VERY GOOD\nCONGRATULATIONS YOU HAVE BEEN PROVISIONALLY ADMITTED')
        elif score==60:
            print('GOOD\nNOT ADMITTED')
        elif score==50:
            print('PASS\nNOT ADMITTED')
        elif score<50:
            print('BAD\nNOT ADMITTED')
        break



    
        
    else:
        print('                                         Incorrect Registration Number')
    
      
else:
    print('WRONG REGISTRATION NUMBER, Sorry this exam is not for you!')

    




