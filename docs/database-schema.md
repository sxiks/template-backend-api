# Database Schema

## Overview

This document defines the standards and conventions used to document database structures in projects derived from the `template-backend-api` architecture.

The objective is to provide a consistent way to document:

* Entities
* Tables
* Relationships
* Constraints
* Indexes
* Naming conventions
* Data lifecycle considerations

This document serves as both a reference and a reusable template.

---

# Database Philosophy

The database layer is responsible for storing and retrieving information required by the application.

Good database design should prioritize:

* Consistency
* Integrity
* Scalability
* Maintainability
* Performance

The database should reflect business concepts while avoiding unnecessary complexity.

---

# Database Design Principles

## Single Source of Truth

A piece of information should only exist in one authoritative location.

Good:

```text
users.email
```

Bad:

```text
users.email
orders.customer_email
payments.customer_email
```

Duplicating business-critical information increases maintenance costs and inconsistency risks.

---

## Normalization

Data should be normalized when appropriate.

Benefits:

* Reduced duplication
* Easier updates
* Better consistency

Example:

```text
Users
  ↓
Orders
```

Instead of:

```text
Orders
├── customer_name
├── customer_email
├── customer_phone
```

stored repeatedly.

---

## Referential Integrity

Relationships should be enforced through foreign keys whenever possible.

Example:

```text
orders.user_id
        ↓
users.id
```

This prevents orphan records and invalid references.

---

## Predictable Naming

Consistency is more important than preference.

Recommended:

```text
users
products
orders
order_items
```

Avoid:

```text
tblUsers
PRODUCTS_TABLE
OrderData
```

---

# Naming Conventions

## Tables

Use plural nouns.

Examples:

```text
users
products
orders
payments
roles
permissions
```

---

## Columns

Use snake_case.

Examples:

```text
first_name
last_name
created_at
updated_at
deleted_at
```

Avoid:

```text
FirstName
firstName
FIRST_NAME
```

---

## Primary Keys

Recommended:

```text
id
```

Example:

```text
users.id
products.id
orders.id
```

---

## Foreign Keys

Recommended:

```text
user_id
product_id
order_id
```

Examples:

```text
orders.user_id
payments.order_id
reviews.product_id
```

---

# Audit Fields

Every major entity should include audit fields.

Recommended:

| Field      | Purpose                     |
| ---------- | --------------------------- |
| created_at | Creation timestamp          |
| updated_at | Last modification timestamp |
| deleted_at | Soft delete timestamp       |

Example:

```text
users
├── id
├── email
├── created_at
├── updated_at
└── deleted_at
```

---

# Example Domain Model

This section demonstrates a common e-commerce style schema.

---

# Users

Purpose:

Store registered user accounts.

## Table

```text
users
```

## Columns

| Column        | Type           | Description        |
| ------------- | -------------- | ------------------ |
| id            | UUID / Integer | Primary key        |
| name          | String         | Full name          |
| email         | String         | Unique email       |
| password_hash | String         | Encrypted password |
| created_at    | Timestamp      | Creation date      |
| updated_at    | Timestamp      | Last update        |
| deleted_at    | Timestamp      | Soft delete        |

---

## Constraints

```text
PRIMARY KEY (id)
UNIQUE (email)
```

---

# Products

Purpose:

Store product information.

## Table

```text
products
```

## Columns

| Column      | Type           | Description         |
| ----------- | -------------- | ------------------- |
| id          | UUID / Integer | Primary key         |
| name        | String         | Product name        |
| description | Text           | Product description |
| price       | Decimal        | Product price       |
| stock       | Integer        | Available inventory |
| created_at  | Timestamp      | Creation date       |
| updated_at  | Timestamp      | Last update         |

---

# Orders

Purpose:

Store customer purchases.

## Table

```text
orders
```

## Columns

| Column       | Type           | Description         |
| ------------ | -------------- | ------------------- |
| id           | UUID / Integer | Primary key         |
| user_id      | FK             | Customer            |
| status       | String         | Current order state |
| total_amount | Decimal        | Order total         |
| created_at   | Timestamp      | Creation date       |
| updated_at   | Timestamp      | Last update         |

