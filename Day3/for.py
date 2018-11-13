for b in range(10):
    if b == 3:
        break
    print(b)

for b in range(10):
    if b == 3:
        continue
    print(b)

for a in range(10):
    if a % 2 == 0:
        continue
    else:
        print(a)

for a in range(10):
    if a % 2 != 0:
        continue
    else:
        print(a)
