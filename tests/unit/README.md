# Unit Tests

## Purpose

Unit tests verify a single component in complete isolation.

The objective is to ensure that an individual function, class, or module behaves correctly without depending on databases, external services, networks, or other application layers.

Unit tests should be the most numerous tests in a project.

---

## Responsibilities

Unit tests are responsible for verifying:

* Business rules
* Validation logic
* Calculations
* Utility functions
* Service methods
* Data transformations

---

## Characteristics

Unit tests should be:

* Fast
* Isolated
* Deterministic
* Repeatable
* Easy to maintain

A unit test should always produce the same result when executed with the same inputs.

---

## What Should Be Tested

Examples:

```text
Password validation
Email validation
Price calculations
Discount calculations
Authorization rules
String formatting
Date formatting
```

---

## What Should NOT Be Used

Unit tests should not depend on:

```text
Databases
HTTP Requests
Message Queues
File Systems
External APIs
Network Connections
```

No real infrastructure should be required.

---

## Example Scope

```text
Input
  ↓
Function
  ↓
Output
```

A single function or method is usually the target.

---

## Relationship With Other Tests

```text
Unit
 ↓
Smallest scope
 ↓
Fastest execution
 ↓
Highest quantity
```

---

## Best Practices

* Test one behavior at a time
* Keep tests independent
* Use clear naming conventions
* Mock external dependencies
* Focus on business rules

---

## Common Mistakes

* Accessing databases
* Making network calls
* Testing multiple responsibilities
* Creating large setup procedures
* Depending on test execution order

---

## Summary

Unit tests verify one component in isolation.

They provide the fastest feedback and should form the foundation of the testing strategy.
