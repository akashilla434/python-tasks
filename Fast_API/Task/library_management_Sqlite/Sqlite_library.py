from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime

# =====================================================
# SQLITE CONNECTION
# =====================================================

conn = sqlite3.connect("library.db", check_same_thread=False)

cursor = conn.cursor()

# =====================================================
# CREATE TABLES
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    price REAL,
    quantity INTEGER,
    available BOOLEAN
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    book_id INTEGER,
    issue_date TEXT,
    return_date TEXT,
    returned BOOLEAN
)
""")

conn.commit()

# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI()

# =====================================================
# Pydantic Models
# =====================================================

class Book(BaseModel):
    title: str
    author: str
    price: float
    quantity: int
    available: bool

class Student(BaseModel):
    name: str
    email: str
    course: str

class IssueBook(BaseModel):
    student_id: int
    book_id: int

# =====================================================
# HOME API
# =====================================================

@app.get("/")
def home():
    return {"message": "Library Management SQLite"}

# =====================================================
# BOOK APIs
# =====================================================

# ADD BOOK
@app.post("/books")
def add_book(book: Book):

    query = """
    INSERT INTO books
    (title, author, price, quantity, available)
    VALUES (?, ?, ?, ?, ?)
    """

    values = (
        book.title,
        book.author,
        book.price,
        book.quantity,
        book.available
    )

    cursor.execute(query, values)

    conn.commit()

    return {"message": "Book Added Successfully"}

# GET ALL BOOKS
@app.get("/books")
def get_books():

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    data = []

    for book in books:
        data.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "price": book[3],
            "quantity": book[4],
            "available": book[5]
        })

    return data

# GET BOOK BY ID
@app.get("/books/{id}")
def get_book(id: int):

    query = "SELECT * FROM books WHERE id=?"

    cursor.execute(query, (id,))

    book = cursor.fetchone()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    return {
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "price": book[3],
        "quantity": book[4],
        "available": book[5]
    }

# UPDATE BOOK
@app.put("/books/{id}")
def update_book(id: int, book: Book):

    query = """
    UPDATE books
    SET title=?,
    author=?,
    price=?,
    quantity=?,
    available=?
    WHERE id=?
    """

    values = (
        book.title,
        book.author,
        book.price,
        book.quantity,
        book.available,
        id
    )

    cursor.execute(query, values)

    conn.commit()

    return {"message": "Book Updated Successfully"}

# DELETE BOOK
@app.delete("/books/{id}")
def delete_book(id: int):

    query = "DELETE FROM books WHERE id=?"

    cursor.execute(query, (id,))

    conn.commit()

    return {"message": "Book Deleted Successfully"}

# =====================================================
# STUDENT APIs
# =====================================================

# ADD STUDENT
@app.post("/students")
def add_student(student: Student):

    query = """
    INSERT INTO students
    (name, email, course)
    VALUES (?, ?, ?)
    """

    values = (
        student.name,
        student.email,
        student.course
    )

    cursor.execute(query, values)

    conn.commit()

    return {"message": "Student Added Successfully"}

# GET ALL STUDENTS
@app.get("/students")
def get_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    data = []

    for student in students:
        data.append({
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "course": student[3]
        })

    return data

# =====================================================
# ISSUE BOOK
# =====================================================

@app.post("/issue-book")
def issue_book(issue: IssueBook):

    query = """
    INSERT INTO issued_books
    (student_id, book_id, issue_date, returned)
    VALUES (?, ?, ?, ?)
    """

    values = (
        issue.student_id,
        issue.book_id,
        str(datetime.now()),
        False
    )

    cursor.execute(query, values)

    # update available false
    cursor.execute(
        "UPDATE books SET available=? WHERE id=?",
        (False, issue.book_id)
    )

    conn.commit()

    return {"message": "Book Issued Successfully"}

# =====================================================
# RETURN BOOK
# =====================================================

@app.post("/return-book/{id}")
def return_book(id: int):

    # update issued book
    query = """
    UPDATE issued_books
    SET returned=?,
    return_date=?
    WHERE id=?
    """

    values = (
        True,
        str(datetime.now()),
        id
    )

    cursor.execute(query, values)

    # get book id
    cursor.execute(
        "SELECT book_id FROM issued_books WHERE id=?",
        (id,)
    )

    data = cursor.fetchone()

    if data:

        book_id = data[0]

        cursor.execute(
            "UPDATE books SET available=? WHERE id=?",
            (True, book_id)
        )

    conn.commit()

    return {"message": "Book Returned Successfully"}

# =====================================================
# AVAILABLE BOOKS
# =====================================================

@app.get("/available-books")
def available_books():

    cursor.execute(
        "SELECT * FROM books WHERE available=1"
    )

    books = cursor.fetchall()

    data = []

    for book in books:
        data.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "price": book[3]
        })

    return data

# =====================================================
# ISSUED BOOKS
# =====================================================

@app.get("/issued-books")
def issued_books():

    cursor.execute(
        "SELECT * FROM issued_books"
    )

    books = cursor.fetchall()

    data = []

    for book in books:
        data.append({
            "id": book[0],
            "student_id": book[1],
            "book_id": book[2],
            "issue_date": book[3],
            "return_date": book[4],
            "returned": book[5]
        })

    return data

# =====================================================
# SEARCH BOOK
# =====================================================

@app.get("/search-book/{title}")
def search_book(title: str):

    query = """
    SELECT * FROM books
    WHERE title LIKE ?
    """

    cursor.execute(query, ('%' + title + '%',))

    books = cursor.fetchall()

    data = []

    for book in books:
        data.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "price": book[3]
        })

    return data
