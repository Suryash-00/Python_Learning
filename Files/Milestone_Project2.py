from importing_ourselves import Milestone2json

USER_CHOICE= '''
Enter:
- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:
'''
def menu():
    #Milestone2json.create_book_table()
    user_input=input(USER_CHOICE)
    while user_input!='q':
        if user_input=='a':
            prompt_add_book()
        elif user_input=='l':
            list_book()
        elif user_input=='r':
            prompt_read_book()
        elif user_input=='d':
            prompt_delete_book()
        else:
            print("Unknown Command. Please try again.")
        user_input=input(USER_CHOICE)

def prompt_add_book():
    name=input("Enter the new book name")
    author=input("Enter it's author")

    Milestone2json.add_book(name, author)

def list_book():
    books=Milestone2json.get_all_books()
    for book in books:
        print(book)

def prompt_read_book():
    name=input("Enter the name of the book you finished reading:")

    Milestone2json.mark_book_as_read(name)

def prompt_delete_book():
    name=input("Enter the book name you finished reading:")

    Milestone2json.delete_book(name)

menu()