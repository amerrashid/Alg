list1 = ["a", "b", "c"]

list1[1] = 'x'
list1.append('y')
list1.remove('x')
list1.pop(0)
new1 = list1 + ["q", "f"]
for listItem in list1:
    print("The value is: ", end="")
    print(listItem)

for bg in new1:
    print(bg)

print(len(list1))

print(len("Hello"))

