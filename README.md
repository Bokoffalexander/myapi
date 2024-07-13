# FastAPI

## Эндпоинты:

### default

GET / (index)

### Студенты (динамический параметр)

#### path parameter

GET /get-student/{student_id}

#### query parameter

GET /get-by-name?name=john 

#### path and query parameters

GET GET /get-by-name/{student_id}?name=john 

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
