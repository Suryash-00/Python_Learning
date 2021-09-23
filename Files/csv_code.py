file=open('D:\Python_Bootcamp\Files\csv_Data.txt', 'r')
lines=file.readlines()
file.close()

lines=[line.strip() for line in lines[1:]]

for line in lines:
    person_data=line.split(',')
    name=person_data[0].title()
    age=person_data[1]
    location=person_data[2].title()
    branch=person_data[3].upper()

    print(f"{name} is {age} and is in {branch} from {location}.")

sample_csv_value=':'.join(['Sagar', '30', 'LPS', 'Designing'])
print(sample_csv_value)