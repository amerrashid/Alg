class Calculator:
    number1 = 0
    number2 = 0

calc1 = Calculator()
calc2 = Calculator()

calc1.number1 = 2
calc1.number2 = 3

calc2 = calc1

print("number1 of calc1 is " + str(calc1.number1))
print("number1 of calc1 is " + str(calc2.number1))

calc1.number1 = 99

print("number1 of calc1 is " + str(calc1.number1))
print("number1 of calc1 is " + str(calc2.number1))
