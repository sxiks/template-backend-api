# FastAPI Example 01 — Basic Endpoint

## Purpose

Demonstrates the smallest possible FastAPI application following the architectural concepts described in this repository.  

## Concepts Covered

- Route definition  
- API versioning  
- JSON response  
- Health check endpoint  

## Endpoint

GET /api/v1/health  

## Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

## Server:

```
http://127.0.0.1:8000
```

## Test:

```bash
curl http://127.0.0.1:8000/api/v1/health
```

## Expected Response

```json
{  "status": "success",  "message": "API is operational"}
```
