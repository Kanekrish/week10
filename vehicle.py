# Base class (Superclass)
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running.")

    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine has been stopped.")

    def drive(self):
        print(f"The {self.make} {self.model} is now in motion.")


# Derived class (Subclass)
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self):
        print("Beep! Beep!")

    def drive(self):  # Overriding the drive method
        print(f"The {self.make} {self.model} is zooming down the road with {self.num_doors} doors.")


# Another derived class (Subclass)
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def rev_engine(self):
        print("Vroom! Vroom!")

    def drive(self):  # Overriding the drive method
        print(f"The {self.make} {self.model} is weaving through traffic on {self.num_wheels} wheels.")


# Create instances of the subclasses
my_car = Car("Toyota", "Camry", 2022, 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportstar", 2022, 2)

# Accessing methods from the base class
my_car.start_engine()  # Output: The Toyota Camry's engine is now running.
my_motorcycle.stop_engine()  # Output: The Harley-Davidson Sportscaster's engine has been stopped.

# Accessing methods specific to each subclass
my_car.honk()  # Output: Beep! Beep!
my_motorcycle.rev_engine()  # Output: Vroom! Vroom!

# Accessing overridden methods in subclasses
my_car.drive()  # Output: The Toyota Camry is zooming down the road with 4 doors.
my_motorcycle.drive()  # Output: The Harley-Davidson Sportswriter is weaving through traffic on 2 wheels.
