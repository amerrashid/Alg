a = input("Enter the year you started to work:")
b = input("Enter the current year:")



try:
    c = int(b) - int(a)
except ValueError:
    print("The value(s) entered are not numeric!")
except Exception:
    print("A general error has occured.")
else:
    print("You have been working for {0} years".format(c))
