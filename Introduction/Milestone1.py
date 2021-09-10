# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def movie_Add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


# Create other functions for:
#   - listing movies
def movie_Listing():
    print(movies)

#   - finding movies
def movie_Find():
    name=input("Enter the title of the movie you want to search")
    for movie in movies:
        if movie['title']==name:
            print(movie)

# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            movie_Add()
        elif selection == "l":
            movie_Listing()
        elif selection == "f":
            movie_Find()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()
# Remember to run the user menu function at the end!