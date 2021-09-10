'''
for index in range(10):
    print("Hello there!")

for index in range(2, 20, 3):
    print(index)
'''
students= [
    {"name": "Suryash", "grade": 80},
    {"name": "Yash", "grade": 88},
    {"name": "Daksh", "grade": 76},
]    
for student in students:
    name= student["name"]
    grade= student["grade"]

    print(f"{name} has a grade of {grade}.")