from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    FloatField,
    BooleanField
)

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
# DATABASE MODEL
# ==================================================

class BookStore(Document):

    id = IntField(primary_key=True)

    title = StringField

    category = StringField

    author = StringField

    price = FloatField

    available = BooleanField(default=True)

# ==================================================
# PYDANTIC MODEL
# ==================================================

class Book(BaseModel):

    id: int
    title: str
    category: str
    author: str
    price: float
    available: bool

# ==================================================
# HOME API
# ==================================================

@app.get("/")
def home():

    return {
        "message": "Library Management Running"
    }

# ==================================================
# ADD BOOK
# ==================================================

@app.post("/add-book")
def add_book(book: Book):

    check = BookStore.objects(id=book.id).first()

    if check:
        raise HTTPException(
            status_code=400,
            detail="Book ID already exists"
        )

    new_book = BookStore(
        id=book.id,
        title=book.title,
        category=book.category,
        author=book.author,
        price=book.price,
        available=book.available
    )

    new_book.save()

    return {
        "message": "Book Added Successfully"
    }

# ==================================================
# GET ALL BOOKS
# ==================================================

@app.get("/all-books")
def all_books():

    books = BookStore.objects()

    data = []

    for book in books:

        data.append({
            "id": book.id,
            "title": book.title,
            "category": book.category,
            "author": book.author,
            "price": book.price,
            "available": book.available
        })

    return {
        "total_books": len(data),
        "books": data
    }

# ==================================================
# GET SINGLE BOOK
# ==================================================

@app.get("/book/{book_id}")
def get_book(book_id: int):

    book = BookStore.objects(id=book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "id": book.id,
        "title": book.title,
        "category": book.category,
        "author": book.author,
        "price": book.price,
        "available": book.available
    }

# ==================================================
# UPDATE BOOK
# ==================================================

@app.put("/update-book/{book_id}")
def update_book(book_id: int, updated: Book):

    book = BookStore.objects(id=book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.title = updated.title
    book.category = updated.category
    book.author = updated.author
    book.price = updated.price
    book.available = updated.available

    book.save()

    return {
        "message": "Book Updated Successfully"
    }

# ==================================================
# DELETE BOOK
# ==================================================

@app.delete("/delete-book/{book_id}")
def delete_book(book_id: int):

    book = BookStore.objects(id=book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.delete()

    return {
        "message": "Book Deleted Successfully"
    }

# ==================================================
# SEARCH BOOK
# ==================================================

@app.get("/search-book/{title}")
def search_book(title: str):

    books = BookStore.objects(
        title__icontains=title
    )

    data = []

    for book in books:

        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author
        })

    return {
        "count": len(data),
        "books": data
    }
