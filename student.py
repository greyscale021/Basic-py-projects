class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

student1 = Student("John", "CSE", 3.9)
student2 = Student("Pokemon", "ARTS", 2.0)


print(student1.name, student1.major, student1.gpa)