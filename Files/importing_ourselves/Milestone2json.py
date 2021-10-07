import json

books_file='books.txt'
def add_book(name, author):
    with open(books_file, 'a') as file:
        my_string=[{"name": name, "author": author, "read": False}]
        file_contents=json.dump(my_string, file)

def get_all_books():
    file= open('books_file.txt', 'r')
    file.close()
    return file

def mark_book_as_read(name):
    books=get_all_books()
    reads=json.load(books)
    for book in reads:
        if book['name']==name:
            book['read']='True'

def delete_book(name):
    books=get_all_books()
    reads=json.load(books)
    books=[book for book in reads if book['name']!=name]
