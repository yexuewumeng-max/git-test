class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 90 and self.score <= 100:
            self.level = "A"
        elif self.score >= 80 and self.score <= 89:
            self.level = "B"
        elif self.score >= 70 and self.score <= 79:
            self.level = "C"
        elif self.score >= 60 and self.score <= 69:
            self.level = "D"
        else:
            self.level = "F"
        return self.level

    def display(self):
        print(f"姓名：{self.name}, 年龄：{self.age}, 等级： {self.get_grade()}")

    def is_passing(self):
        if self.score >= 60:
            return True
        else:
            return False

    school = "Python 编程学校"

    @classmethod
    def get_school_info(cls):
        return cls.school

    @staticmethod
    def is_valid_score(score):
        if score >= 0 and score <= 100:
            return True
        else:
            return False

Student1 = Student("Tom", 18, 99)
Student2 = Student("Jerry", 19, 89)
Student3 = Student("Tiffy", 16, 58)

Student1.display()
Student2.display()
Student3.display()

if Student1.is_passing():
    print("yes")
else:
    print("no")

if Student2.is_passing():
    print("yes")
else:
    print("no")

if Student3.is_passing():
    print("yes")
else:
    print("no")

print(Student.get_school_info())
print(Student.is_valid_score(85))
print(Student.is_valid_score(105))

print(Student.school)


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        Animal.animal_count += 1

    def speak(self):
        print(f"{self.name}发出了声音")

    def get_info(self):
        return f"名字：{self.name}, 物种：{self.species}, 年龄：{self.age}"

    animal_count = 0
    habitat = "earth"

    @classmethod
    def get_animal_count(cls):
        return cls.animal_count

    @classmethod
    def creat_from_dict(cls, data_dict):
       
        return cls(data_dict["name"], data_dict["species"], data_dict["age"])

    @staticmethod
    def is_adult(age):
        if age >= 3:
            return True
        else:
            return False

    
Animal1 = Animal("momo", "Dog", 2)
Animal2 = Animal.creat_from_dict({"name": "大黄", "species": "狗", "age": 4})
Animal3 = Animal("fish", "fish", 1)

Animal1.speak()
Animal2.speak()
Animal3.speak()

print(Animal1.get_info())
print(Animal2.get_info())
print(Animal3.get_info())

print(Animal.get_animal_count())

print(Animal.is_adult(2))

