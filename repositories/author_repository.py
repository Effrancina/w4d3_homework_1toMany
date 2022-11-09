from db.run_sql import run_sql
from models.author import Author
from models.book import Book


def save(author):
    sql = "INSERT INTO authors (full_name) VALUES (%s) RETURNING *"
    values = [author.full_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    for row in results:
        author = Author(row['full_name'], row['id'] )
        authors.append(author)
    return authors