#OSITA CHIKERE
#alaribechikereosita@yahoo.com


#display the purpose of this program
print("this is a quiz about Nigeria")

#display the instructions
print("select the letter with the correct option")

#initialize the score variable
score = 0

#ask the user a question
question1 = input("in what year did Nigeria gain her independence? \n(a)1950 \n(b)1955 \n(c)1960 \n(d)1965 \n")

#wait for the answer
#if the question is correct, display: "correct and add 1 to the score
if(question1.lower()=="c"):
    print("corret")
    score=score + 1
#else display: "wrong"
else:
    print("wrong")

#ask the user a question
question2= input("in what year did Nigeria became a republic? \n(a)1970 \n(b)1963 \n(c)1965 \n(d)1962 \n")

#if the question is correct, display: "correct" and 1 to the score
if (question2.lower()=="b"):
    print("correct")
    score = score + 1
#else display: "wrong"
else:
     print("wrong")

#ask the user a question
question3 = input("who named Nigeria after the niger river area? \n(a)mike tyson n()lord lugard \n(c)bill cosby \n(d)flora shaw \n")

#if the question is correct, display: "correct" and add 1 to the score
if (question3.lower()=="d"):
    print("correct")
    score = score + 1
#else display: "wrong"
else:
    print("wrong")


#ask the user a question
question4= input("when was the southern and northern protectorate amalgamated into one Nigeria? \n(a)1920 \n(b)1930 \n(c)1914 n(d)1910 \n")
if (question4.lower()=="c"):
    print("correct")
    score = score + 1
#else display: "wrong"
else:
    print("wrong")

#ask the user a question
question5= input("who is the first indigenous governor general of Nigeria? \n(a)dr Nnamdi Azikiwe \n(b)sir ahmadu bello \n(c)chief chris okotiebo \n(c)chris ngige \n(d)bobrisky \n")
if (question5.lower ()=="a"):
    print ("correct")
    score = score + 1
#else display: "wrong"
else:
    print ("wrong")
