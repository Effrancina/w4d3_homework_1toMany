from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, genre, author, id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author, book.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():  
    books = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)
    for row in results:
        book = Book(row['title'], row['genre'], row['author'], row['id'] )
        books.append(book)
    return books