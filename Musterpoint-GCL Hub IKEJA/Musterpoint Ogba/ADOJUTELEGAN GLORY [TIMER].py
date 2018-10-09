print("My Name: ADOJUTELEGAN GLORY Y.")
print("Email Address: crystalbellcreations@yahoo.com")
print("Facilitators Name: Dotun Omosanya")
print("Centre: MusterPoint Ogba Lagos\n")
print("WELCOME TO GLORY_TIMER\n")
print("This Timer Will Help You To Monitor The Duration of Time Expended While Carrying Out Your Task")


import os
import time

def timer_age_limited():
    seconds= float(0)
    minutes= int(0)
    hours= int(0)

    print("PRESS R To BEGIN and PRESS Ctrl-C to STOP\n")
    run = input("WAITING FOR RESPONSE: ")

    try:
        while True:
            run.lower()=="r"
            if seconds > 59:
                seconds = 0
                minutes = minutes+1
            if minutes > 59:
                minutes = 0
                hours = hours+1
            os.system('cls')
            seconds = (seconds + 1)
            print(hours, ":",minutes,":",seconds)
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nWell Done, You Have Tried Enough. Good Job.\n')

print("You must be 18years upward to access this Timer\n")
print("Please  Enter your age. e.g. 25")

years = int(input("Age:"))
while True:
    if years < 18:
        print("So Sorry! You are less than the required age")
        break
    else:
        print("Congratulations! You are good to start.")
        timer_age_limited()
        break

