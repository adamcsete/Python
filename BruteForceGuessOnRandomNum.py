import random
import datetime


class RandomBruteForce:
    def __init__(self):
        # Creating variables
        code = ""
        checker = set()
        diffcounter = 0
        counter = 0

        # Creating the code to be broken - code contains 4 digits
        for i in range(4):
            code = code + str(random.randint(0, 9))

        # Time when the forcing started
        time1 = datetime.datetime.now()

        # Actual forcing code
        while True:
            counter += 1
            alter = ""
            for i in range(4):
                alter = alter + str(random.randint(0, 9))
            if alter not in checker:
                checker.add(alter)
                diffcounter += 1
                print("The code is: " + code + ", " + "the guess is: " + alter)
            if alter == code:
                break

        # Time when the forcing ended
        time2 = datetime.datetime.now()
        print("\nNumber of attempts: ", counter, "\nNumber of different attempts: ", diffcounter, "\nStarted: ", time1, "\nEnded:",  time2)


RandomBruteForce()
