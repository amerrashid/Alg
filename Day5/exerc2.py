import random

# a = random.randint(1, 100)
# print(a)

list = []
for x in range(10):
    x = random.randint(1, 100)
    list.append(x)
print(list)

for y in list:
    low = min(list)
    high = max(list)
    lenf = len(list)
    tot = sum(list)

print("The minimum is " + str(low))
print("The maximum is " + str(high))
print("The length is " + str(lenf))
print("The sum is " + str(tot))
