class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            raise ValueError("Age cannot be negative.")

Dog1 = Dog("Buddy", 3)
print(Dog1.bark())  # Output: Buddy says Woof!
Dog2 = Dog("Max", 5)
Dog2.set_age(6)
print(Dog2.get_age())  # Output: 6