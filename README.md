# Menzis Java Legacy Modernization

This project simulates the modernization of a monolithic Java-based legacy system at Menzis. The goal is to refactor the existing Spring-based monolith into scalable, containerized microservices deployed via Kubernetes with CI/CD automation.

## Goals
- Analyze and isolate legacy modules
- Split into REST-based microservices
- Containerize and deploy on Kubernetes
- Automate via GitHub Actions

## Structure
- `legacy/`: Original monolithic Java app
- `modernized/`: Refactored core logic
- `services/`: Microservices (e.g., auth, billing)
- `docker/`: Dockerfiles per service
- `k8s/`: Kubernetes deployment files
- `cicd/`: CI/CD pipeline configuration
- `scripts/`: Migration plans & rollout logic


