#emyokwumbu@gmail.com

def questions():
     #Initialize the score variable
        score=20
        Question1=input('(1) The new book has beautiful.........which make it attractive\n (a) illustrations \n (b) demonstrations \n (c) illuminations \n (d) compositions \n ')
        if (Question1.lower()=='c'):
            print(' ')
            score=score + 0
        else:
            print(' ')
            score = (score + 0)-20
        Question2=input('(2) At christmas, employees of the sugar factory receives huge........ \n (a) benefit \n (b) dividends \n (c) bonuses \n (d) salaries \n ')
        if (Question2.lower()=='c'):
            print(' ')
            score=score + 20
        else:
            print(' ')
            score= (score + 20)-20
        Question3=input('(3)At the end of the ........, the National Anthem is played on our radio station \n (a) programming \n (b) sproduction \n (c) transition \n (d) transmission \n ')
        if (Question3.lower()=='c'):
            print(' ')
            score=score + 20
        else:
            print(' ')
            score= (score + 20)-20
        Question4=input('(4) Their marriage was finally ........after years of hostility. \n (a) cancelled \n (b) annulled \n (c) broken \n (d) separated \n')
        if (Question4.lower()=='a'):
            print(' ')
            score=score + 20
        else:
            print(' ')
            score= (score + 20)-20
        Question5=input('(5) Not all activists champion........causes. \n (a) uworthy \n (b) real \n (c) concrete \n (d) favourable \n')
        if (Question5.lower()=='b'):
            print(' ')
            score=score + 20
        else:
            print(' ')
            score= (score + 20)-20
        print('Total score =' , score)
        if score==100:
            print('EXCELLENT')
        elif score==80:
            print('VERY GOOD')
        elif score==60:
            print('GOOD')
        elif score==50:
            print('PASS')
        elif score<50:
            print('BAD')
print('                      (CODE LAGOS 4 PROJECT)  \n\n')


print('NAME: OKWUMBU STEPHEN EMEKA')
print('SUPERVISOR: MR IDRIS')
print('EMAIL: emyokwumbu@gmail.com')
print('CONTACT: 07036718066,08127813976')

print('PROJECT ON NATIONAL COMMON ENTRANCE EXAMINATION INTO JUNIOR SECONDARY SCHOOLS (CBT) \n\n')




        #*************NATIONAL COMMON ENTRANCE CBT*****************#

print('                    LAGOS STATE EXAMINATION BOARD                 ')
print('      NATIONAL COMMON  ENTRANCE INTO  JUNIOR SECONDARY SCHOOLS                ')
print('                      CBT EXAMINATION 2018/2019              \n \n')

import time
import datetime


print('DATE:',datetime.datetime.now().strftime("%y-%m-%d\nTIME: %H:%M \n \n"))




#Those that are registered are allowed to partake in this entrance exam.
#LOGIN with your REGISTRATION NUMBER.
#If your REGISTRATION NUMBER is correct, it will display your personal details.
#You are given only 3 attempt to enter the correct REGISTRATION NUMBER.
#If you enter the WRONG REGISTRATION NUMBER, you wont be able to write this exam.
#Answer all questions,each questions carries 20 marks.
#Your total score will be diplayed once you are done with the exam.

#GOODLUCK!

for i in range (3):
    regnum=input('               ENTER REGISTRATION NUMBER  :  ' )
    if regnum== '001AA' :
            
        print('CANDIDATE NAME: OKWUMBU Emeka')
        print('EXAMINATION NO: 001AA')
        print('SEX           : MALE')
        print('EXAM CENTRE   : AYANGBURE PRIMARY SCHOOL IKORODU \n \n')
        print('INSTRUCTIONS FOR CANDIDATES: Make sure you read all questions carefully before choosing your options letter A-D on the keyboard.\n\n')
        print('CHOOSE THE WORDS THAT BEST COMPLETES EACH OF THE FOLLOWING SENTENCES.\n\n')
        questions()
        break
    
    elif regnum== ('002AB'):
        

        print('CANDIDATE NAME: AHMED chinedu')
        print('EXAMINATION NO: 002AB')
        print('SEX           : MALE')
        print('EXAM CENTRE   : AYANGBURE PRIMARY SCHOOL IKORODU \n \n')
        print('INSTRUCTIONS FOR CANDIDATES: Make sure you read all questions carefully before choosing your options letter A-D on the keyboard.\n\n')
        print('CHOOSE THE WORDS THAT BEST COMPLETES EACH OF THE FOLLOWING SENTENCES.\n\n')
        questions()
        break
        
               
    elif regnum== ('003AC'):

        print('CANDIDATE NAME: MODUPE rosemary')
        print('EXAMINATION NO: 003AC')
        print('SEX           : FEMALE')
        print('EXAM CENTRE   : AYANGBURE PRIMARY SCHOOL IKORODU \n \n')
        print('INSTRUCTIONS FOR CANDIDATES: Make sure you read all questions carefully before choosing your options letter A-D on the keyboard.\n\n')
        print('CHOOSE THE WORDS THAT BEST COMPLETES EACH OF THE FOLLOWING SENTENCES.\n\n')
        questions()
        break
    
       


        
    else:
        print('                                         Incorrect Registeration Number')
    
      
else:
    print('WRONG REGISTRATION NUMBER, Sorry this exam is not for you!')

    




