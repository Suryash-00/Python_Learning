import csv
movies = [
    {"name": "The Matrix", "director": "Wockowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
]
'''
def write_to_file(output):
    with open("movies.csv", "w") as f:
        f.write("name", "director \n")
        for line in output:
            f.write(f"{line['name']}, {line['director']}\n")
'''
# OR
'''
def write_to_file(output):
    with open("movies.csv", "w") as f:
        writer=csv.writer(f)
        f.write("name", "director \n")
        writer.writerows([elem.values() for elem in output])
'''
# OR


def write_to_file(output):
    with open("movies.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "director"])
        writer.writeheader()
        writer.writerows(output)


def read_from_file():
    with open("movies.csv", "r") as f:
        '''
        content=f.readlines()
        for line in content[1:]:
            column=line.strip().split(",")
            print(f"Name: {column[0]}\t Director:{column[1]}")
'''
        # OR
        '''
        reader=csv.reader(f)
        for line in reader:
            print(f"Name: {line[0]}\t Director: {line[1]}")
'''
        # OR
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']}\t Director: {line['director']}")
