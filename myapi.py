from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# наше приложение обьект FastAPI
app = FastAPI()

# словарь куда будем добавлять обьекты класса Student
students = {}

# класс Student
class Student(BaseModel):
    name: str
    age: int
    year: str

# создадим Тестовый класс Студентов
class TestStudent():
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year

# создадим обьект Тестового Студента
obj = TestStudent("john", 17, "year 12")

# добавим обьект класса TestStudent в словарь students
students[1] = obj

# класс UpdateStudent для обновления данных по студенту
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# Создадим CRUD эндпоинтов
# корень home
@app.get("/")
def home():
    return {"name": "First Data"}

# a dictionary of all students
@app.get("/get-students")
def get_students():
    return students

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
def get_student(a_name: Optional[str]=None):
    for student_id in students:
        if students[student_id].name == a_name:
            return students[student_id]
    return {"Data": "Not Found"}

# path and query parameters
@app.get("/get-by-name/{student_id}")
def get_student(student_id: int, a_name: str):
    if students[student_id].name == a_name:
        return {"Data": "Correct name"}
    return {"Data": "Not correct student_id or name"}

# post and request body
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

# put and Update student
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "No such student"}

    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]

# delete student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "No such student"}

    del students[student_id]
    return {"Message": "Student successfully deleted"}
