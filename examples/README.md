# Examples

This directory contains practical implementations of the architectural concepts described in the root repository.

The purpose of these examples is not to provide production-ready applications, but to demonstrate how the layered backend architecture can be implemented using different technologies and frameworks.

---

## Purpose

The examples help bridge the gap between architectural theory and implementation.

Each technology-specific example shows how the following concepts are applied in practice:

* API versioning
* Layered architecture
* Separation of concerns
* Business logic isolation
* Configuration management
* Testing structure
* Authentication patterns
* Scalability considerations

---

## Available Implementations

### FastAPI

Location:

```text
examples/fastapi/
```

Demonstrates how the template architecture can be implemented using:

* Python
* FastAPI
* Pydantic
* Dependency Injection
* ASGI applications

Recommended for learning:

* Modern Python backend development
* REST API design
* Dependency injection concepts
* OpenAPI documentation generation

---

### Express

Location:

```text
examples/express/
```

Demonstrates how the template architecture can be implemented using:

* Node.js
* Express.js
* Middleware patterns
* Service-based application structure

Recommended for learning:

* JavaScript backend development
* HTTP middleware concepts
* API routing patterns
* Service-oriented architecture

---

## Learning Path

Suggested order:

1. Read the repository root README.
2. Study the architecture documentation.
3. Review the FastAPI implementation.
4. Review the Express implementation.
5. Compare how both frameworks implement the same concepts.
6. Create your own backend project using the template.

---

## Important Notes

The examples are educational references.

They are intentionally simplified to highlight architectural concepts rather than framework-specific optimizations.

When creating a real project, adapt the examples according to your requirements, team conventions, and deployment environment.
