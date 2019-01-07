def fibonacci():
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
fibonacci()
