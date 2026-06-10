# Core Layer

## Purpose

The Core layer contains application-wide infrastructure and foundational components.

These components support the entire application but do not belong to a specific business domain.

---

## Responsibilities

The Core layer is responsible for:

- Configuration management
- Application startup
- Dependency injection
- Error handling
- Middleware registration
- Lifecycle management
- Security infrastructure
- Logging initialization

---

## Should Contain

Examples:

- Application bootstrap
- Dependency container
- Global exception handlers
- Middleware configuration
- Security configuration
- Logging configuration
- Application settings

---

## Should NOT Contain

The Core layer should not contain:

- Business rules
- Domain workflows
- Resource-specific controllers
- Database entities
- Feature-specific logic

---

## Example Components

```text
Application Startup
Configuration Loader
Dependency Container
Global Error Handler
Authentication Middleware
Logging Setup
```
---

## Relationship With Other Layers

```text
          Core
            │
 ┌──────────┼──────────┐
 │          │          │
API      Services    Models
```
The Core layer supports all other layers.

---

## Best Practices

- Centralize configuration
- Keep infrastructure concerns isolated
- Register dependencies in one place
- Use global error handling
- Standardize middleware configuration

---

## Common Mistakes

- Placing business logic in middleware
- Duplicating configuration across modules
- Creating feature-specific code in Core
- Mixing infrastructure and domain concerns

---

## Summary

The Core layer provides the application's infrastructure and foundational services.