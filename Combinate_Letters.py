import random, math

letternumber = int(input("Number of the letters: "))

letters = []
    
#get the letters
for i in range (letternumber):
    print(i+1,".letter:", end="")
    letters.append(input())
        
print()      
    
i=0
    
for word in letters:
    print(i+1,".letter is", word)
    i=i+1

def combinate_letters():

#mix them
    x = []
    
    for i in range(letternumber):
        x.append(0)
    
    helpset = {-1}
    
    for i in range(letternumber):
        x[i] = random.randint(0,letternumber-1)
        while x[i] in helpset:
                x[i] = random.randint(0,letternumber-1)
        helpset.add(x[i])
    
#writing the mixed letters on screen
    newword = ""
    for i in range(letternumber):
        newword += letters[x[i]]
    
    return newword

#repeating the word creation until reaching factorial 
words = {"helpword"}
for i in range(math.factorial(letternumber)):
    word = combinate_letters()
    while word in words:
        word = combinate_letters()
    words.add(word)
    print(word)
    


