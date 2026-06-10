# Configuration

## Purpose

The `config/` directory contains configuration examples and environment-specific settings used by backend applications.

Its purpose is to centralize all configurable values and infrastructure settings that may change between environments without requiring code modifications.

Configuration should be externalized from application logic whenever possible.

This directory exists to demonstrate how professional backend projects organize configuration in a maintainable and scalable way.

---

## What Is Configuration?

Configuration is any value that may vary depending on:

* Environment
* Infrastructure
* Deployment target
* Security requirements
* Operational needs

Examples:

* Database connection settings
* Logging levels
* Cache configuration
* External service URLs
* Feature flags
* Environment variables

A common principle is:

> Configuration changes frequently. Code should not.

---

## Responsibilities

The configuration layer is responsible for:

* Defining environment-specific settings
* Centralizing infrastructure configuration
* Supporting multiple deployment environments
* Reducing hardcoded values
* Improving maintainability
* Improving deployment consistency

---

## Directory Structure

```text
config/
├── README.md
├── database.yml
├── environments.yml
└── logging.yml
```

---

## Files Overview

### database.yml

Contains database-related settings.

Examples:

* Host
* Port
* Database name
* Connection pool settings
* Read replicas

Example:

```yaml
development:
  host: localhost
  port: 5432

production:
  host: db-production
  port: 5432
```

---

### environments.yml

Contains environment-specific application behavior.

Examples:

* Debug mode
* Feature flags
* Environment identifiers
* Runtime settings

Example:

```yaml
development:
  debug: true

production:
  debug: false
```

---

### logging.yml

Contains logging configuration.

Examples:

* Log levels
* Output formats
* Log destinations
* Rotation policies

Example:

```yaml
development:
  level: DEBUG

production:
  level: INFO
```

---

## Should Contain

Examples of configuration that belongs here:

* Database settings
* Cache settings
* Logging configuration
* Message queue configuration
* External service endpoints
* Environment-specific values
* Feature toggles
* Application settings

---

## Should NOT Contain

The configuration layer should not contain:

* Business rules
* Application workflows
* HTTP routes
* Controllers
* Database queries
* Service logic
* Domain-specific decisions

Incorrect examples:

```text
User registration logic
Payment validation rules
Authorization workflows
```

These belong in the Services layer.

---

## Environment Separation

Professional applications typically support multiple environments.

Common environments include:

```text
Development
Staging
Production
```

---

### Development

Purpose:

* Local development
* Testing new features

Typical settings:

```yaml
debug: true
logging: DEBUG
database: localhost
```

Characteristics:

* Maximum visibility
* Detailed logs
* Fast feedback

---

### Staging

Purpose:

* Pre-production validation
* Integration testing

Typical settings:

```yaml
debug: false
logging: INFO
database: staging-db
```

Characteristics:

* Similar to production
* Safe testing environment

---

### Production

Purpose:

* Real users
* Live workloads

Typical settings:

```yaml
debug: false
logging: WARNING
database: production-db
```

Characteristics:

* Stability first
* Security first
* Performance focused

---

## Configuration Hierarchy

A common configuration flow is:

```text
Default Configuration
          ↓
Environment Configuration
          ↓
Environment Variables
          ↓
Runtime Values
```

Environment variables should override static configuration whenever possible.

---

## Relationship With Other Layers

```text
          Config
             │
 ┌───────────┼───────────┐
 │           │           │
API       Services     Models
```

Configuration supports all layers but should remain independent from business logic.

---

## Best Practices

* Keep configuration outside source code
* Avoid hardcoded values
* Separate environments clearly
* Store secrets in environment variables
* Use descriptive configuration names
* Document every configuration option
* Keep configuration files version controlled when safe

---

## Common Mistakes

* Hardcoding credentials
* Mixing business logic with configuration
* Using the same settings for all environments
* Storing secrets in repositories
* Duplicating configuration across files
* Creating environment-specific code branches

---

## Security Considerations

Sensitive information should never be committed to source control.

Examples:

```text
Passwords
API Keys
Private Keys
Tokens
Certificates
Secrets
```

Instead:

```text
.env
Secret Managers
Environment Variables
Vault Solutions
```

Use `.env.example` files only to document required values.

---

## Summary

The `config/` directory centralizes environment-dependent settings and infrastructure configuration.

Its purpose is to separate operational concerns from application logic, improve maintainability, and support multiple deployment environments without modifying source code.
