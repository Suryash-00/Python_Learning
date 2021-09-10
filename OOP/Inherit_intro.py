class Student:
    def __init__(self, name, school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary=salary

    @property   #This is property decorator and turns a method into a property
    def weekly_salary(self):
        return self.salary*38

suri=WorkingStudent('Suryash', 'SMS', 20)
print(suri.salary)
suri.marks.append(82)
suri.marks.append(72)
suri.marks.append(78)
print(suri.average())
print(suri.weekly_salary)