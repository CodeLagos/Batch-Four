#Joshua Odubiro
#olayemisamuel55@gmail.com
#08162583688

#python to calculate number of days between two dates

from datetime import date
def op():
    year=int(input("input the start year in integer format"))
    month=int(input("input the start month in integer format"))
    day=int(input("input the start day in integer format"))
    endyear=int(input("input the end year in integer format"))
    endmonth=int(input("input the end month in integer format"))
    endday=int(input("input the end day in integer format"))
    do=date(year,month,day)
    d1=date(endyear,endmonth,endday)
    delta=d1-do
    print(delta.days+1)
op()
