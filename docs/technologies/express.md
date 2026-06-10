# Express.js

## Overview

Express.js is the most widely adopted backend framework in the Node.js ecosystem.

It provides a minimal and flexible foundation for building:

* REST APIs
* Web applications
* Microservices
* Backend systems

Official documentation:

https://expressjs.com/

---

# Why Use Express?

Express is popular because it is:

* Lightweight
* Flexible
* Mature
* Well documented
* Supported by a massive ecosystem

It gives developers complete control over application structure.

---

# Express and Template Architecture

The `template-backend-api` architecture maps naturally to Express.

```text
src/
├── api/
├── core/
├── models/
├── services/
└── utils/
```

---

## API Layer

Location:

```text
src/api/v1/
```

Responsibilities:

* Route definitions
* Controllers
* HTTP handling

Example:

```javascript
router.get("/users", controller.getUsers);
```

---

## Service Layer

Location:

```text
src/services/
```

Responsibilities:

* Business logic
* Application rules
* Data coordination

Example:

```javascript
class UserService {
  getAllUsers() {
    return [];
  }
}
```

---

## Model Layer

Location:

```text
src/models/
```

Responsibilities:

* Database entities
* ORM definitions
* Data access

Common tools:

```text
Prisma
Sequelize
TypeORM
Mongoose
```

---

## Core Layer

Location:

```text
src/core/
```

Responsibilities:

* Configuration
* Middleware
* Error handling
* Logging

---

## Utils Layer

Location:

```text
src/utils/
```

Responsibilities:

* Validators
* Formatters
* Constants
* Reusable helpers

---

# Recommended Project Structure

```text
src/
├── api/
│   └── v1/
│       ├── users.routes.js
│       └── products.routes.js
├── core/
│   ├── config.js
│   ├── logger.js
│   └── errors.js
├── models/
│   ├── user.model.js
│   └── product.model.js
├── services/
│   ├── user.service.js
│   └── product.service.js
├── utils/
│   └── validators.js
└── app.js
```

---

# Installation

Initialize project:

```bash
npm init -y
```

Install Express:

```bash
npm install express
```

Development dependencies:

```bash
npm install -D nodemon
```

---

# Application Entry Point

Example:

```javascript
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.json({
    message: "API Running"
  });
});

app.listen(3000);
```

---

# Routing

Example:

```javascript
const router = require("express").Router();

router.get("/", controller.getUsers);

module.exports = router;
```

---

# Controllers

Purpose:

Handle HTTP concerns only.

Example:

```javascript
exports.getUsers = async (req, res) => {
  const users = await userService.getUsers();

  res.json(users);
};
```

Avoid business logic inside controllers.

---

# Services

Purpose:

Implement business rules.

Example:

```javascript
class UserService {
  async getUsers() {
    return [];
  }
}
```

---

# Validation

Recommended libraries:

```text
Zod
Joi
Express Validator
```

Example:

```javascript
const schema = z.object({
  email: z.string().email()
});
```

---

# Database Integration

Popular stacks:

```text
Express
Prisma
PostgreSQL
```

or

```text
Express
Mongoose
MongoDB
```

---

# Prisma

Recommended ORM for modern projects.

Install:

```bash
npm install prisma
npm install @prisma/client
```

Initialize:

```bash
npx prisma init
```

Migration:

```bash
npx prisma migrate dev
```

---

# Authentication

Most common:

```text
JWT Authentication
```

Libraries:

```bash
npm install jsonwebtoken
npm install bcrypt
```

---

# Middleware

Examples:

* Authentication
* Logging
* Validation
* Rate limiting

Example:

```javascript
app.use(express.json());
```

---

# Error Handling

Centralize errors.

Example:

```javascript
app.use((err, req, res, next) => {
  res.status(500).json({
    error: err.message
  });
});
```

---

# Logging

Recommended:

```text
Pino
Winston
Morgan
```

Example:

```bash
npm install pino
```

---

# Testing

Recommended frameworks:

```text
Jest
Vitest
Supertest
```

Install:

```bash
npm install -D jest supertest
```

Example:

```javascript
test("health endpoint", () => {
  expect(true).toBe(true);
});
```

---

# Environment Variables

Install:

```bash
npm install dotenv
```

Example:

```javascript
require("dotenv").config();
```

---

# Security

Recommended packages:

```bash
npm install helmet
npm install cors
npm install express-rate-limit
```

Purpose:

* Secure headers
* CORS control
* Rate limiting

---

# Docker Example

```dockerfile
FROM node:22-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]
```

---

# Production Deployment

Recommended process:

```text
Nginx
    ↓
Express
    ↓
Database
```

Process manager:

```text
PM2
```

Install:

```bash
npm install -g pm2
```

Run:

```bash
pm2 start src/app.js
```

---

# Advantages

* Extremely flexible
* Huge ecosystem
* Massive community
* Easy learning curve
* Excellent documentation

---

# Limitations

* Requires more decisions
* Less opinionated architecture
* Validation not built-in
* Documentation not automatic

---

# Recommended Learning Path

1. JavaScript fundamentals
2. Node.js fundamentals
3. Express routing
4. Middleware
5. Validation
6. Database integration
7. Authentication
8. Testing
9. Docker
10. Production deployment

---

# FastAPI vs Express

| Area           | FastAPI   | Express            |
| -------------- | --------- | ------------------ |
| Language       | Python    | JavaScript         |
| Performance    | Excellent | Excellent          |
| Validation     | Built-in  | External libraries |
| Documentation  | Automatic | Manual             |
| Ecosystem      | Large     | Massive            |
| Learning Curve | Moderate  | Easy               |

---

# Conclusion

Express remains one of the most important backend frameworks in the industry.

It integrates perfectly with the layered architecture defined in `template-backend-api` and serves as the recommended Node.js implementation example for this repository.
