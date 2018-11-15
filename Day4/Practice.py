# 1
age = 20
age2 = 20
print(age)
print(age2)
print("The sum of the ages is " + str(age + age2))


# 2
name = "champlain"
print("I am taking this course at " + name.title())


# 3
import decimal

Sale1 = "1.40"
Sale2 = "2.30"
sale1_d = decimal.Decimal(Sale1)
sale2_d = decimal.Decimal(Sale2)
print(sale1_d + sale2_d)


# 4
total = 34.00
increase_rate = 15.56
calc = (total + ((total*increase_rate)/100))

print("The total amount increased by the percentage rate is : " + str(calc))


# 5
var1 = "hello"
var2 = "you"
var1_length = len(var1)
var2_length = len(var2)
total = var1_length + var2_length

print("The length of both the variables var1 and var2 is "
      + str(total) + " characters")


# 6
for a in range(1, 11):
    a = a*a
    print(a)


# 7

for a in range(2):
    for b in range(2):
        for c in range(2):
            print(str(a)+str(b)+str(c))





