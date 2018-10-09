#program to help one generate a password and store this password
#USING THE FILE OPTIONS
print('Name:Ojo-Bello Oluwayimika \nCentre:GCL hub \nE-mail:yimzika@gmail.com \n Project Name:Password manager \nFacilitator:Mr.Dotun')
import random
import os.path
import time
myfile=open('Testfile.txt','w')
complexpass=''
print('Do you want a simple password')
passtype=input('yes or no?;')
if passtype=='yes':
    flair='1'
else:
    flair='0'
while flair=='1':
 min=1900
 max=2020
 print('This program is designed to help you generate passwords and store them safely')
 file1= open("Testfile.txt","a")
 username=str(input('What is your firstname/nickname?:'))
 DOB=str(input('What year where you born'))
 Account=str(input('What account is this password for?'))
 rand_no=(random.randint(min, max))
 print('Please wait...')
 print('Application is generating a secure password')
 lists=['Eggs','Peanuts', 'Butter' ,'Bread','Fire','Frozen','Water','Clear','lightning','bugatti','Tiger','Milk','cookies' ]
 password1=username+DOB+'!'
 password2=username+random.choice(lists)+str(rand_no)
 print('Which do you prefer',password1, "or", password2)
 IN=(input('1 or 2?'))
 if IN=='1':
     Final_password=password1
 else:
     Final_password=password2
 finalpass= ('Your password is ', Final_password, 'for ', Account)
 finale=str(finalpass)
 ('\n your password is ',Final_password, Account)
 print('your password for your ', Account, ' account is ', Final_password)
 savepass=input('Are you Ok with this password?')
 if savepass=='yes':
     flair='0'
 else:
     print('Lets try this again')
 myfile= open('Testfile.txt','a')
 print('Processing your password')
 time.sleep(5)
 myfile=open('Testfile.txt',"a")
 myfile.write(finale)
 myfile.close()
 print('your password has been stored')
 print('please check the directory below')
 print('C:/Users/Mattobell/AppData/Local/Programs/Python/Python37-32/Testfile.txt to check your stored password')
 print('Or do you need a much more complex password')
 reqcomp=input('yes or no?')
 if reqcomp=='no':
     print('Thamk you')
     time.sleep(3)
     quit()
 elif reqcomp=='yes':
     print('ok')
     time.sleep(3)
letters_numbers=['A','B','C','D','E','F','G','H','I','J','k','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k']
complexpass=(''.join(random.sample(letters_numbers,10)))
print(complexpass)
complexpass
complex_ini=str(input('are you okay with this password?: '))
if complex_ini=='yes':
    flair='2'
    Account=str(input('what is this password for?'))
    finale=('Your password is ', complexpass , 'for ', Account, ' account')
    finalpass=str(finale)
while flair=='2':
    myfile=open('Testfile.txt','a')
    print('processing your password')
    myfile.write(finalpass)
    myfile.close()
    print('your password has been stored')
    print('please check the directory below')
    print('C:/Users/Mattobell/AppData/Local/Programs/Python/Python37-32/Testfile.txt to check your stored password')
    break
input('press enter to exit:')



    

    

 

