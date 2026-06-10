# Express Example 03 — Authentication

## Purpose

Demonstrates middleware-based route protection.  

## Concepts Covered

- Middleware  
- Authorization headers  
- Protected routes  

## Endpoints

GET /api/v1/public  

GET /api/v1/protected  

## Valid Token

```text
my-secret-token
```

## Header:

```http
Authorization: Bearer my-secret-token
```

## Installation

```bash
npm install
```

## Run

```bash
npm start
```
