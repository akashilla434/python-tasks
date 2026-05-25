from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Books Page
@app.route('/books')
def books():
    return render_template('books.html')

# Add Book
@app.route('/add_book', methods=['POST'])
def add_book():

    title = request.form['title']
    author = request.form['author']
    price = request.form['price']

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            price REAL
        )
    """)

    cursor.execute(
        "INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
        (title, author, price)
    )

    conn.commit()
    conn.close()

    return "Book Added Successfully"

if __name__ == '__main__':
    app.run(debug=True)
