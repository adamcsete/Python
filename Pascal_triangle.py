#Pascal háromszög progi

def fuggi():
    print("Ez egy fuggveny aminek nincs parametere!")    
    sz = ""    
    for i in range(10):
        sz+= str(i)
        sz+= " "
    print sz

def pascal_triangle():
    i, koz, j, szam = 0, 0, 0, 1
    sor = input("Kerem a sorok szamat: ")
    koz = sor
    for i in range(sor):     
        for koz in range(sor,i,-1):
            print " ",
        szam=1
        for j in range(i+1):
            print str(szam)+" ",
            szam=szam*(i-j)/(j+1)
        print"\n",

fuggi()
pascal_triangle()
