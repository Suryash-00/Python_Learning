movies= [
    {"name": "Kal Ho Na Ho", "director": "Karan Johar"},
    {"name": "Tamasha", "director": "Imtiaz Ali Khan"},
    {"name": "Bombay Velvet", "director": "Anurag Kashyap"},
    {"name": "Barfi", "director": "Anurag Basu"}
]

def find_movie(expected, finder):
    for movie in movies:
        if finder(movie)==expected:
            return movie

find_by= input("What property are you looking for?")
looking_for= input("What are you looking for?")

movie= find_movie(looking_for, lambda movie: movie[find_by])
print(movie)