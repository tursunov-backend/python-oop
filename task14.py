class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Student(name='{self.name}', age={self.age})")


s01 = Student('Ali', 16)
s02 = Student('Vali', 11)
s03 = Student('Sami', 14)
s04 = Student('Gani', 18)
s05 = Student('Salim', 15)

students = [s01, s02, s03, s04, s05]


old_student = max(students, key=lambda x: x.age)


for s in students:
    s.show_info()

print("\nEng yoshi katta student:")
old_student.show_info()
