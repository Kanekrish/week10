# main1.py
from dog1 import Dog  # Importing the Dog class
from cat1 import Cat  # Importing the Cat class

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

