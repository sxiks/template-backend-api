# Testing

## Purpose

The `tests/` directory contains the project's testing structure.

Its purpose is to verify that the application behaves correctly, remains maintainable over time, and continues working as new features are introduced.

Testing should be considered a core part of the development process rather than an optional activity.

This template follows the industry-standard **Testing Pyramid** approach.

---

## Testing Pyramid

The Testing Pyramid organizes tests according to their scope, speed, cost, and reliability.

```text
           E2E
            ▲
            │
     Integration
            ▲
            │
          Unit
```

The higher a test is in the pyramid:

* The slower it becomes
* The more components it involves
* The more expensive it is to maintain

The lower a test is in the pyramid:

* The faster it runs
* The easier it is to maintain
* The more frequently it should be written

---

## Directory Structure

```text
tests/
├── README.md
├── unit/
│   └── README.md
├── integration/
│   └── README.md
└── e2e/
    └── README.md
```

---

## Testing Levels

### Unit Tests

Purpose:

Verify a single component in complete isolation.

Characteristics:

* Fast
* Deterministic
* Independent
* No external systems

Examples:

* Service validation rules
* Utility functions
* Data transformations

---

### Integration Tests

Purpose:

Verify that multiple components work correctly together.

Characteristics:

* Moderate speed
* Multiple application layers involved
* Real component interaction

Examples:

* Service + Repository
* Service + Database
* API + Service

---

### End-to-End Tests

Purpose:

Verify complete user flows.

Characteristics:

* Slowest tests
* Highest confidence
* Simulate real application usage

Examples:

* User registration flow
* Authentication flow
* Product purchase flow

---

## Test Distribution

A healthy backend project typically follows:

```text
70% - Unit Tests
20% - Integration Tests
10% - E2E Tests
```

Exact percentages may vary depending on project requirements.

---

## Relationship With Application Layers

```text
Tests
 │
 ├── Unit
 │    └── Individual Components
 │
 ├── Integration
 │    └── Component Interactions
 │
 └── E2E
      └── Entire System
```

---

## Best Practices

* Prioritize unit tests
* Test business rules thoroughly
* Keep tests deterministic
* Isolate failures
* Avoid duplicated test coverage
* Test behavior rather than implementation

---

## Common Mistakes

* Relying only on E2E tests
* Writing no unit tests
* Testing framework internals
* Creating brittle tests
* Depending on external services during unit testing

---

## Summary

The `tests/` directory implements the Testing Pyramid approach.

Unit tests verify individual components, integration tests verify interactions, and E2E tests verify complete application workflows.
