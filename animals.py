# Base class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Abstract method, to be overridden by subclasses

    def move(self):
        print(f"{self.name} is moving")


# Derived class (Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball")


# Another derived class (Subclass)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        print("Meow!")

    def climb_tree(self):
        print(f"{self.name} is climbing a tree")


# Create instances of the subclasses
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Gray")

# Accessing methods from the base class
my_dog.move()  # Output: Buddy is moving
my_cat.move()  # Output: Whiskers is moving

# Accessing methods specific to each subclass
my_dog.make_sound()  # Output: Woof!
my_cat.make_sound()  # Output: Meow!

# Accessing methods unique to specific subclasses
my_dog.fetch()  # Output: Buddy is fetching the ball
my_cat.climb_tree()  # Output: Whiskers is climbing a tree
