# Utils Layer

## Purpose

The Utils layer contains reusable helper functions and shared utilities.

These components should be generic and independent of business rules.

---

## Responsibilities

The Utils layer is responsible for:

- Helpers
- Validators
- Constants
- Formatters
- Utility functions
- Shared enumerations

---

## Should Contain

Examples:

- Date formatting
- String manipulation
- Number formatting
- Generic validators
- Utility calculations
- Shared constants

---

## Examples

```text
DateFormatter
StringHelper
PaginationHelper
EmailValidator
CurrencyFormatter
```

## Should NOT Contain

The Utils layer should not contain:

- Business rules
- Database access
- HTTP logic
- Authentication workflows
- Domain-specific decisions

---

## Relationship With Other Layers


```text
          Utils
            │
 ┌──────────┼──────────┐
 │          │          │
API      Services    Models
```
Utilities can be used by all layers.

---

## Best Practices

- Keep utilities stateless
- Keep functions pure whenever possible
- Avoid dependencies on framework-specific code
- Reuse utilities instead of duplicating logic

---

## Common Mistakes

- Putting business rules in helper functions
- Creating overly generic utility classes
- Using utilities as a dumping ground for random code
- Mixing domain logic with formatting logic

---

## Summary

The Utils layer contains reusable, framework-independent helper functionality shared across the application.