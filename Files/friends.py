friends=input("Enter the names of your three friends seperated by commas only (no spaces):").split(",")

people=open('people.txt', 'r')
people_nearby=[line.strip() for line in people.readlines()]
people.close()

friends_set=set(friends)
people_nearby_set=set(people_nearby)
friends_nearby=friends_set.intersection(people_nearby_set)

nearby_friends_file=open('nearby_friends.txt', 'w')

for friend in friends_nearby:
    print(f"{friend} is nearby!")
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()