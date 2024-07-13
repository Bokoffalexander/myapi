from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def index():
    return {"name": "First Data"}

# path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path( 
		description="Введите id студента", 
		gt=0,
		lt=4)
		):
    return students[student_id]

# query parameter
@app.get("/get-by-name")
def get_student(name: Optional[str]=None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# path and query parameters
@app.get("/get-by-name/{student_id}")
def get_student(student_id: int, name: str):
    if students[student_id]["name"] == name:
        return {"Data": "Correct name"}
    return {"Data": "Not correct student_id or name"}

# post and request body
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]
