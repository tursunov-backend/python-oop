class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age =  age
        self.grade = grade

    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-sinf o'quvchisi.")

st01 = Student('ali', 13, 4)
st02 = Student('vali', 14, 5) 

st01.info()
st02.info()