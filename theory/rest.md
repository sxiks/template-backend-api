# API Reference

## Overview

This document defines the standard structure for documenting REST API endpoints within projects derived from the `template-backend-api` architecture.

The objective is to provide a consistent and predictable format for documenting:

* Endpoints
* Request parameters
* Request bodies
* Responses
* Error handling
* Authentication requirements

This document serves as both a reference and a template.

---

# Documentation Standards

Every endpoint should document:

* HTTP method
* Endpoint path
* Description
* Authentication requirements
* Request parameters
* Request body
* Success responses
* Error responses
* Example requests
* Example responses

---

# API Conventions

## Base URL

Development:

```text
http://localhost:8000/api/v1
```

Staging:

```text
https://staging.example.com/api/v1
```

Production:

```text
https://api.example.com/api/v1
```

---

## API Versioning

All endpoints should be versioned.

Example:

```text
/api/v1/users
/api/v1/products
/api/v1/orders
```

Future versions:

```text
/api/v2/users
/api/v2/products
```

Versioning prevents breaking changes for existing clients.

---

## Resource Naming

Use plural nouns.

Good:

```text
/users
/products
/orders
```

Avoid:

```text
/user
/product
/order
```

---

## HTTP Methods

| Method | Purpose                    |
| ------ | -------------------------- |
| GET    | Retrieve data              |
| POST   | Create resources           |
| PUT    | Replace resources          |
| PATCH  | Partially update resources |
| DELETE | Remove resources           |

---

# Authentication

## Public Endpoint

No token required.

Example:

```http
GET /health
```

---

## Protected Endpoint

Requires authentication.

Example:

```http
Authorization: Bearer <token>
```

Request:

```http
GET /users/profile
Authorization: Bearer eyJhbGciOi...
```

---

# Standard Response Format

## Success Response

```json
{
  "success": true,
  "data": {}
}
```

---

## Error Response

```json
{
  "success": false,
  "error": "ValidationError",
  "message": "Email already exists"
}
```

---

# HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 409  | Conflict              |
| 422  | Validation Error      |
| 500  | Internal Server Error |

---

# Resource Documentation Template

Each resource should follow the structure below.

---

# Users Resource

Base Path:

```text
/api/v1/users
```

---

## Create User

### Endpoint

```http
POST /api/v1/users
```

### Description

Creates a new user.

### Authentication

Not required.

### Request Body

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "StrongPassword123"
}
```

### Validation Rules

| Field    | Rules                    |
| -------- | ------------------------ |
| name     | Required                 |
| email    | Required, unique         |
| password | Required, minimum length |

### Success Response

Status:

```http
201 Created
```

Body:

```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Error Responses

Email already exists:

```http
409 Conflict
```

```json
{
  "success": false,
  "error": "UserAlreadyExists",
  "message": "Email already registered"
}
```

Validation error:

```http
422 Unprocessable Entity
```

```json
{
  "success": false,
  "error": "ValidationError",
  "message": "Invalid request data"
}
```

---

## Get User

### Endpoint

```http
GET /api/v1/users/{id}
```

### Description

Retrieves a single user.

### Authentication

Required.

### Path Parameters

| Parameter | Type    | Description     |
| --------- | ------- | --------------- |
| id        | Integer | User identifier |

### Success Response

```http
200 OK
```

```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Error Response

```http
404 Not Found
```

```json
{
  "success": false,
  "error": "UserNotFound",
  "message": "User does not exist"
}
```

---

## List Users

### Endpoint

```http
GET /api/v1/users
```

### Description

Returns a paginated list of users.

### Authentication

Required.

### Query Parameters

| Parameter | Type    | Required | Description    |
| --------- | ------- | -------- | -------------- |
| page      | Integer | No       | Current page   |
| limit     | Integer | No       | Items per page |
| search    | String  | No       | Search filter  |

### Example Request

```http
GET /api/v1/users?page=1&limit=10
```

### Success Response

```http
200 OK
```

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "John Doe"
    },
    {
      "id": 2,
      "name": "Jane Doe"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 2
  }
}
```

---

## Update User

### Endpoint

```http
PUT /api/v1/users/{id}
```

### Description

Updates an existing user.

### Authentication

Required.

### Path Parameters

| Parameter | Type    |
| --------- | ------- |
| id        | Integer |

### Request Body

```json
{
  "name": "Updated Name"
}
```

### Success Response

```http
200 OK
```

```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "Updated Name"
  }
}
```

---

## Delete User

### Endpoint

```http
DELETE /api/v1/users/{id}
```

### Description

Deletes a user.

### Authentication

Required.

### Success Response

```http
204 No Content
```

Response body:

```text
(empty)
```

---

# Pagination Standard

List endpoints should implement pagination.

Request:

```http
GET /resources?page=1&limit=20
```

Response:

```json
{
  "success": true,
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 125,
    "totalPages": 7
  }
}
```

---

# Filtering Standard

Example:

```http
GET /products?category=electronics
```

Multiple filters:

```http
GET /products?category=electronics&status=active
```

---

# Sorting Standard

Ascending:

```http
GET /products?sort=name
```

Descending:

```http
GET /products?sort=-createdAt
```

---

# Search Standard

Example:

```http
GET /users?search=john
```

---

# Authentication Endpoints Example

## Login

### Endpoint

```http
POST /api/v1/auth/login
```

### Request Body

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

### Success Response

```json
{
  "success": true,
  "data": {
    "accessToken": "jwt-token",
    "expiresIn": 3600
  }
}
```

---

## Refresh Token

### Endpoint

```http
POST /api/v1/auth/refresh
```

### Success Response

```json
{
  "success": true,
  "data": {
    "accessToken": "new-token"
  }
}
```

---

## Logout

### Endpoint

```http
POST /api/v1/auth/logout
```

### Success Response

```http
204 No Content
```

---

# Error Catalog

## ValidationError

```json
{
  "success": false,
  "error": "ValidationError",
  "message": "Invalid input"
}
```

---

## Unauthorized

```json
{
  "success": false,
  "error": "Unauthorized",
  "message": "Authentication required"
}
```

---

## Forbidden

```json
{
  "success": false,
  "error": "Forbidden",
  "message": "Insufficient permissions"
}
```

---

## NotFound

```json
{
  "success": false,
  "error": "NotFound",
  "message": "Resource not found"
}
```

---

## Conflict

```json
{
  "success": false,
  "error": "Conflict",
  "message": "Resource already exists"
}
```

---

## InternalServerError

```json
{
  "success": false,
  "error": "InternalServerError",
  "message": "Unexpected server error"
}
```

---

# Documentation Checklist

Before considering an endpoint documented, verify:

* [ ] Endpoint path documented
* [ ] HTTP method documented
* [ ] Authentication documented
* [ ] Parameters documented
* [ ] Request body documented
* [ ] Success response documented
* [ ] Error responses documented
* [ ] Example request included
* [ ] Example response included
* [ ] Status codes documented

---

# Conclusion

Consistent API documentation improves:

* Developer experience
* Team collaboration
* API adoption
* Maintenance
* Long-term scalability

Every new endpoint added to a project should follow the standards defined in this document.
