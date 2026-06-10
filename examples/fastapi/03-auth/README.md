# FastAPI Example 03 — Authentication

## Purpose

Demonstrates route protection using bearer authentication.  

This example introduces:  

- Protected endpoints  
- Dependency Injection  
- Authentication middleware concepts  
- Authorization headers  

## Concepts Covered

- HTTPBearer  
- Dependency Injection  
- Protected Routes  

## Endpoints

GET /api/v1/public  

GET /api/v1/protected  

## Test

Valid Token:

```textile
my-secret-token
```

Header:

```http
Authorization: Bearer my-secret-token
```

## Run

```bash
pip install fastapi uvicornuvicorn main:app --reload
```


