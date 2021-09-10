class Student:
    def __init__(self, new_name, new_grades):
        self.name=new_name
        self.grades=new_grades
    def average(self):
        return sum(self.grades)/len(self.grades)

student_one= Student('Suryash', [70,88,90,99])
student_two= Student('Rahul', [90,80,80,100])

print(student_one.name)
print(student_two.name)
print(student_one.__class__)
print(student_one.average())
print(Student.average(student_one))
