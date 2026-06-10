# End-to-End Tests

## Purpose

End-to-End (E2E) tests verify complete application workflows from the user's perspective.

These tests execute the application as a whole and validate that all layers work together correctly.

They provide the highest level of confidence because they simulate real usage scenarios.

---

## Responsibilities

E2E tests verify:

* Complete user journeys
* API behavior
* Authentication flows
* Database interactions
* Infrastructure integration
* System-wide functionality

---

## Characteristics

E2E tests are:

* The slowest tests
* The most realistic tests
* The most expensive to maintain
* The highest-confidence tests

---

## Typical Flow

```text
Request
   ↓
API
   ↓
Services
   ↓
Models
   ↓
Database
   ↓
Response
```

Every major layer participates in the execution.

---

## What Should Be Tested

Examples:

```text
User Registration
User Login
Password Reset
Order Creation
Product Purchase
Payment Processing
```

These workflows represent complete business scenarios.

---

## Example Scenario

```text
User submits login request
        ↓
Authentication service validates credentials
        ↓
Database retrieves user
        ↓
Token generated
        ↓
Response returned
```

The test validates the entire flow.

---

## Relationship With Other Tests

```text
Unit Tests
      ↓
Integration Tests
      ↓
End-to-End Tests
```

E2E tests sit at the top of the Testing Pyramid.

---

## Best Practices

* Focus on critical user journeys
* Keep the number of E2E tests limited
* Test realistic scenarios
* Automate execution when possible
* Validate system behavior rather than implementation details

---

## Common Mistakes

* Using E2E tests for every feature
* Duplicating unit-test coverage
* Testing minor implementation details
* Creating excessively long workflows
* Ignoring execution time

---

## Summary

End-to-End tests validate complete application behavior by exercising all major layers and infrastructure components together under realistic conditions.
