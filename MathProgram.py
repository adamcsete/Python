import random
import datetime

def MathProg():
    while True:
        print("    Bubble sort - number 1")
        print("      Leap year - number 2")
        print("Pascal triangle - number 3")
        print("      Fibonacci - number 4")
        print("           Exit - number 0")
        x = int(input("Please choose an option: "))

        if(x == 1): BubbleSort()
        elif(x == 2): LeapYear()
        elif(x == 3): Pascal_triangle()
        elif(x == 4): Fibonacci()
        elif(x == 0): break

def BubbleSort():
    arraysize = int(input("Number of sortable numbers: "))
    sortable = []
    arraysize = arraysize-1

    for i in range(arraysize):
        sortable.append(random.randint(10,99))
    print("Original list of numbers: ",sortable)

    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(sortable)-1):
            if sortable[i] > sortable[i + 1]:
                sorted = False
                sortable[i],  sortable[i+1]= sortable [i+1], sortable[i]

    print("Sorted list of numbers: ",sortable)

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

def Pascal_triangle():
    i = koz = j = szam = 0
    print("Pascal háromszög program")
    sor = int(input("Kerem a sorok szamat: "))
    koz = sor
    for i in range(sor):
        for koz in range(sor,i,-1):
            print (" ",end="")
        szam = 1
        for j in range(i+1):
            print(int(szam)," ", end = "")
            szam = szam * (i - j) / (j + 1)
        print("\n", end = "")

def Fibonacci():
    linelength = int(input("Number of Fibonacci numbers: "))
    if linelength == 1:
        print("1")
    elif linelength == 2:
        print("1 1")
    elif (linelength>2):
        print("1 1", end="")
        former = 1
        recent = 1
        output = 0
        for i in range(linelength-2):
            output = former + recent
            print("",output,end="")
            former=recent
            recent=output

MathProg()
