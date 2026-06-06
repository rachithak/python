class animal:
    def sound(self):
        print("animal marks sound")
class dog(animal):
    def bark(self):
        print("dog barks")
d=dog()
d.sound()
d.bark()