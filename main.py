from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from schemas import StudentCreate  # Import from schemas.py

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World"}


@app.post("/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(name=student.name, age=student.age, course=student.course)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/students/")
def read_all_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    existing_student = db.query(Student).filter(Student.id == student_id).first()
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.course = student.course
    db.commit()
    db.refresh(existing_student)
    return existing_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
