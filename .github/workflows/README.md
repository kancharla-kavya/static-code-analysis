
# Static Code Analysis Integration in Pipelines

A DevOps project demonstrating static code analysis integration in CI/CD pipelines using GitHub Actions, Docker, and various analysis tools.

## Project Overview

This project showcases:
- **Static Code Analysis** with SonarQube, Pylint, Bandit
- **Security Scanning** with Safety and Bandit
- **Code Quality** with Radon
- **Docker Integration** with security best practices
- **GitHub Actions** CI/CD pipeline

## Tools Used

- **SonarQube** - Comprehensive code quality analysis
- **Pylint** - Python code analysis
- **Bandit** - Security linting
- **Radon** - Code complexity analysis
- **Safety** - Dependency vulnerability scanning
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline

## Local Development

### Prerequisites
- Python 3.9+
- Docker
- Git

### Setup
```bash
# Clone repository
git clone <your-repo-url>
cd static-analysis-project

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run static analysis
pylint app.py
bandit -r .