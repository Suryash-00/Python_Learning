'''
numbers= [0,2,3,4,5,6]
doubled_numbers= [number*2 for number in numbers]
print(doubled_numbers)
'''
'''
friend_ages= [21, 22, 20, 28]
age_strings= [f"My friend is {age} years old" for age in friend_ages]
print(age_strings)
'''
friend= input("Enter your friend's name")
names= ["Suri", "Ganguly", "Jawline", "Machchli"]
lower= [name.lower() for name in names]
if friend.lower() in lower:
    print(f"{friend.lower()} is your friend")

#use title() for title case and upper() for upper case  