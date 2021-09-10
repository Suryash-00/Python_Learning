'''
currencies= 75, 1.2
INR, USD= currencies
'''
'''
friends= [("Suri", 21), ("Daksh", 21), ("Yash", 22)]
for name, age in friends:
    print(f"{name} is {age} old")
'''
friend_age= {"Suri": 21, "Daksh": 21, "Yash": 22}
for name in friend_age:
    print(name)

friend_age= {"Suri": 21, "Daksh": 21, "Yash": 22}
for name, age in friend_age.items():
    print(f"{name} is {age} years old")