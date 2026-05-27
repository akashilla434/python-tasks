from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import mysql.connector
from datetime import datetime
import uvicorn

# =====================================================
# MYSQL CONNECTION
# =====================================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ROOT",
    database="library_db"
)

cursor = db.cursor(dictionary=True)

# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI()

# =====================================================
# PYDANTIC MODELS
# =====================================================

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    quantity: int
    available: bool

class Student(BaseModel):
    id: int
    name: str
    email: str
    course: str

class IssueBook(BaseModel):
    student_id: int
    book_id: int

# =====================================================
# HOME PAGE
# =====================================================

@app.get("/", response_class=HTMLResponse)
def home():

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    html = """

    <html>

    <head>

        <title>Library Management System</title>

        <style>

            body{
                font-family: Arial;
                margin: 40px;
                background-color: #f2f2f2;
            }

            h1{
                color: darkblue;
            }

            table{
                border-collapse: collapse;
                width: 100%;
                background-color: white;
            }

            th, td{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }

            th{
                background-color: lightgray;
            }

            input{
                padding: 10px;
                margin: 5px;
            }

            button{
                padding: 10px 15px;
                background-color: blue;
                color: white;
                border: none;
                cursor: pointer;
            }

        </style>

    </head>

    <body>

        <h1>Library Management System</h1>

        <h2>Add Book</h2>

        <form action="/add-book" method="post">

            <input type="number" name="id" placeholder="ID" required>

            <input type="text" name="title" placeholder="Title" required>

            <input type="text" name="author" placeholder="Author" required>

            <input type="number" step="0.01" name="price" placeholder="Price" required>

            <input type="number" name="quantity" placeholder="Quantity" required>

            <button type="submit">Add Book</button>

        </form>

        <hr>

        <h2>Books List</h2>

        <table>

            <tr>

                <th>ID</th>
                <th>Title</th>
                <th>Author</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Available</th>

            </tr>

    """

    for book in books:

        html += f"""

        <tr>

            <td>{book['id']}</td>
            <td>{book['title']}</td>
            <td>{book['author']}</td>
            <td>{book['price']}</td>
            <td>{book['quantity']}</td>
            <td>{book['available']}</td>

        </tr>

        """

    html += """

        </table>

    </body>

    </html>

    """

    return html

# =====================================================
# ADD BOOK FROM WEB PAGE
# =====================================================

@app.post("/add-book")
async def add_book_form(request: Request):

    try:

        form = await request.form()

        query = """
        INSERT INTO books(
            id,
            title,
            author,
            price,
            quantity,
            available
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            int(form["id"]),
            form["title"],
            form["author"],
            float(form["price"]),
            int(form["quantity"]),
            1
        )

        cursor.execute(query, values)

        db.commit()

        return HTMLResponse(
            """
            <h2>Book Added Successfully</h2>
            <a href="/">Go Back</a>
            """
        )

    except Exception as e:

        return HTMLResponse(
            f"""
            <h2>Error:</h2>
            <p>{e}</p>
            <a href="/">Go Back</a>
            """
        )

# =====================================================
# GET ALL BOOKS
# =====================================================

@app.get("/books")
def get_books():

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    return books

# =====================================================
# GET BOOK BY ID
# =====================================================

@app.get("/books/{id}")
def get_book(id: int):

    query = "SELECT * FROM books WHERE id=%s"

    cursor.execute(query, (id,))

    book = cursor.fetchone()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    return book

# =====================================================
# UPDATE BOOK
# =====================================================

@app.put("/books/{id}")
def update_book(id: int, book: Book):

    query = """
    UPDATE books
    SET title=%s,
        author=%s,
        price=%s,
        quantity=%s,
        available=%s
    WHERE id=%s
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

    db.commit()

    return {"message": "Book Updated Successfully"}

# =====================================================
# DELETE BOOK
# =====================================================

@app.delete("/books/{id}")
def delete_book(id: int):

    query = "DELETE FROM books WHERE id=%s"

    cursor.execute(query, (id,))

    db.commit()

    return {"message": "Book Deleted Successfully"}

# =====================================================
# ADD STUDENT
# =====================================================

@app.post("/students")
def add_student(student: Student):

    query = """
    INSERT INTO students(name, email, course)
    VALUES (%s, %s, %s)
    """

    values = (
        student.name,
        student.email,
        student.course
    )

    cursor.execute(query, values)

    db.commit()

    return {"message": "Student Added Successfully"}

# =====================================================
# GET STUDENTS
# =====================================================

@app.get("/students")
def get_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    return students

# =====================================================
# ISSUE BOOK
# =====================================================

@app.post("/issue-book")
def issue_book(issue: IssueBook):

    cursor.execute(
        "SELECT * FROM books WHERE id=%s",
        (issue.book_id,)
    )

    book = cursor.fetchone()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    query = """
    INSERT INTO issued_books(
        student_id,
        book_id,
        issue_date,
        returned
    )
    VALUES (%s, %s, %s, %s)
    """

    values = (
        issue.student_id,
        issue.book_id,
        datetime.now(),
        False
    )

    cursor.execute(query, values)

    cursor.execute(
        "UPDATE books SET available=%s WHERE id=%s",
        (False, issue.book_id)
    )

    db.commit()

    return {"message": "Book Issued Successfully"}

# =====================================================
# RETURN BOOK
# =====================================================

@app.post("/return-book/{id}")
def return_book(id: int):

    query = """
    UPDATE issued_books
    SET returned=%s,
        return_date=%s
    WHERE id=%s
    """

    values = (
        True,
        datetime.now(),
        id
    )

    cursor.execute(query, values)

    cursor.execute(
        "SELECT book_id FROM issued_books WHERE id=%s",
        (id,)
    )

    data = cursor.fetchone()

    if data:

        book_id = data["book_id"]

        cursor.execute(
            "UPDATE books SET available=%s WHERE id=%s",
            (True, book_id)
        )

    db.commit()

    return {"message": "Book Returned Successfully"}

# =====================================================
# AVAILABLE BOOKS
# =====================================================

@app.get("/available-books")
def available_books():

    cursor.execute(
        "SELECT * FROM books WHERE available=True"
    )

    books = cursor.fetchall()

    return books

# =====================================================
# ISSUED BOOKS
# =====================================================

@app.get("/issued-books")
def issued_books():

    cursor.execute(
        "SELECT * FROM issued_books"
    )

    books = cursor.fetchall()

    return books

# =====================================================
# SEARCH BOOK
# =====================================================

@app.get("/search-book/{title}")
def search_book(title: str):

    query = """
    SELECT * FROM books
    WHERE title LIKE %s
    """

    cursor.execute(
        query,
        (f"%{title}%",)
    )

    books = cursor.fetchall()

    return books

# =====================================================
# SERVER RUN
# =====================================================

if __name__ == "__main__":

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=5000,
        reload=True
    )