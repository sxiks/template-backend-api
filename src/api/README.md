# API Layer

## Purpose

The API layer is the entry point of the application.

Its responsibility is to handle HTTP communication between clients and the backend system. This layer receives requests, validates input, invokes the appropriate service, and returns responses.

This is the only layer that should be aware of HTTP concepts such as routes, methods, headers, query parameters, request bodies, status codes, and response formatting.

---

## Responsibilities

The API layer is responsible for:

* Defining routes and endpoints
* Handling HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`)
* Parsing request data
* Validating request structure and format
* Calling the appropriate service
* Returning standardized responses
* Managing HTTP status codes
* Translating domain errors into HTTP responses

---

## Should Contain

Examples of components that belong in this layer:

* Routes
* Controllers
* Request DTOs
* Response DTOs
* Input validation schemas
* API versioning structure

Examples:

* UserController
* ProductController
* AuthController
* UserRoutes
* ValidationMiddleware

---

## Should NOT Contain

The API layer must not contain:

* Business logic
* Database queries
* ORM operations
* Complex calculations
* Workflow orchestration
* External service integrations

Incorrect example:

```text
POST /users
↓
Validate request
↓
Hash password
↓
Create JWT
↓
Send email
```

The API layer should not perform those actions directly.

Instead:

```text
POST /users
↓
UserService
↓
Response
```

---

## Example Request Flow

```text
Client Request
       ↓
API Route
       ↓
Controller
       ↓
Service Layer
       ↓
Response
```

---

## Relationship With Other Layers

```text
API
 ↓
Services
 ↓
Models
```

The API layer communicates with services.

It should never access models directly.

---

## Best Practices

* Keep controllers thin
* Validate inputs early
* Return consistent response structures
* Use proper HTTP status codes
* Version APIs from the beginning
* Separate routes by resource

---

## Common Mistakes

* Adding business rules inside controllers
* Querying the database directly from routes
* Returning inconsistent response formats
* Creating large controller files
* Skipping API versioning

---

## Summary

The API layer handles communication.

It translates HTTP requests into service calls and service results into HTTP responses.
