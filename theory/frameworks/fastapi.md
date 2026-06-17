# FastAPI

## Overview

FastAPI is a modern Python framework for building APIs.

It is designed around:

* High performance
* Type safety
* Automatic documentation
* Developer productivity

FastAPI leverages Python type hints to provide request validation, serialization, dependency injection, and OpenAPI documentation generation.

Official documentation:

https://fastapi.tiangolo.com/

---

# Why Use FastAPI?

FastAPI is an excellent choice when building:

* REST APIs
* Microservices
* Internal APIs
* Backend services
* AI and Machine Learning APIs
* Data-driven applications

Benefits include:

* Excellent performance
* Automatic OpenAPI documentation
* Strong typing
* Built-in validation
* Dependency injection
* Modern Python ecosystem support

---

# FastAPI and Template Architecture

Within the `template-backend-api` architecture:

```text
src/
├── api/
├── core/
├── models/
├── services/
└── utils/
```

FastAPI maps naturally to the layered design.

---

## API Layer

Location:

```text
src/api/v1/
```

Responsibilities:

* Route definitions
* Request validation
* Response formatting
* HTTP status codes

Example:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return []
```

---

## Service Layer

Location:

```text
src/services/
```

Responsibilities:

* Business rules
* Application workflows
* Coordination between components

Example:

```python
class UserService:

    def get_all_users(self):
        return []
```

Routes should call services instead of implementing business logic directly.

---

## Model Layer

Location:

```text
src/models/
```

Responsibilities:

* ORM models
* Data schemas
* Database interactions

Common tools:

* SQLAlchemy
* SQLModel
* Tortoise ORM

Example:

```python
class User(Base):
    __tablename__ = "users"
```

---

## Core Layer

Location:

```text
src/core/
```

Responsibilities:

* Configuration
* Logging
* Middleware
* Dependency injection
* Exception handling

---

## Utils Layer

Location:

```text
src/utils/
```

Responsibilities:

* Reusable helpers
* Validators
* Formatters
* Constants

---

# Recommended Project Structure

```text
src/
├── api/
│   └── v1/
│       ├── users.py
│       └── products.py
├── core/
│   ├── config.py
│   ├── logging.py
│   └── exceptions.py
├── models/
│   ├── user.py
│   └── product.py
├── services/
│   ├── user_service.py
│   └── product_service.py
├── utils/
│   └── validators.py
└── main.py
```

---

# Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Freeze dependencies:

```bash
pip freeze > requirements.txt
```

---

# Application Entry Point

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Running"}
```

Run:

```bash
uvicorn src.main:app --reload
```

---

# Dependency Injection

FastAPI includes a powerful dependency system.

Example:

```python
from fastapi import Depends

def get_current_user():
    return {"id": 1}

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user
```

Benefits:

* Reusability
* Testability
* Separation of concerns

---

# Request Validation

FastAPI uses Pydantic.

Example:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
```

Endpoint:

```python
@app.post("/users")
def create_user(payload: UserCreate):
    return payload
```

---

# Response Models

Example:

```python
class UserResponse(BaseModel):
    id: int
    name: str
```

```python
@app.get("/users/{id}", response_model=UserResponse)
def get_user():
    pass
```

Benefits:

* Type safety
* Documentation generation
* Consistent responses

---

# Database Integration

Most common approach:

```text
FastAPI
    ↓
SQLAlchemy
    ↓
PostgreSQL
```

Recommended stack:

```text
FastAPI
SQLAlchemy
Alembic
PostgreSQL
```

---

# Migrations

Recommended tool:

```text
Alembic
```

Create migration:

```bash
alembic revision --autogenerate -m "create users table"
```

Apply migration:

```bash
alembic upgrade head
```

---

# Authentication

Common approaches:

## JWT

Recommended for APIs.

Libraries:

```bash
pip install python-jose
pip install passlib[bcrypt]
```

---

## OAuth2

Built-in FastAPI support.

Useful for:

* Third-party authentication
* Enterprise systems

---

# Error Handling

Centralize exceptions.

Example:

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

---

# Middleware

Examples:

* Authentication
* Logging
* CORS
* Rate limiting

Example:

```python
app.add_middleware(...)
```

---

# Automatic Documentation

One of FastAPI's strongest features.

Swagger UI:

```text
/docs
```

ReDoc:

```text
/redoc
```

Generated automatically from:

* Routes
* Schemas
* Type hints

---

# Testing

Recommended framework:

```text
Pytest
```

Install:

```bash
pip install pytest
```

Example:

```python
def test_health():
    assert True
```

Run:

```bash
pytest
```

---

# Deployment

Recommended production server:

```text
Gunicorn + Uvicorn Workers
```

Example:

```bash
gunicorn src.main:app \
-k uvicorn.workers.UvicornWorker \
-w 4
```

---

# Docker Example

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","8000"]
```

---

# Advantages

* Excellent performance
* Strong typing
* Automatic documentation
* Easy validation
* Modern Python ecosystem
* Large community

---

# Limitations

* Smaller ecosystem than Express
* Async concepts may require learning
* Heavy use of typing for best results

---

# Recommended Learning Path

1. Python fundamentals
2. HTTP basics
3. FastAPI routes
4. Pydantic schemas
5. SQLAlchemy
6. Authentication
7. Testing
8. Docker
9. CI/CD
10. Production deployment

---

# Conclusion

FastAPI is one of the most productive and modern frameworks available for Python backend development.

It aligns naturally with the architecture proposed by `template-backend-api` and is recommended as the primary Python implementation example for this repository.
