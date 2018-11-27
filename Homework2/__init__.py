import random

# a = random.randint(1, 100)
# print(a)

list = []
for x in range(10):
    x = random.randint(1, 100)
    list.append(x)
print(list)

maxVal = list[0]
for y in list:
    if y>maxVal:
       maxVal = y
print(maxVal)

minVal = list[0]
for y in list:
    if y<minVal:
       minVal = y
print(minVal)

lx = 1
for lx in list:
    lx = lx + 1
print(lx)

tot = list[0]
for z in list:
    tot = tot + z
print(tot)
testtot = sum(list)
print(testtot)