# FastAPI Example 02 — CRUD Operations

## Purpose

Demonstrates a simple CRUD implementation using an in-memory data store.  

The goal is to understand:  

- Create  
- Read  
- Update  
- Delete  

operations before introducing databases.  

## Concepts Covered

- Request validation  
- Response models  
- Path parameters  
- HTTP status codes  

## Endpoints

POST /api/v1/students  

GET /api/v1/students  

GET /api/v1/students/{id}  

DELETE /api/v1/students/{id}

## Run

```bash
pip install fastapi uvicorn pydantic

uvicorn main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```
