from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from mongoengine import (
    Document,
    StringField,
    IntField,
    FloatField,
    connect
)

import uvicorn
import os

# ==================================================
# FASTAPI APP
# ==================================================

app = FastAPI()

# ==================================================
# BASE DIRECTORY
# ==================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==================================================
# STATIC FILES
# ==================================================

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# ==================================================
# TEMPLATES
# ==================================================

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

# ==================================================
# MONGODB CONNECTION
# ==================================================

MONGO_URL = "mongodb+srv://akashilla434_db_user:nh4S5xaq45BXIQF5@akash.w5c7o82.mongodb.net/library_management?retryWrites=true&w=majority"

connect(host=MONGO_URL)

# ==================================================
# BOOK COLLECTION
# ==================================================

class Book(Document):

    id = IntField(primary_key=True)

    name = StringField(required=True)

    author = StringField(required=True)

    price = FloatField(required=True)

    status = StringField(default="available")

# ==================================================
# HOME PAGE
# ==================================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    books = Book.objects()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "books": books
        }
    )

# ==================================================
# ADD BOOK
# ==================================================

@app.post("/add-book")
def add_book(

    id: int = Form(...),

    name: str = Form(...),

    author: str = Form(...),

    price: float = Form(...)

):

    existing_book = Book.objects(id=id).first()

    if not existing_book:

        book = Book(

            id=id,

            name=name,

            author=author,

            price=price

        )

        book.save()

    return RedirectResponse(
        url="/",
        status_code=303
    )

# ==================================================
# DELETE BOOK
# ==================================================

@app.get("/delete/{book_id}")
def delete_book(book_id: int):

    book = Book.objects(id=book_id).first()

    if book:

        book.delete()

    return RedirectResponse(
        url="/",
        status_code=303
    )

# ==================================================
# SERVER
# ==================================================

if __name__ == "__main__":

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=5000,
        reload=True
    )