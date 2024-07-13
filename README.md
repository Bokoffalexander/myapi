# FastAPI

## Эндпоинты:

### default

GET / (home)

### Студенты

#### выдать всех студентов

GET /get-students

#### path parameter (динамический параметр)

GET /get-student/{student_id}

#### query parameter

GET /get-by-name?name=john 

#### path and query parameters

GET /get-by-name/{student_id}?name=john 

#### post and request body

POST /create-student/{student_id}

body
{
  "name": "San",
  "age": 30,
  "year": "year 19"
}

#### put and update student

PUT /update-student/{student_id}

#### delete student

DELETE /delete-student/{student_id}
