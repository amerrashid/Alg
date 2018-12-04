def print_separator(width):
    for w in range (width):
        print("*", end="")
    print()

def print_separator_2(width):
    print("x" * width)

print("This is line 1")

print_separator(50)
print_separator_2(50)
