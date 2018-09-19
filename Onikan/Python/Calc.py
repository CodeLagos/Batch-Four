#ojuade kazeem
import math
print("WELCOME TO MY CALCULATOR I WISH YOU ENJOY USING THIS PROGRAM")
print("PLEASE READ THE INSTRUCTIONS CAREFULLY BEFORE USING THE PROGRAM")
print(" CHOOSE THE FUNCTION YOU WISH TO PERFORM" " \"YOU DO THIS BY TYPING EITHER \n ADD \n SUBTRACT \n MULTIPLY \n SQAURE ROOT  \n DIVIDE")
print("NOTE ALL FUNCTION NAME SHOULD BE IN UPPERCASE")
print("FOR USING THE SQUARE ROOT IF YOU HAVE JUST ONE NUMBER TO SOLVE FOR REPEAT IT IN THE SECOND NUMBER OPTION")
print("                      YOU CAN STATRT USING THE PROGRAM")
A=input("Enter a function: ")
B=input("Enter the first number: ")
C=input("Enter the second number: ")
D=float(B) + float(C)
E=float(B) * float(C)
F=float(B) - float(C)
G=math.sqrt(float(B))
H=math.sqrt(float(C))
I=float(B)/float(C)
if (A=="ADD"):
    print("THE ADDITION OF",B,"AND",C,"GIVES" ,D)
elif (A=="SUBTRACT"):
    print("THE SUBTRACTION OF",B,"AND",C,"GIVES" ,F)
elif (A=="MULTIPLY"):
    print("THE MULTIPLICATION OF",B,"AND",C,"GIVES" ,E)
elif(A=="SQUARE ROOT"):
    print("VALUE FOR THE FIRST NUMBER IS",G,"\n" "VALUE FOR THE SECOND NUMBER IS",H)
elif (A=="DIVIDE"):
    print("THE DIVISION OF",B,"AND",C,"GIVES" ,I)
    


