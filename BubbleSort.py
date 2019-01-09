import random

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

BubbleSort()
