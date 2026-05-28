from flask import Flask, render_template, request, redirect, session, send_file
import mysql.connector
from datetime import date
import qrcode
import os

app = Flask(__name__)
app.secret_key = "library123"

# ================= DATABASE =================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ROOT",
    database="library_management"
)

cursor = db.cursor()

# ================= LOGIN =================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        cursor.execute(
            "SELECT * FROM students WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cursor.fetchone()

        if user:
            session["user"] = user[1]
            session["id"] = user[0]

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid Email or Password"
        )

    return render_template("login.html")


# ================= DASHBOARD =================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        user=session["user"]
    )


# ================= BOOKS =================

@app.route("/books")
def books():

    if "user" not in session:
        return redirect("/")

    search = request.args.get("search")

    if search:

        cursor.execute("""
            SELECT * FROM books
            WHERE title LIKE %s
            OR author LIKE %s
        """, ("%" + search + "%", "%" + search + "%"))

    else:

        cursor.execute("SELECT * FROM books")

    data = cursor.fetchall()

    return render_template(
        "books.html",
        books=data
    )


# ================= ADD BOOK =================

@app.route("/add_book", methods=["POST"])
def add_book():

    if "user" not in session:
        return redirect("/")

    title = request.form.get("title")
    author = request.form.get("author")
    price = request.form.get("price")
    quantity = request.form.get("quantity")

    cursor.execute("""
        INSERT INTO books
        (title, author, price, quantity, available)
        VALUES(%s,%s,%s,%s,%s)
    """, (title, author, price, quantity, quantity))

    db.commit()

    return redirect("/books")


# ================= ISSUE BOOK =================

@app.route("/issue/<int:id>")
def issue(id):

    if "user" not in session:
        return redirect("/")

    today = date.today()
    student_id = session["id"]

    cursor.execute(
        "SELECT available FROM books WHERE id=%s",
        (id,)
    )

    result = cursor.fetchone()

    if result and result[0] > 0:

        cursor.execute("""
            UPDATE books
            SET available = available - 1
            WHERE id=%s
        """, (id,))

        cursor.execute("""
            INSERT INTO transactions
            (book_id, student_id, issue_date)
            VALUES(%s,%s,%s)
        """, (id, student_id, today))

        db.commit()

    return redirect("/books")


# ================= RETURN BOOK =================

@app.route("/return/<int:id>")
def return_book(id):

    if "user" not in session:
        return redirect("/")

    today = date.today()

    cursor.execute("""
        SELECT issue_date
        FROM transactions
        WHERE book_id=%s
        ORDER BY id DESC
        LIMIT 1
    """, (id,))

    result = cursor.fetchone()

    fine = 0

    if result:

        issue_date = result[0]

        days = (today - issue_date).days

        if days > 7:
            fine = (days - 7) * 10

    cursor.execute("""
        UPDATE books
        SET available = available + 1
        WHERE id=%s
    """, (id,))

    cursor.execute("""
        UPDATE transactions
        SET return_date=%s,
            fine=%s
        WHERE book_id=%s
        ORDER BY id DESC
        LIMIT 1
    """, (today, fine, id))

    db.commit()

    return redirect("/books")


# ================= QR CODE =================

@app.route("/qr/<int:id>")
def qr(id):

    if "user" not in session:
        return redirect("/")

    if not os.path.exists("static"):
        os.makedirs("static")

    img = qrcode.make(f"BOOK ID : {id}")

    path = f"static/qr_{id}.png"

    img.save(path)

    return send_file(path, mimetype="image/png")


# ================= DELETE BOOK =================

@app.route("/delete/<int:id>")
def delete(id):

    if "user" not in session:
        return redirect("/")

    cursor.execute(
        "DELETE FROM books WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect("/books")


# ================= STUDENTS =================

@app.route("/students")
def students():

    if "user" not in session:
        return redirect("/")

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    return render_template(
        "students.html",
        students=data
    )
# ================= ADD STUDENT =================

@app.route("/add_student", methods=["POST"])
def add_student():

    if "user" not in session:
        return redirect("/")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    department = request.form.get("department")
    student_year = request.form.get("year")

    cursor.execute("""
        INSERT INTO students
        (name, email, password, department, student_year)
        VALUES(%s,%s,%s,%s,%s)
    """, (name, email, password, department, student_year))

    db.commit()

    return redirect("/students")
    
# ================= REPORTS =================

@app.route("/reports")
def reports():

    if "user" not in session:
        return redirect("/")

    cursor.execute("""
        SELECT books.title,
               students.name,
               transactions.issue_date,
               transactions.return_date,
               transactions.fine
        FROM transactions
        JOIN books
        ON books.id = transactions.book_id
        JOIN students
        ON students.id = transactions.student_id
    """)

    data = cursor.fetchall()

    return render_template(
        "reports.html",
        reports=data
    )


# ================= LOGOUT =================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# ================= SERVER =================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
