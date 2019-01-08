import datetime

def LeapYear():
    number = int(input("How many of the upcoming leap years would you like to see: "))
    lyr=0
    year=int(datetime.datetime.now().year)
    help = False
    print("Current year is: ",year)
    for i in range (number):
        while True:
            if (year%4!=0):
                year+=1
            elif (year%100!=0):
                lyr=year
                break
            elif (year%400!=0):
                year+=1
            else:
                lyr=year
                break
        print(lyr," ",end="")
        year+=1

LeapYear()
