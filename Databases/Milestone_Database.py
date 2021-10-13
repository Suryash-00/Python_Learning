import sqlite3

def create_book_table():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()

    cursor.execute('CREATE TABLE books (name text, author text, read integer)')
    connection.commit()
    connection.close()

def add_book(name, author):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    ''' 
    cursor.execute(f'INSERT INTO books VALUES ("{name}", "{author}", 0)')
    '''
    cursor.execute('INSERT INTO Books VALUES (?, ?, 0)', (name, author))
    connection.commit()
    connection.close()

def get_all_books():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()

    cursor.execute('SELECT * FROM books')
    # books=cursor.fetchall()       This will convert the table into a list of tuples
    books=[{'name': row[0], 'author':row[1], 'read': row[2]} for row in cursor.fetchall()]
    # This is to save data in the form of list of dictionaries.
    connection.close()

    return books

def mark_book_as_read(name):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
    connection.commit()
    connection.close()

def delete_book(name):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))
    connection.commit()
    connection.close()