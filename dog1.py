# dog1.py
from animal1 import Animal  # Importing the base class

# Derived class (Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball")


