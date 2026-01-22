class Student:

    def __init__(self, name, age, grade):
        self.name = 'name'
        self.age = age
        self.grade = grade

    def info(self):
        return f"Student(name='{self.name}', age='{self.age}', grade='{self.grade}')"

s01 = Student('Ali', 16, 4)
s02 = Student('Vali', 12, 5)

print(s01.info())
print(s02.info())