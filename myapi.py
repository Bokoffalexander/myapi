from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

# path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path( description="Введите id студента", gt=0, lt=3)):
    return students[student_id]

# query parameter
@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}
