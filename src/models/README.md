# Models Layer

## Purpose

The Models layer represents the application's data structures and persistence mechanisms.

It defines how data is stored, retrieved, and organized.

---

## Responsibilities

The Models layer is responsible for:

* Entities
* Domain objects
* ORM models
* Database access
* Repositories
* Data mapping

---

## Should Contain

Examples:

* User model
* Product model
* Order model
* Repository classes
* Database entities

Typical technologies:

* SQLAlchemy
* Prisma
* Sequelize
* Hibernate
* Entity Framework

---

## Examples

### SQLAlchemy

```text
User
Product
Order
```

### Prisma

```text
User
Product
Order
```

### Sequelize

```text
User
Product
Order
```

---

## Should NOT Contain

The Models layer should not contain:

* HTTP logic
* Controllers
* Business workflows
* Authentication rules
* Response formatting

---

## Relationship With Other Layers

```text
API
 ↓
Services
 ↓
Models
 ↓
Database
```

Models communicate directly with the database.

Services communicate with models.

---

## Best Practices

* Keep models focused on data
* Separate persistence from business logic
* Use repositories when appropriate
* Define clear relationships
* Avoid framework lock-in when possible

---

## Common Mistakes

* Placing business logic inside models
* Mixing database code with HTTP code
* Creating excessively complex entities
* Allowing direct database access from controllers

---

## Summary

The Models layer defines how information is structured and persisted.
