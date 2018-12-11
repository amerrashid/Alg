class Animal :
    name = ""

class Dog (Animal) :
    def make_sound(self):
        print ("Bark")

class Cat (Animal) :
    def make_sound(self):
        print ("Meow")

d = Dog()
d.name = "Spot"

c = Cat()
c.name = "Felix"

d.make_sound()
c.make_sound()