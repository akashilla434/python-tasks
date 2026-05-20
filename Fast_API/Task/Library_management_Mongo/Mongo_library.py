from fastapi import FastAPI
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()
MONGO_URL = "mongodb+srv://akashilla434_db_user:nh4S5xaq45BXIQF5@akash.w5c7o82.mongodb.net/library_db?retryWrites=true&w=majority"

'''
mongodb+srv://username:password@clustername.xxxxx.mongodb.net/todo_db?retryWrites=true&w=majority
│              │        │        │                              │
│              │        │        │                              └── Database name
│              │        │        └──────────────────────────────── Cluster URL
│              │        └───────────────────────────────────────── Password
│              └────────────────────────────────────────────────── Username
└───────────────────────────────────────────────────────────────── MongoDB protocol
'''
# MongoDB Connection
client = MongoClient(MONGO_URL)

# Database
db = client["library_db"]

# Collection
books = db["books"]


# Home
@app.get("/")
def home():
    return {"message": "Library Management Mongo Running"}


# Add Book
@app.post("/books")
def add_book(name: str, author: str, price: int):

    book = {
        "name": name,
        "author": author,
        "price": price,
        "status": "available"
    }

    books.insert_one(book)

    return {"message": "Book Added"}


# Get All Books
@app.get("/books")
def get_books():

    data = []

    for book in books.find():

        data.append({
            "id": str(book["_id"]),
            "name": book["name"],
            "author": book["author"],
            "price": book["price"],
            "status": book["status"]
        })

    return data


# Get Book id
@app.get("/books/{id}")
def get_book(id: str):

    book = books.find_one({"_id": ObjectId(id)})

    if not book:
        return {"error": "Book not found"}

    return {
        "id": str(book["_id"]),
        "name": book["name"],
        "author": book["author"],
        "price": book["price"],
        "status": book["status"]
    }


# Update Book
@app.put("/books/{id}")
def update_book(id: str, name: str, author: str, price: int):

    books.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": name,
                "author": author,
                "price": price
            }
        }
    )

    return {"message": "Book Updated"}


# Delete Book
@app.delete("/books/{id}")
def delete_book(id: str):

    books.delete_one({"_id": ObjectId(id)})

    return {"message": "Book Deleted"}


# Issue Book
@app.post("/issue-book/{id}")
def issue_book(id: str):

    books.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "status": "issued"
            }
        }
    )

    return {"message": "Book Issued"}


# Return Book
@app.post("/return-book/{id}")
def return_book(id: str):

    books.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "status": "available"
            }
        }
    )

    return {"message": "Book Returned"}


# Available Books
@app.get("/available-books")
def available_books():

    data = []

    for book in books.find({"status": "available"}):

        data.append({
            "id": str(book["_id"]),
            "name": book["name"]
        })

    return data


# Issued Books
@app.get("/issued-books")
def issued_books():

    data = []

    for book in books.find({"status": "issued"}):

        data.append({
            "id": str(book["_id"]),
            "name": book["name"]
        })

    return data


#  search Book 
@app.get("/search-book/{title}")
def search_book(title: str):

    data = []

    for book in books.find(
        {
            "name": {
                "$regex": title,
                "$options": "i"
            }
        }
    ):

        data.append({
            "id": str(book["_id"]),
            "name": book["name"],
            "author": book["author"],
            "price": book["price"],
            "status": book["status"]
        })

    return data
