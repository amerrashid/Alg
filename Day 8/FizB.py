def is_div(a,b):
    if a % b == 0:
        return True
    return False


def fizz_buzz(n):
    if is_div(n, 3) and is_div(n, 5):
        print('FizzBuzz')
    elif is_div(n, 3):
        print('Fizz')
    elif is_div(n, 5):
        print('Buzz')
    else:
        print()


for num in range(0, 21):
    print (str(num) + ": ", end="")
    fizz_buzz(num)
