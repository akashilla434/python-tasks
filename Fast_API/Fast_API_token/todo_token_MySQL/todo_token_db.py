# ============================================================
#  IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional

# ============================================================
#  FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
#  JWT CONFIGURATION
# ============================================================

SECRET_KEY = "Akash@2207"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE = timedelta(minutes=10)

# ============================================================
#  MYSQL DATABASE
# ============================================================

DATABASE_URL = "mysql+pymysql://root:ROOT@localhost:3306/student_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ============================================================
#  DATABASE TABLE
# ============================================================

class StudentDB(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    course = Column(String(255))
    age = Column(Integer)

# Create Table
Base.metadata.create_all(bind=engine)

# ============================================================
#  PYDANTIC MODEL
# ============================================================

class Student(BaseModel):

    id: Optional[int] = None
    name: str
    course: str
    age: int

    class Config:
        orm_mode = True

# ============================================================
# LOGIN MODEL
# ============================================================

class Login(BaseModel):

    username: str
    password: str

# ============================================================
#  LOGIN SCHEMA
# ============================================================

users = {
    "admin": "admin123",
    "akash": "1234"
}

# ============================================================
#  DATABASE SESSION
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ============================================================
#  CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

# ============================================================
#  TOKEN VALIDATION
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
#  HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Student Management System Running "
    }

# ============================================================
# LOGIN API
# ============================================================

@app.post("/login")
def login(user: Login):

    if user.username not in users:

        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if users[user.username] != user.password:

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# ============================================================
#  CREATE STUDENT
# ============================================================

@app.post("/students")
def create_student(
    student: Student,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    existing = db.query(StudentDB).filter(
        StudentDB.id == student.id
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = StudentDB(
        id=student.id,
        name=student.name,
        course=student.course,
        age=student.age
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return {
        "message": "Student added successfully",
        "data": new_student
    }

# ============================================================
#  GET ALL STUDENTS
# ============================================================

@app.get("/students")
def get_students(
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    students = db.query(StudentDB).all()

    return {
        "count": len(students),
        "data": students
    }

# ============================================================
# GET SINGLE STUDENT
# ============================================================

@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

# ============================================================
# UPDATE STUDENT
# ============================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated: Student,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated.name
    student.course = updated.course
    student.age = updated.age

    db.commit()

    db.refresh(student)

    return {
        "message": "Student updated successfully",
        "data": student
    }

# ============================================================
#  DELETE STUDENT
# ============================================================

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }








