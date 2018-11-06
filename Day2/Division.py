x = input("Enter a Number         :")
y = input("Enter a Second Number  :")

try:
    result = (int(x)/int(y))
except ZeroDivisionError:
    print("Sorry you cannot divide by zero")
except ValueError:
    print("Please use values 0-9 (Except as divisor!)")
except Exception:
    print("An unknown error has occured")
else:
    print(result)