import json

'''
file = open('friends_json.txt', 'r')
file_contents = json.load(file)      #reads file and turns it into a dictionary
file.close()

print(file_contents["friends"][0])
'''
cars=[
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]
file=open('cars_jsn.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string='[{"name": "Alfa Romeo", "released": 1950}]'
inc_car=json.loads(my_json_string)

print(inc_car[0]["name"])