---

# Order Items

Purpose:

Store products included in an order.

## Table

```text
order_items
```

## Columns

| Column     | Type           | Description        |
| ---------- | -------------- | ------------------ |
| id         | UUID / Integer | Primary key        |
| order_id   | FK             | Parent order       |
| product_id | FK             | Product            |
| quantity   | Integer        | Purchased quantity |
| unit_price | Decimal        | Price at purchase  |

---

# Relationships

## One-to-Many

A single user can own multiple orders.

```text
users
  │
  └──── orders
```

Relationship:

```text
users.id
       ↓
orders.user_id
```

---

## One-to-One

Example:

```text
users
  │
  └──── profiles
```

Relationship:

```text
users.id
       ↓
profiles.user_id
```

---

## Many-to-Many

Example:

```text
users
   │
user_roles
   │
roles
```

Bridge table:

```text
user_roles
├── user_id
└── role_id
```

---

# Entity Relationship Diagram

Example:

```text
Users
 │
 │ 1:N
 ▼
Orders
 │
 │ 1:N
 ▼
OrderItems
 │
 │ N:1
 ▼
Products
```

---

# Indexing Strategy

Indexes improve query performance.

Recommended indexes:

## Primary Keys

Automatically indexed.

Example:

```text
users.id
orders.id
products.id
```

---

## Unique Fields

Example:

```text
users.email
```

Constraint:

```text
UNIQUE(email)
```

---

## Search Fields

Frequently queried columns should be indexed.

Examples:

```text
products.name
orders.status
users.email
```

---

## Foreign Keys

Examples:

```text
orders.user_id
order_items.order_id
order_items.product_id
```

These columns are frequently used in joins.

---

# Soft Delete Strategy

Recommended for most business applications.

Instead of:

```sql
DELETE FROM users
WHERE id = 1;
```

Use:

```sql
UPDATE users
SET deleted_at = NOW()
WHERE id = 1;
```

Benefits:

* Data recovery
* Auditing
* Historical reporting

---

# Data Lifecycle

Every entity should define:

## Creation

How records are created.

Example:

```text
POST /users
```

---

## Updates

How records change.

Example:

```text
PUT /users/{id}
```

---

## Archival

How inactive records are handled.

Example:

```text
deleted_at
```

---

## Removal

Whether hard deletion is allowed.

Example:

```text
Admin-only operation
```

---

# Migration Strategy

Database changes should be versioned.

Recommended tools:

## Python

```text
Alembic
```

---

## Node.js

```text
Sequelize Migrations
Knex Migrations
TypeORM Migrations
Prisma Migrations
```

---

## Java

```text
Flyway
Liquibase
```

---

# Security Considerations

Sensitive information should never be stored in plain text.

Never store:

```text
Passwords
API Keys
Tokens
Secrets
```

Bad:

```text
password
```

Good:

```text
password_hash
```

---

# Performance Considerations

As databases grow:

* Add indexes carefully
* Avoid unnecessary joins
* Use pagination
* Monitor query execution plans
* Archive inactive records

Common anti-patterns:

```text
SELECT *
```

on large tables.

Returning thousands of records without pagination.

Missing indexes on foreign keys.

---

# Documentation Checklist

For every table verify:

* [ ] Purpose documented
* [ ] Columns documented
* [ ] Primary key documented
* [ ] Foreign keys documented
* [ ] Constraints documented
* [ ] Relationships documented
* [ ] Indexes documented
* [ ] Audit fields included
* [ ] Security considerations reviewed

---

# Future Extensions

As systems grow, consider documenting:

* Data warehouses
* Event sourcing models
* Read replicas
* Multi-tenant schemas
* Sharding strategies
* Caching layers

---

# Conclusion

A well-documented schema helps developers understand:

* How data is structured
* How entities relate to each other
* How information flows through the system
* How the database evolves over time

Database documentation should evolve alongside the application and remain synchronized with every schema change.
