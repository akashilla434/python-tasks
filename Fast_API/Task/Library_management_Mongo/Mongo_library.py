from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import *
from datetime import datetime

# ==================================================
# FASTAPI APP
# ==================================================

app = FastAPI()

# ==================================================
# MONGODB CONNECTION
# ==================================================

MONGO_URL = "mongodb+srv://akashilla434_db_user:nh4S5xaq45BXIQF5@akash.w5c7o82.mongodb.net/library_db?retryWrites=true&w=majority"

'''
mongodb+srv://username:password@clustername.xxxxx.mongodb.net/todo_db?retryWrites=true&w=majority
│              │        │        │                              │
│              │        │        │                              └── Database name
│              │        │        └──────────────────────────────── Cluster URL
│              │        └───────────────────────────────────────── Password
│              └────────────────────────────────────────────────── Username
└───────────────────────────────────────────────────────────────── MongoDB protocal
'''
connect(host=MONGO_URL)
# ==================================================
# MONGODB COLLECTIONS
# ==================================================

# BOOKS COLLECTION
class Book(Document):
    title = StringField(required=True)
    author = StringField()
    price = FloatField()
    quantity = IntField()
    available = BooleanField(default=True)

# STUDENTS COLLECTION
class Student(Document):
    name = StringField()
    email = StringField()
    course = StringField()

# ISSUED BOOKS COLLECTION
class IssuedBook(Document):
    student_id = StringField()
    book_id = StringField()

    issue_date = DateTimeField(default=datetime.utcnow)
    return_date = DateTimeField()

    returned = BooleanField(default=False)

# ==================================================
# Pydantic Models
# ==================================================

class BookSchema(BaseModel):
    title: str
    author: str
    price: float
    quantity: int
    available: bool

class StudentSchema(BaseModel):
    name: str
    email: str
    course: str

class IssueSchema(BaseModel):
    student_id: str
    book_id: str

# ==================================================
# HOME API
# ==================================================

@app.get("/")
def home():
    return {"message": "Library Management System MongoDB"}

# ==================================================
# BOOK APIs
# ==================================================

# ADD BOOK
@app.post("/books")
def add_book(book: BookSchema):

    new_book = Book(
        title=book.title,
        author=book.author,
        price=book.price,
        quantity=book.quantity,
        available=book.available
    )

    new_book.save()

    return {"message": "Book Added Successfully"}

# GET ALL BOOKS
@app.get("/books")
def get_books():

    books = Book.objects()

    data = []

    for book in books:
        data.append({
            "id": str(book.id),
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "quantity": book.quantity,
            "available": book.available
        })

    return data

# GET BOOK BY ID
@app.get("/books/{id}")
def get_book(id: str):

    try:
        book = Book.objects.get(id=id)

        return {
            "id": str(book.id),
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "quantity": book.quantity,
            "available": book.available
        }

    except:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

# UPDATE BOOK
@app.put("/books/{id}")
def update_book(id: str, book: BookSchema):

    try:
        update_book = Book.objects.get(id=id)

        update_book.title = book.title
        update_book.author = book.author
        update_book.price = book.price
        update_book.quantity = book.quantity
        update_book.available = book.available

        update_book.save()

        return {"message": "Book Updated Successfully"}

    except:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

# DELETE BOOK
@app.delete("/books/{id}")
def delete_book(id: str):

    try:
        book = Book.objects.get(id=id)

        book.delete()

        return {"message": "Book Deleted Successfully"}

    except:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

# ==================================================
# STUDENT APIs
# ==================================================

# ADD STUDENT
@app.post("/students")
def add_student(student: StudentSchema):

    new_student = Student(
        name=student.name,
        email=student.email,
        course=student.course
    )

    new_student.save()

    return {"message": "Student Added Successfully"}

# GET ALL STUDENTS
@app.get("/students")
def get_students():

    students = Student.objects()

    data = []

    for student in students:
        data.append({
            "id": str(student.id),
            "name": student.name,
            "email": student.email,
            "course": student.course
        })

    return data

# ==================================================
# ISSUE BOOK
# ==================================================

@app.post("/issue-book")
def issue_book(issue: IssueSchema):

    try:
        book = Book.objects.get(id=issue.book_id)

        issued = IssuedBook(
            student_id=issue.student_id,
            book_id=issue.book_id,
            issue_date=datetime.utcnow(),
            returned=False
        )

        issued.save()

        # book unavailable
        book.available = False
        book.save()

        return {"message": "Book Issued Successfully"}

    except:
        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

# ==================================================
# RETURN BOOK
# ==================================================

@app.post("/return-book/{id}")
def return_book(id: str):

    try:
        issued = IssuedBook.objects.get(id=id)

        issued.returned = True
        issued.return_date = datetime.utcnow()

        issued.save()

        # make book available again
        book = Book.objects.get(id=issued.book_id)

        book.available = True
        book.save()

        return {"message": "Book Returned Successfully"}

    except:
        raise HTTPException(
            status_code=404,
            detail="Issued Book Not Found"
        )

# ==================================================
# AVAILABLE BOOKS
# ==================================================

@app.get("/available-books")
def available_books():

    books = Book.objects(available=True)

    data = []

    for book in books:
        data.append({
            "id": str(book.id),
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "quantity": book.quantity
        })

    return data

# ==================================================
# ISSUED BOOKS
# ==================================================

@app.get("/issued-books")
def issued_books():

    issued = IssuedBook.objects()

    data = []

    for book in issued:
        data.append({
            "id": str(book.id),
            "student_id": book.student_id,
            "book_id": book.book_id,
            "issue_date": book.issue_date,
            "return_date": book.return_date,
            "returned": book.returned
        })

    return data

# ==================================================
# SEARCH BOOK
# ==================================================

@app.get("/search-book/{title}")
def search_book(title: str):

    books = Book.objects(title__icontains=title)

    data = []

    for book in books:
        data.append({
            "id": str(book.id),
            "title": book.title,
            "author": book.author,
            "price": book.price
        })

    return data
