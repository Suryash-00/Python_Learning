'''
ages= [21, 20, 28, 22, 21]
odds= [age for age in ages if age%2==1]
print(odds)
'''
friends= ["Suri", "Yash", "daksh", "pIYUSH"]
guests= ["Bhanu", "baba", "Daksh", "Suri"]
friends_lower= [friend.lower() for friend in friends]
guests_lower= [guest.lower() for guest in guests ]

present_friends= [
    name.title() 
    for name in guests_lower 
    if name in friends_lower
]
print(present_friends)
