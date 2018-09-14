#Salaudeen Usman(Salaudeenusman30@gmail.com)
#Display the purpose of the program
print("First semester examination program")

#Display the instructions
print("Attempt ALL questions in this section.")
print("....")

#Initialize the score variable
score = 0

#--------------------------------------------------------------------------------
       #First Semester Examination 2012/2013
#--------------------------------------------------------------------------------

#Ask the user questions
question1 = input("Barter system had the following shsortcomings except? \n(a) measure of deferred payment \n(b) the problem of double coincidence of want \n(c) the indivisibillity of some product \n(d) the problem of specialization.\n")

#If the question is correct display: "Correct" and add 1 to the score
if (question1.lower() =="a"):
    print("Correct")
    score = score + 2
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question2 = input("Transfer of value becomes easier with the use of? \n(a) barter system \n(b) the internet \n(c) money \n(d) a good transport system\n")

#If the question is correct display: "Correct" and add 1 to the score
if (question2.lower() =="b"):
    print("Correct")
    score = score + 3
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question3 = input("One of the followings is not correct about an open cheque? \n(a) it is always cashable over the counter \n(b) the cashier needs to confirm the issuing bank before payment is made \n(c) it may need to be cleared at the clearing house \n(d) it can be of any value as premitted by the relevant regulatory agencies. \n")

#If the question is correct display: "Correct" and add 1 to the score
if (question3.lower() =="c"):
    print("Correct")
    score = score + 2
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question4 = input("Excess reserve is defined as..........? \n(a) the difference the interest payable on loans from a bank and interest receivable from assets lent out by bank customers.\n(b) the excess of deposit over the reserve \n(c) the excess of the discount rate over the interest rate \n(d) the difference between general reserves and the statutory reserves\n")

#If the question is correct display: "Correct" and add 1 to the score
if (question4.lower() =="a"):
    print("Correct")
    score = score + 2
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question5 = input("Full employment is a situation in which? \n(a) all adults who can work are employed \n(b) all people that are willing and able to work have jobs at the current wage rate. \n(c) there is no unemployment at all \n(d)there is only a seasonal unemployment \n")

#If the question is correct display: "Correct" and add 1 to the score
if (question5.lower() =="d"):
    print("Correct")
    score = score + 3
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question6 = input("The multiplier refers? \n(a) the part of expenditure that is endogenous \n(b) the  rate at which the investment changes as the government spending change \n(c) the rate at which the level of income charges as any of the autonomous spending change \n(d) the first differential of the autonomous spending as a result of a constant level of national income\n")

#If the question is correct display: "Correct" and add 1 to the score
if (question6.lower() =="a"):
    print("Correct")
    score = score + 2
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question7 = input("One of the following explain the broader money M3? \n(a) currency in circulation [cc] plus demand deposit [DD] \n(b) demand deposit plus time deposit \n(c) currency in circulation plus time deposit and demand deposit \n(d) currency in circulation plus certificate of deposit plus share stock\n")

#If the question is correct display: "Correct" and add 1 to the score
if (question7.lower() =="b"):
    print("Correct")
    score = score + 2
#Esle display: "Wrong"
else:
    print("Wrong")
    
#Ask the user a qustion
question8 = input("In a three-sector model the followings except one are true? \n(a) tax is introduced into the model of national income \n(b) government presence is noted \n(c) there must be a proportional tax \n(d) the tax multiplier must be negative\n")

#If the question is correct display: "Correct" and add 1 to the score
if (question8.lower() =="c"):
    print("Correct")
    score = score + 2
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question9 = input("One of the following does not affect demand for money? \n(a) change in income \n(b) inflation \n(c) interest rate \n(d) excess reserve \n")

#If the question is correct display: "Correct" and add 1 to the score
if (question9.lower() =="a"):
    print("Correct")
    score = score + 3
#Esle display: "Wrong"
else:
    print("Wrong")

#Ask the user a qustion
question10 = input("All but one of the following s describe fiscal policies? \n(a) surplus budgeting \n(b) delaying repayment of public debt \n(c) selling and buying of treasury bills \n(d) increasing the tax rate \n")

#If the question is correct display: "Correct" and add 1 to the score
if (question10.lower() =="d"):
    print("Correct")
    score = score + 2
#Esle display: "Wrong"
else:
    print("Wrong")

#Go back to step 10 until all the questions have been answered
#Print the score of the user
print("Your score is", score)

if  (score == 3):
    print("Excellent job")
elif(score == 2):
    print("Wow.. good job")
else:
    print("you can still do better")
