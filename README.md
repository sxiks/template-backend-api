# template-backend-api

> A production-oriented starting structure for backend REST APIs.
> Language-agnostic, layered architecture, versioned from day one.

---

## Purpose

Backend APIs are where most real software lives. This template establishes the professional conventions — versioning, layering, testing pyramid, environment configuration — that you'll encounter in every professional codebase. Using this template from the start prevents the common mistakes of monolithic files, hardcoded configuration, and untested services.

**Use this template when you are:**

- Building a REST API in any language (Python/FastAPI, Python/Flask, Node.js/Express, Java/Spring, etc.)
- Starting a backend project that will expose HTTP endpoints
- Building a service layer that other applications (frontend, mobile) will consume
- Creating a portfolio API project that demonstrates professional architecture

**Do NOT use this template when you are:**

- Building a static website → use `template-static-web`
- Building a database-only project → use `template-database`
- Building a frontend application → use `template-frontend-app`
- Building a simple academic script → use `template-academic`

---

## Use Cases

| Scenario | Fit |
|---|---|
| REST API with CRUD operations (users, products, etc.) | ✅ Ideal |
| Backend service with authentication and authorization | ✅ Ideal |
| Portfolio API demonstrating layered architecture | ✅ Ideal |
| Microservice with a single responsibility | ✅ Good |
| GraphQL API | ⚠️ Adapt `src/api/` structure to resolvers |
| WebSocket-only service | ⚠️ Adapt as needed |
| Static website backend | ❌ Use `template-static-web` |

---

## Architecture Overview

This template is built around a **layered architecture** — the standard pattern in professional backend development. Each layer has one job and one job only.

```
HTTP Request
     ↓
┌─────────────┐
│   api/v1/   │  ← Routes and controllers: only handles HTTP in/out
└──────┬──────┘
       ↓
┌─────────────┐
│  services/  │  ← Business logic: all decisions happen here
└──────┬──────┘
       ↓
┌─────────────┐
│   models/   │  ← Data structures and database interactions
└─────────────┘
```

**`core/`** and **`utils/`** are shared by all layers — configuration, logging, helpers, constants.

---

## Project Structure

