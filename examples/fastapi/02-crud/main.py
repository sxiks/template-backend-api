from typing import List

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Example 02 - CRUD Operations",
    version="1.0.0",
)

# ------------------------------------------------------------------
# Mock Database
# ------------------------------------------------------------------

students_db = []
student_id_counter = 1


# ------------------------------------------------------------------
# Schemas
# ------------------------------------------------------------------

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int
    is_active: bool


# ------------------------------------------------------------------
# Create
# ------------------------------------------------------------------

@app.post(
    "/api/v1/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(student: StudentCreate):

    global student_id_counter

    new_student = {
        "id": student_id_counter,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "email": student.email,
        "is_active": True,
    }

    students_db.append(new_student)
    student_id_counter += 1

    return new_student


# ------------------------------------------------------------------
# Read All
# ------------------------------------------------------------------

@app.get(
    "/api/v1/students",
    response_model=List[StudentResponse],
)
async def get_students():

    return students_db


# ------------------------------------------------------------------
# Read One
# ------------------------------------------------------------------

@app.get(
    "/api/v1/students/{student_id}",
    response_model=StudentResponse,
)
async def get_student(student_id: int):

    for student in students_db:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found",
    )


# ------------------------------------------------------------------
# Delete
# ------------------------------------------------------------------

@app.delete(
    "/api/v1/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student(student_id: int):

    for index, student in enumerate(students_db):

        if student["id"] == student_id:
            del students_db[index]
            return

    raise HTTPException(
        status_code=404,
        detail="Student not found",
    )
