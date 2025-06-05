# Migration Plan – Menzis Legacy System

## Step 1: Analysis
- Identify bounded contexts inside the monolith
- Extract modules (e.g. user, claims, billing)

## Step 2: Containerization
- Wrap the monolith in Docker for safe deprecation
- Create separate Dockerfiles for each new service

## Step 3: Microservice Rebuild
- Rewrite critical services like `auth-service` using Spring Boot or Micronaut
- Expose REST endpoints

## Step 4: Deployment
- Define Kubernetes deployment & service YAML
- Use Helm or Kustomize for environments

## Step 5: CI/CD
- Setup GitHub Actions for build/test/deploy pipeline
- Run integration tests on each push to `main`

