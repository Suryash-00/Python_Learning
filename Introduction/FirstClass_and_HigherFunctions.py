'''
def greet():
    print("Hello")

hello=greet

hello()
'''
avg= lambda seq: sum(seq)/len(seq)
total= lambda seq: sum(seq)
top= lambda seq: max(seq)
students = [
    {"name": "Rolf", "grades": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "grades": {2, 7, 9, 22, 10, 5}},
    {"name": "Anna", "grades": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "grades": {19, 20, 12, 7, 3, 5}}
]
operations={
    'average': avg,
    'total': total,
    'top': max
}

for student in students:
    name= student["name"]
    grades= student["grades"]

    print(f"Student: {name}")
    
    operation= input("Enter 'average', 'total' or 'top': ")

    operation_func= operations[operation]
    print(operation_func(grades))
'''    
if operation=='average':
        print(avg(grades))
    elif operation=='total':
        print(total(grades))
    elif operation=='top':
        print(top(grades))
    else:
        print("Wrong choice entered")
'''
