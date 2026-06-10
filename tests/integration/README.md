# Integration Tests

## Purpose

Integration tests verify that multiple components work correctly together.

While unit tests focus on individual pieces, integration tests validate the interactions between layers and systems.

Their goal is to detect problems that cannot be discovered through isolated testing.

---

## Responsibilities

Integration tests verify:

* Component interaction
* Layer communication
* Database integration
* Repository behavior
* Service collaboration
* Infrastructure integration

---

## Characteristics

Integration tests are:

* Slower than unit tests
* Faster than E2E tests
* More realistic than isolated tests
* Focused on component collaboration

---

## Typical Scenarios

Examples:

```text
API Layer
    ↓
Service Layer
```

```text
Service Layer
    ↓
Database Layer
```

```text
Repository
    ↓
Database
```

---

## What Should Be Tested

Examples:

* Service + Repository
* Repository + Database
* API + Service
* Authentication + Persistence
* Validation + Storage

---

## Example Flow

```text
Service
   ↓
Repository
   ↓
Database
```

The objective is to verify that all participating components work correctly together.

---

## Relationship With Other Tests

```text
Unit Tests
      ↓
Integration Tests
      ↓
E2E Tests
```

Integration tests occupy the middle layer of the Testing Pyramid.

---

## Best Practices

* Focus on critical integrations
* Use realistic test environments
* Test real component interactions
* Isolate external dependencies when possible
* Keep scenarios focused

---

## Common Mistakes

* Duplicating E2E tests
* Testing too many components at once
* Ignoring database behavior
* Creating fragile test environments
* Using integration tests for unit-level concerns

---

## Summary

Integration tests validate communication between multiple application components and ensure that system layers work correctly together.
