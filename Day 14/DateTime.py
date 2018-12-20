import datetime

x = datetime.datetime.now()

print (x)

print(x.year)
print(x.strftime("%A"))

"2018-12-20 11:30am"

date_to_print = ""

date_to_print += x.strftime("%Y-%m-%d %I:%M")
date_to_print += x.strftime("%p").lower()

print(date_to_print)

print(x.strftime("%Y-%m-%d %I:%M%p").lower())

print("X"*10)