```
template-backend-api/
├── .github/                        # GitHub automation
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.md           # Standardized bug report form
│   │   └── feature-request.md      # Standardized feature request form
│   └── workflows/
│       ├── ci.yml                  # Run tests on every push and PR
│       └── cd.yml                  # Deploy on merge to main
├── config/                         # All configuration — nothing hardcoded elsewhere
│   ├── database.yml                # Database connection settings per environment
│   ├── environments.yml            # Environment-specific variables reference
│   └── logging.yml                 # Log levels and output format
├── docs/                           # API and architecture documentation
│   ├── api-reference.md            # All endpoints: method, path, params, response
│   ├── architecture.md             # System design, layer diagram, key decisions
│   ├── database-schema.md          # Tables, columns, relationships
│   └── deployment.md               # How to deploy this API in each environment
├── examples/                       # Working demonstrations of this template in use
│   ├── example-01-basic-endpoint/  # One GET endpoint: route → controller → response
│   ├── example-02-crud-operations/ # Full CRUD: routes, models, services, unit tests
│   └── example-03-auth-integration/# JWT auth: middleware, protected routes, tests
├── src/
│   ├── api/
│   │   └── v1/                     # All v1 routes and controllers
│   ├── core/                       # Application-level logic: startup, error handling
│   ├── models/                     # Data structures, ORM models, DB access
│   ├── services/                   # Business logic — the heart of the application
│   └── utils/                      # Reusable helpers: formatters, validators, constants
├── tests/
│   ├── e2e/                        # End-to-end: full request-response cycles
│   ├── integration/                # Integration: multiple components working together
│   └── unit/                       # Unit: one function in complete isolation
├── .env.example                    # Documents every required environment variable
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Folder Responsibilities

### `src/api/v1/` — HTTP boundary

This is the **only** layer that knows about HTTP. It handles:
- Defining routes and their HTTP methods
- Parsing request data (query params, body, headers)
- Calling the appropriate service function
- Returning the HTTP response with correct status codes

It does **not** contain business logic. If you find yourself writing `if/else` conditions that aren't about HTTP format, move them to `services/`.

**Why v1?** Versioning from the start costs nothing. Adding v2 later without versioning costs weeks of refactoring.

### `src/services/` — Business logic

This is where all decisions happen. Services:
- Validate business rules (not just format, but logic)
- Coordinate between models
- Call external APIs or integrations
- Return domain objects or raise domain errors

Services are **testable without HTTP**. If you can test a service with a plain function call, you've correctly separated it from the API layer.

### `src/models/` — Data layer

Defines what your data looks like and how it's stored:
- Data classes or structs (language-dependent)
- ORM models (SQLAlchemy, Sequelize, Hibernate)
- Database access methods (queries, inserts, updates)

### `src/core/` — Application infrastructure

Things that every layer needs but don't belong to any one layer:
- Application startup and shutdown lifecycle
- Global error handlers and exception types
- Middleware (authentication, logging, rate limiting)
- Dependency injection configuration

### `src/utils/` — Shared helpers

Pure functions that have no side effects:
- Date and string formatters
- Input validators (format-only, not business rules)
- Mathematical calculations
- Constants and enums used across the codebase

### `config/` — Configuration, never code

All configuration is file-driven, not hardcoded. If a value could change between development, staging, and production, it belongs in `config/` and is loaded from environment variables.

### `tests/` — The testing pyramid

| Layer | What it tests | Speed | Count |
|---|---|---|---|
| `tests/unit/` | One function in isolation | Milliseconds | Many (most tests) |
| `tests/integration/` | Two or more components together | Seconds | Some |
| `tests/e2e/` | Full request-response cycle | Seconds | Few (critical paths only) |

---

## Getting Started

### Prerequisites

- Git installed and configured
- Your language runtime installed (Python 3.x, Node.js LTS, Java JDK 17+, etc.)
- A database server if needed (PostgreSQL, MySQL, SQLite for development)

### Initialize from template

```bash
# Clone the template
git clone https://github.com/sxiks/template-backend-api.git my-api
cd my-api

# Disconnect from template remote
git remote remove origin

# Set your own remote
git remote add origin https://github.com/sxiks/my-api.git

# First commit
git add .
git commit -m "init: initialize API from template-backend-api"
git push -u origin main
```

### Environment configuration

```bash
# Copy the example file — NEVER commit the real .env
cp .env.example .env

# Edit .env with your local values
nano .env
```

The `.env.example` file documents every variable the application needs:

```
# Application
APP_ENV=development
APP_PORT=8000
APP_SECRET_KEY=your-secret-key-here

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydb_dev
DB_USER=postgres
DB_PASSWORD=your-password
```

### Run the application (language-dependent)

```bash
# Python / FastAPI example
pip install -r requirements.txt
uvicorn src.main:app --reload

# Node.js / Express example
npm install
npm run dev

# Java / Spring Boot example
mvn spring-boot:run
```

### Run the test suite

```bash
# Python
pytest tests/

# Node.js
npm test

# Java
mvn test
```

---

## API Reference

Document every endpoint here as you build it.

### Base URL

```
Development:  http://localhost:8000/api/v1
Staging:      https://staging.yourapp.com/api/v1
Production:   https://api.yourapp.com/api/v1
```

### Endpoint template

```
GET /api/v1/resource
Authorization: Bearer <token>

Response 200:
{
  "data": [...],
  "total": 10,
  "page": 1
}

