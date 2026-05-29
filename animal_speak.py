#parent class
class animal:
    def speak(self):
        print("animal speaks")
#child class overriding the speak method
class Dog(animal):
    def speak(self):
        print("wolf,wolf")
class Cat(animal):
    def speak(self):
        print("meow.meow")
def make_animal_speak(animal):
    animal.speak()
#creating objects
dog=Dog()   
cat=Cat()
#calling function
make_animal_speak(dog)
make_animal_speak(cat)
  