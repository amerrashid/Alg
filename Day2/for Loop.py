for t in range(10):
    print(t)
    print(t+1)
print ("Program run has ended")

for t in range(11):
    print(str(t) + ": ", end="")

    for t in range(t):
        print("x", end = " ")
    print()
print ("Program run has ended")

for y in range(0,11):
    print(str(y)+": ", end="")
    for x in range(y):
        print("*", end="")
    print()
print ("Program run has ended")
