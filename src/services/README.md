# Services Layer

## Purpose

The Services layer contains the application's business logic.

This is where decisions are made and business rules are enforced.

If the API layer answers "How do we receive data?", the Services layer answers "What should happen with this data?"

---

## Responsibilities

The Services layer is responsible for:

* Business rules
* Workflows
* Use cases
* Domain validation
* Coordinating multiple models
* Integrating external systems
* Managing transactions

---

## Should Contain

Examples:

* UserService
* ProductService
* OrderService
* AuthService
* EmailService

Typical responsibilities:

* Register users
* Validate permissions
* Process orders
* Calculate totals
* Generate tokens
* Call third-party APIs

---

## Should NOT Contain

The Services layer should not contain:

* HTTP routes
* Controllers
* Response formatting
* Framework-specific request handling
* ORM configuration
* Application startup code

---

## Example Workflow

```text
Create User
    ↓
Validate Data
    ↓
Check Business Rules
    ↓
Hash Password
    ↓
Save User
    ↓
Send Welcome Email
```

All these steps belong in the Services layer.

---

## Relationship With Other Layers

```text
API
 ↓
Services
 ↓
Models
```

Services receive requests from the API layer and use models to access data.

---

## Best Practices

* One responsibility per service
* Keep services framework-agnostic
* Reuse services across multiple endpoints
* Make services easy to test
* Centralize business rules

---

## Common Mistakes

* Mixing HTTP logic with business logic
* Duplicating rules across controllers
* Accessing configuration directly from services
* Creating excessively large service classes

---

## Summary

The Services layer is the heart of the application.

All business decisions should happen here.
