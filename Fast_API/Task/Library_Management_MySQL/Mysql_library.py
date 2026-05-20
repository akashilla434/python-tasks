from fastapi import FastAPI
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ROOT",
    database="library"
)

# Home
@app.get("/")
def home():
    return {"message": "Library Running"}

# Add Book
@app.post("/books")
def add_book(name: str, author: str, price: int):

    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO books(name, author, price) VALUES(%s,%s,%s)",
        (name, author, price)
    )

    db.commit()

    return {"message": "Book Added"}

# Get Books
@app.get("/books")
def get_books():

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM books")

    return cursor.fetchall()

# Update Book
@app.put("/books/{id}")
def update_book(id: int, name: str, author: str, price: int):

    cursor = db.cursor()

    cursor.execute(
        "UPDATE books SET name=%s, author=%s, price=%s WHERE id=%s",
        (name, author, price, id)
    )

    db.commit()

    return {"message": "Book Updated"}

# Delete Book
@app.delete("/books/{id}")
def delete_book(id: int):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id=%s",
        (id,)
    )

    db.commit()

    return {"message": "Book Deleted"}
# Issue Book
@app.post("/issue-book/{id}")
def issue_book(id: int):

    cursor = db.cursor()

    cursor.execute(
        "UPDATE books SET status='issued' WHERE id=%s",
        (id,)
    )

    db.commit()

    return {"message": "Book Issued"}


# Return Book
@app.post("/return-book/{id}")
def return_book(id: int):

    cursor = db.cursor()

    cursor.execute(
        "UPDATE books SET status='available' WHERE id=%s",
        (id,)
    )

    db.commit()

    return {"message": "Book Returned"}


# Available Books
@app.get("/available-books")
def available_books():

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM books WHERE status='available'"
    )

    return cursor.fetchall()


# Issued Books
@app.get("/issued-books")
def issued_books():

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM books WHERE status='issued'"
    )

    return cursor.fetchall()

# Search Book
@app.get("/search-book/{name}")
def search_book(name: str):

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM books WHERE name LIKE %s",
        ("%" + name + "%",)
    )

    books = cursor.fetchall()

    return books












