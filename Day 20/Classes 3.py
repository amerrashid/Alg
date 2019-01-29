import random
numList = [1, 2, 3, 4]
nums = 0
tot = 0
elem = 0
avg = 0
maxNo = 0
minNo = 0

class Calculator:

    def __init__(self, numList):
        self.numList = numList

    def get_average(self, numList):
        tot = sum(numList)
        elem = len(numList)
        avg = tot / elem
        print ("The Average is: " + str(avg))

    def get_max(self, numList):
        maxNo = max(numList)
        print ("The Maximum is: " + str(maxNo))

    def get_min(self, numList):
        minNo = min(numList)
        print ("The Minimum is: " + str(minNo))

    def clr(self, numList):
        numList.clear()
        print ("Cleared")

    def rand_gen(self, numList, x, y, z):

        cnt = 0
        while cnt < x:
            rand = random.randint(y,z)
            numList.append(rand)
            cnt += 1
        print (numList)



c = Calculator(numList)
#cv = c.clr(numList)
av = c.get_average(numList)
mx = c.get_max(numList)
mx = c.get_min(numList)
gen = c.rand_gen(numList, 3, 8, 10)

