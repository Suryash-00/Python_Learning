import json

json_list=[]

csv_file=open('football_club.txt', 'r')
lines=csv_file.readlines()

for line in lines:
    club, city, country=line.strip().split(',')
    data={
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)
csv_file.close()

json_file=open('football_convert.txt', 'w')
json.dump(json_list, json_file)
json_file.close()