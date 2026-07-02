# Book Store — Full-Stack Python Web App with CI/CD Pipeline

> Python · Flask · Docker · Kubernetes · Jenkins · Nginx · Automated Testing

---

## What is this project?

A full-stack bookstore web application built with Python Flask, containerised with Docker, served behind an Nginx reverse proxy, deployed on Kubernetes, and integrated with a Jenkins CI/CD pipeline for automated testing and deployment.

The project demonstrates a complete software delivery lifecycle — from local development to containerised production deployment with automated quality gates.

---

## Architecture
Browser
↓
Nginx (reverse proxy)
↓
Flask Application (app.py)
↓
SQLite Database (database.db)
↓
books.json (seed data)

**Deployment stack:**
Jenkins Pipeline
↓ (on push)
Docker Build → Docker Compose (local)
↓
Kubernetes Deployment (deployement.yaml)

---

## Tech Stack

| Component | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Frontend** | HTML/CSS (templates/), static assets |
| **Database** | SQLite |
| **Reverse Proxy** | Nginx |
| **Containerisation** | Docker, Docker Compose |
| **Orchestration** | Kubernetes |
| **CI/CD** | Jenkins |
| **Testing** | Automated test suite (tests/) |

---

## Key Features

- Browse and manage a book catalogue
- Full CRUD operations via Flask REST backend
- Nginx reverse proxy for production-grade request handling
- Dockerised with multi-container support via docker-compose
- Kubernetes deployment manifest for scalable orchestration
- Jenkins pipeline with automated test execution before deployment
- Automated test runner script (run_tests.sh)

---

## CI/CD Pipeline

The Jenkins pipeline (Jenkinsfile) automates the full delivery process:

1. **Build** — Docker image is built from the Dockerfile
2. **Test** — automated tests run via run_tests.sh
3. **Deploy** — if tests pass, the app is deployed via Kubernetes

---

## Local Setup

### Run with Docker Compose

docker-compose up --build

The app will be available at http://localhost

### Run without Docker

pip install -r requirements.txt
python app.py

### Run tests

bash run_tests.sh

---

## Project Structure

├── app.py                 # Flask application entry point
├── books.json             # Seed data for the book catalogue
├── database.db            # SQLite database
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container build instructions
├── docker-compose.yml     # Multi-container local setup
├── nginx.conf             # Nginx reverse proxy configuration
├── deployement.yaml       # Kubernetes deployment manifest
├── Jenkinsfile            # CI/CD pipeline definition
├── run_tests.sh           # Test runner script
├── templates/             # HTML templates (Jinja2)
├── static/                # CSS and static assets
└── tests/                 # Automated test suite

---

## What I Learned

This project was built to develop hands-on experience with the full DevOps lifecycle — moving beyond writing application code to understanding how software is containerised, tested automatically, and deployed reliably at scale using industry-standard tooling.
