# display the welcome message
print("YOU are Welcome!!! This is a Trivial Quiz For CodeLagos,Please Note all questions carry equal Marks, You have 20mins.To complete the Quiz \n")
print("Project Designed By:Loveth Ugochukwu \n")
print("Name of The Program:Trivial Game/Multiple choice Quiz")
print("Email Address:chisazan@gmail.com \n")
print("FacilIitator'S Name:Dotun Onasanya \n")
print("Centre Name: GCL HUB \n")
print("program Objective:The idea of this Trivial Game is to create a simple Educational Games and Multiple choice Examination Questions Schools \n")
#Initialize the score variable
score = 0
question1=input("1-what is the name of Isaac father?\n(a)John,\n(b)Emeka,\n(c)Abraham\n")
#If answer is correct ,display:correct and add one to the score
score = score + 1
if(question1.lower() == "c"):
    print("correct")
else:
    print("wrong")
question2=input("2- who was the oldest man that ever lived in the Bible?\n(a)Hezekiah,\n(b)Methuselah,\n(c)paul\n")
if(question2.lower() == "b"):
    print("correct")
    score = score + 1

else:
    print("wrong")

question3=input("3-who was the shortest man in the Bible?\n(a)zacheus,\n(b)Agathe,\n(c)Zachetwoe\n")
if(question3.lower() == "a"):
   print("correct")
   score = score + 1

else:
    print("wrong")
    
question4=input("4-How many Books has the Bible?\n(a)25,\n(b)65,\n(c)66\n")
#If answer is correct ,display:correct and add one to the score 
score = score+1
if(question4.lower() == "c"):
    print("correct")
else:
    print ("wrong")
question5=input("5-How many people did Jesus feed?\n(a)5000,\n(b)3006,\n(c)5679\n")
#If answer is correct ,display:correct and add one to the score 
if(question5.lower() == "a"):
  print("correct")
  score = score +1

else:
    print ("wrong")
#Get back to step 3 until all the questions have been answered
    print(score)
    
    
question6=input("who was swallowed by a fish?\n(a)Jonah,\n(b)David,\n(c)Ada\n")
#If answer is correct ,display:correct and add one to the score 
score = score+1
if(question6.lower() == "a"):
    print("correct")
else:
    print ("wrong")
#Get back to step 3 until all the questions have been answered
    print(score)
    
question7=input("Ruth had a mother inlaw,what was her name called?\n (a)Stephnie,\n(b)Abigail,\n(c)Naomi\n")
#If answer is correct ,display:correct and add one to the score 
score = score+1
if(question7.lower() == "c"):
    print("correct")
else:
    print ("wrong")
    
#Get back to step 3 until all the questions have been answered
    print(score)

    
question8=input("Jesus Christ had how many Disciples?\n (a)63,\n(b)12,\n(c)23\n")
#If answer is correct ,display:correct and add one to the score 
score = score+1
if(question8.lower() == "b"):
    print("correct")
else:
    print ("wrong")
    
#Get back to step 3 until all the questions have been answered
    print(score)

    
question9=input("The Lord shall fight for me and i shall hold my peace can be found in ?\n (a)James 12vs5,\n(b)Mal3vs4,\n(c)Ex.14vs14\n")
#If answer is correct ,display:correct and add one to the score 
score = score+1
if(question9.lower() == "c"):
    print("correct")
else:
    print ("wrong")
    
#Get back to step 3 until all the questions have been answered
    print(score)

    
question10=input("what is the shortest verse in the Bible?\n (a)Mercy cried,\n(b)Jesus Wept,\n(c)Naomi laughed\n")
#If answer is correct ,display:correct and add one to the score 
score = score+1
if(question10.lower() == "b"):
    print("correct")
else:
    print ("wrong")
    
#Get back to step 3 until all the questions have been answered
    print(score)

#Total Score'
Score=float(score/10)* 100
print("out of 10, that is",Score, "%")

    

