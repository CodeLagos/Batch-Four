# NAME: Oluwasanmi Ale
# EMAIL: sanmicines@gmail.com

# This is a Quality Audit_Form to grade CSR on 4 Parameters on Calls made.

# Ask the User to enter Name
Quality_Assesor=input("Quality Assesor's Name:")

# Ask the User to enter Agent's ID
Agent_ID=str(input("Enter Agent's ID: "))

# Ask the User to enter the Date
Date=str(input("Enter the Date of Audit "))

# Ask the User to Score the Agent accordingly on different parameters
print("Pleas grade the Agent on the following parameters")
print("SOFT_SKILL")
Soft_Skill1=input("Did Agent obtain and make use of Customer's name? Enter Yes or NO:")
Score=0
if(Soft_Skill1=="Yes"):
    Score=Score+12.5
else:
    Score=0
print(Score)
Soft_Skill2=input("Was the correct mode of request used by the Agent? Enter Yes or No:")
if(Soft_Skill2=="Yes"):
    Score1=Score+12.5
else:
    Score1=Score-12.5
if(Score==12.5 and Soft_Skill2=="No"):
    Score1=Score
if(Score==0 and Soft_Skill2=="No"):
   Score1=0
print(Score1)

print("PERSUASIVE AND NEGOTIATION SKILL")
Persuasive_and_Negotiation_Skill1=input("Did Agent provide winback option or an alternative where necessary?Yes or No:")
Score2=0
if(Persuasive_and_Negotiation_Skill1=="Yes"):
    Score2=Score2+12.5
else:
    Score2=0
print(Score2)
Persuasive_and_Negotiation_Skill2=input("Was Agent able to persuade Customer to make payment? Yes or No:")
if(Persuasive_and_Negotiation_Skill2=="Yes"):
    Score3=Score2+12.5
else:
    Score3=Score2-12.5
if(Score2==12.5 and Persuasive_and_Negotiation_Skill2=="No"):
    Score3=Score2
if(Score2==0 and Persuasive_and_Negotiation_Skill2=="No"):
    Score3=0
print(Score3)

print("CONTENT RESELL")
Content_Resell1=input("Did Agent try to sell content to Customer? Yes or No:")
Score4=0
if(Content_Resell1=="Yes"):
    Score4=Score4+12.5
else:
    Score4=0
print(Score4)
Content_Resell2=input("Was current promo communicated to the Customer? Yes or No:")
if(Content_Resell2=="Yes"):
    Score5=Score4+12.5
else:
    Score5=Score4
if(Score4==12.5 and Content_Resell2=="No"):
    Score5=Score4
if(Score4==0 and Content_Resell2=="No"):
    Score5=0
print(Score5)

#Agent who fails to report correctly earns a "NO" and Scorea a fatal.
print("REPORTING")
Reporting=input("Did Agent capture correct churn reason and termination?Yes or No:")
Score6=0
if(Reporting=="Yes"):
    Score6=25
else:
    Score6=0
print(Score6)
Total_Score=Score1+Score3+Score5+Score6
print(Total_Score)
if(Reporting=="No"):
    Total_Score=0
print("Agent's Total Score is",Total_Score)

print("Audited by:",Quality_Assesor)
