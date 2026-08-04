class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"Some generic animal sound.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print(f"Woof! Woof!")

    def fetch(self, item):
        self.item = item
        print(f"{self.name} fetches the {self.item}.")

    def eat(self):
        print("Buddy loves bones.")
        return super().eat()

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Meow~ Meow~")

    def scratch(self, object):
        self.object = object
        print(f"{self.name} scratches the {self.object}.")

    def eat(self):
        print("Whiskers loves fish.")
        return super().eat()
       
def introduce(Animal):
    print(f"name: {Animal.name} and age: {Animal.age}")
    return Animal.make_sound(), Animal.eat()


    
a = Animal("Generic", 5)
a.eat()
a.sleep()
a.make_sound()

d = Dog("Buddy", 3, "Golden Retriever")
d.eat()          # 继承自 Animal
d.sleep()        # 继承自 Animal
d.make_sound()   # 重写后
d.fetch("ball")  # 子类特有
print(d.breed)   # 新增属性

c = Cat("Whiskers", 2, "orange")
c.eat()
c.sleep()
c.make_sound()
c.scratch("sofa")
print(c.color)

animals = [Dog("Rex", 4, "German Shepherd"), Cat("Luna", 3, "gray")]
for a in animals:
    introduce(a)