#display the purpose of the program
#adigun ridwan(adigunridwan@g.mail)
#code lagos 4.0
print("this program is to tell if you are elligible to vote")
#display the instruction
print("please read and answer question carefully")
#ask user his or her name
name=input("ask user to enter name: ")
#ask user to enter age
age=int(input("ask user to enter age: "))
if(age<18):
   a=("you are not elligible to vote")
        
else:
    a=(" ")
#ask user another question
answer=input("are you a citizen of this country (yes or no)\n")
if(answer.lower()=="no"):
    b=("you are not a Nigerian")   
else:
    b=("you are a Nigerian")
#ask user another question
answer=input("did you have any idea on how to vote\n")
if(answer.lower()=="no"):
    c=("come to the head office for training")    
else:
    c=(" ")
#ask user another question
answer=input("did you have your pvc with you\n")
if(answer.lower()=="no"):
    d=("go and have your pvc")
    
else:
    d=("you are elligible and free to vote for the candidate of your choice.\nThank you")    
   
print(name,"\n",a,"\n",b,"\n",c,"\n",d,"\n")
