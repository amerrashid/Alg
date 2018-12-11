import random
i = (random.randint(1,101))
for x in range (6):

    try:
        user_in = int(input ("Please enter a number between 1 & 100 (attempt " + str(x+1) + "): "))
        if user_in > i:
            print ("Wrong guess, you guessed too high.")
        elif user_in < i:
            print ("Wrong guess, you guessed too low.")
        elif user_in == i:
            print ("Correct! You win.")
            break
        else:
            print("Sorry, you didn't guess the correct number. The correct number was " + str(i))

    except ValueError:
        print ("Please use numeric values")

