from fastapi import FastAPI

app = FastAPI()

books = []

# Home
@app.get("/")
def home():
    return {"message": "Library Management System"}

# Add Book
@app.post("/books")
def add_book(book: dict):

    books.append(book)

    return {
        "message": "Book Added",
        "data": book
    }

# Get All Books
@app.get("/books")
def get_books():

    return books

# Get Book By ID
@app.get("/books/{id}")
def get_book(id: int):

    for book in books:

        if book["id"] == id:
            return book

    return {"message": "Book not found"}

# Update Book
@app.put("/books/{id}")
def update_book(id: int, updated_book: dict):

    for index, book in enumerate(books):

        if book["id"] == id:

            books[index] = updated_book

            return {
                "message": "Book Updated"
            }

    return {"message": "Book not found"}

# Delete Book
@app.delete("/books/{id}")
def delete_book(id: int):

    for index, book in enumerate(books):

        if book["id"] == id:

            books.pop(index)

            return {
                "message": "Book Deleted"
            }

    return {"message": "Book not found"}

# Issue Book
@app.post("/issue-book/{id}")
def issue_book(id: int):

    for book in books:

        if book["id"] == id:

            book["issued"] = True

            return {
                "message": "Book Issued"
            }

    return {"message": "Book not found"}

# Return Book
@app.post("/return-book/{id}")
def return_book(id: int):

    for book in books:

        if book["id"] == id:

            book["issued"] = False

            return {
                "message": "Book Returned"
            }

    return {"message": "Book not found"}

# Available Books
@app.get("/available-books")
def available_books():

    available = []

    for book in books:

        if book["issued"] == False:

            available.append(books)

    return available

# get Issued Books
@app.get("/get-issued-books")
def get_issued_books():

    issued = []

    for book in books:

        if book["get_issued"] == True:

            issued.append(book)

    return get_issued

# Search Book By Title
@app.get("/search-book/{title}")
def search_book(title: str):

    result = []

    for book in books:

        if title.lower() in book["title"].lower():

            result.append(book)

    return result
