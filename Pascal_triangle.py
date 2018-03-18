#Pascal háromszög progi

def pascal_triangle():
	i = koz = j = szam = 0
	print ("Pascal háromszög program")
	sor = int(input("Kerem a sorok szamat: "))
	koz = sor
	for i in range(sor):     
		for koz in range(sor,i,-1):
			print (" ",end="")
		szam = 1
		for j in range(i+1):
			print(str(szam) + " ", end = "")
			szam = szam * (i - j) / (j + 1)
		print("\n", end = "")

pascal_triangle()
