class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

student1 = Student("John", "CSE", 3.9)
student2 = Student("Pokemon", "ARTS", 2.0)


print(student1.name, student1.major, student1.gpa)

student1 = Student('Ismail', 'Cse', 3.9)
student2 = Student("Pam", "Art", 3.8)

print(student1.name, student1.major, student1.gpa)

print(student2.name, student2.major, student2.gpa)
