class Cat:
    name = ""
    age = 0
    registered = False

    def __init__(self, input_n, input_age):
        self.name = input_n
        self.age = input_age

        if input_age > 2:
            self.registered = True

    def meow(self, number_times):
        for m in range (number_times):
            print("Meow")

    def meow(self, number_time, phrase=""):
        for m in range (number_time):
            print("Meow" + phrase)

c1 = Cat ("Jack", 2)
c2 = Cat ("Samantha", 9)

print ("Cat c1 registration is " + str(c1.registered))
print("Cat c2 registration is " + str(c2.registered))

c1.meow(5, " Test")