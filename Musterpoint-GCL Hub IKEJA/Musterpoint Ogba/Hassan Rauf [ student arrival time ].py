#a program to list the names of student daily by grouping into how they came early.
print ("project by: Hassan Rauf Olayiwola\n project title: a program to list the names of student the time they came in.\n email:raufolayiwolah@gmail.com\n facilitator: onasanya Dotun \n centre: muster point, ogba")
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
today=date.today()
print (today)
student=[]
snum=0
while snum>=0:
    snum=eval(input("enter your student code:"))
    if snum>=0:
        checkin=datetime.now()
        print (checkin)
        early=checkin + timedelta(seconds=900)
        late=early+timedelta(seconds=900)
        s=input("enter your name:")
        for i in student:
            print (i,end='')
        student.append(s)
        student.append(checkin)
        print(" you came in at", checkin)
        if (checkin<=early):
            print ("welcome, you are early")
        elif (early < checkin <=late):
            print ("you are late")
        else:
            print ("you are very late")
else:
    print ("ATTENDANCE LIST",*student, sep = "\n")


