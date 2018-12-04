def is_num_neg(n):
    if n < 0:
        return True
    return False

the_num = input("Enter a number :")

if is_num_neg(int(the_num)):
    print("Negative")
else:
    print("Positive")
