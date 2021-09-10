friends= ["Suri", "Yash", "daksh", "pIYUSH"]
guests= ["Bhanu", "baba", "Daksh", "Suri"]
friends_lower= {friend.lower() for friend in friends}
guests_lower= {guest.lower() for guest in guests}

present_friends= friends_lower.intersection(guests_lower)
present_friends= {name.title() for name in present_friends}
print(present_friends)

long_time_no_see= [3,5,7,9]
long_time= {
    friends[i]: long_time_no_see[i]
    for i in range(len(friends))
}
print(long_time)