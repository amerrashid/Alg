class Animal:

    def __init__(self):
        self.name = "Joe"

    def make_sound(self):
        print ("I made a generic sound.")

    def test(self):
        print("test")

class Dog (Animal):

    def make_sound(self):
        print ("My name is " + self.name + " bark")

    def make_parent_sound(self):
        self.test()
        super().make_sound()

def invoke_sound_from_objective(animal):
    animal.make_sound()

d1 = Dog()

d1.make_sound()
d1.make_parent_sound()

