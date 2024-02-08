# cat1.py
from animal1 import Animal  # Importing the base class

# Another derived class (Subclass)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        print("Meow!")

    def climb_tree(self):
        print(f"{self.name} is climbing a tree")