Response 401:
{
  "error": "Unauthorized",
  "message": "Token is missing or invalid"
}
```

> Full reference: see [`docs/api-reference.md`](docs/api-reference.md)

---

## Examples

### `example-01-basic-endpoint`

**Demonstrates:** The simplest possible API interaction.

```
Route definition → Controller function → Service call → Response
```

Read this example first. It shows the complete data flow through all layers for a single `GET` endpoint.

### `example-02-crud-operations`

**Demonstrates:** Full Create, Read, Update, Delete lifecycle for one resource.

Includes:
- All four HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- Model definition with database access
- Service layer with business validation
- Unit tests for the service
- Integration tests for the routes

### `example-03-auth-integration`

**Demonstrates:** JWT authentication flow from login to protected resource access.

Includes:
- Login endpoint that issues a token
- Auth middleware that validates incoming tokens
- Protected route that requires a valid token
- Unit tests for token generation and validation
- Integration tests for the full auth flow

---

## Development Workflow

### Branch naming

```
main          ← stable, always deployable
develop       ← integration branch
feature/*     ← new endpoint or feature
fix/*         ← bug correction
docs/*        ← documentation only
chore/*       ← dependencies, config, CI changes
```

### Commit convention

```
feat: add POST /api/v1/users endpoint
fix: return 404 instead of 500 for missing resource
docs: add authentication flow to api-reference.md
test: add integration tests for product CRUD
refactor: extract token logic to auth service
chore: upgrade FastAPI to 0.110
```

### Adding a new endpoint — step by step

```
1. Define the route in src/api/v1/
2. Create the service function in src/services/
3. Add or update the model in src/models/ if needed
4. Write unit tests in tests/unit/
5. Write integration tests in tests/integration/
6. Document the endpoint in docs/api-reference.md
7. Update CHANGELOG.md
```

---

## Best Practices

### Error handling

- Use a global error handler in `src/core/` — no try/catch in every route.
- Return consistent error responses with `error` and `message` fields.
- Never expose stack traces or internal details to the client.
- Use HTTP status codes correctly: 400 (bad input), 401 (unauthenticated), 403 (unauthorized), 404 (not found), 500 (server error).

### Security

- All secrets in environment variables — **never** hardcoded in code.
- Validate and sanitize all incoming data before passing to services.
- Never log passwords, tokens, or sensitive user data.
- Use HTTPS in staging and production.
- Rate-limit public endpoints.

### Performance

- Add database indexes to all columns used in WHERE clauses.
- Paginate list endpoints — never return unbounded results.
- Log response times and monitor for slow endpoints.

### Logging

- Log every request (method, path, status code, response time).
- Log errors with full context (but no sensitive data).
- Use structured logging (JSON format) in production.

---

## Scaling Guidelines

| When your API grows with... | Do this |
|---|---|
| More resources | Add new subdirectories under `src/api/v1/` per resource |
| Breaking API changes | Create `src/api/v2/` — never break v1 |
| More business complexity | Add subdirectories under `src/services/` |
| Multiple databases | Separate models by database in `src/models/` |
| External API integrations | Add `src/integrations/` |
| Background jobs | Add `src/workers/` or a separate worker service |
| Caching needs | Add `src/cache/` |
| Large team | Split into microservices, each with its own `template-backend-api` instance |

---

## Deployment

See [`docs/deployment.md`](docs/deployment.md) for full deployment instructions.

### Quick reference

```bash
# Build for production (language-dependent)
# Python: no build step — install dependencies
pip install -r requirements.txt

# Set environment variables on the server
export APP_ENV=production
export APP_SECRET_KEY=...

# Run with a production server
gunicorn src.main:app --workers 4
```

---

## Roadmap

- [ ] Add language-specific starter configurations (Python/FastAPI, Node.js/Express)
- [ ] Add Docker support (`Dockerfile`, `docker-compose.yml`)
- [ ] Add database migration template (Alembic for Python, Flyway for Java)
- [ ] Add rate limiting middleware example
- [ ] Add OpenAPI/Swagger auto-documentation configuration

---

## References

- [REST API Design Best Practices](https://restfulapi.net/)
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Express.js Guide](https://expressjs.com/en/guide/routing.html)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [The Twelve-Factor App](https://12factor.net/)

---

*Template maintained by Sxik · Part of the proyectos_sena ecosystem.*