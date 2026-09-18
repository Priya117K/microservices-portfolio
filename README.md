# 🚀 Containerized Microservices E-Commerce Platform

A **production-style, containerized e-commerce platform** built using a modern microservices architecture. The project combines a responsive SaaS dashboard, independently deployable Flask services, persistent MySQL storage, and Docker Compose orchestration into a complete full-stack application.

![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Containerized-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Flask-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge\&logo=react\&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3-06B6D4?style=for-the-badge\&logo=tailwindcss\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)

---

## ✨ Overview

This project demonstrates how a traditional monolithic e-commerce application can be structured as a set of **independent microservices**, each responsible for a specific business capability.

The application provides:

* 🛒 Interactive e-commerce shopping experience
* 🔐 Dedicated authentication service
* 📦 Independent product management service
* 🧾 Order processing service
* 💾 Persistent MySQL database storage
* 📊 Real-time service health monitoring
* 🐳 Fully containerized development environment
* 🎨 Modern SaaS-style dashboard interface
* 🔄 REST-based communication between services

The entire application can be started with a **single Docker Compose command**.

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────────┐
                         │      React Dashboard    │
                         │     React + Tailwind    │
                         └────────────┬────────────┘
                                      │
                                      │ HTTP / REST
                                      ▼
                 ┌────────────────────────────────────┐
                 │          Docker Network             │
                 │                                    │
                 │   ┌──────────────┐                 │
                 │   │ Auth Service  │                 │
                 │   │ Flask :5001  │                 │
                 │   └───────┬──────┘                 │
                 │           │                         │
                 │   ┌───────▼──────┐                 │
                 │   │  Products    │                 │
                 │   │  Flask :5002 │                 │
                 │   └───────┬──────┘                 │
                 │           │                         │
                 │   ┌───────▼──────┐                 │
                 │   │   Orders     │                 │
                 │   │  Flask :5003 │                 │
                 │   └───────┬──────┘                 │
                 │           │                         │
                 │   ┌───────▼──────┐                 │
                 │   │    MySQL     │                 │
                 │   │     :3306    │                 │
                 │   └──────────────┘                 │
                 │                                    │
                 └────────────────────────────────────┘
```

### Service Responsibilities

| Service                |   Port | Responsibility                           |
| ---------------------- | -----: | ---------------------------------------- |
| **Frontend Dashboard** | `8080` | User interface and e-commerce experience |
| **Auth Service**       | `5001` | Authentication and JWT-based sessions    |
| **Products Service**   | `5002` | Product catalogue and product APIs       |
| **Orders Service**     | `5003` | Cart checkout and order processing       |
| **MySQL**              | `3306` | Persistent application data              |

Each backend service runs inside its own container, allowing the services to be developed, deployed, and scaled independently.

---

# 🛠️ Tech Stack

### Frontend

* **React 18**
* **Tailwind CSS**
* **Lucide Icons**
* **Nginx**
* Dynamic product imagery

### Backend

* **Python**
* **Flask**
* **REST APIs**
* **CORS**
* **JSON Web Tokens (JWT)**

### Database

* **MySQL 8.0**
* Docker-managed persistent volumes

### Infrastructure

* **Docker**
* **Docker Compose**
* Isolated Docker bridge network
* Multi-container application orchestration

---

# 🎯 Key Features

## 🖥️ Modern SaaS Dashboard

A responsive dashboard-inspired interface designed around a modern SaaS experience.

* Dark-mode sidebar navigation
* Responsive layouts
* Product catalogue
* Interactive UI components
* Clean dashboard-style navigation

  <img width="1352" height="636" alt="image" src="https://github.com/user-attachments/assets/7232db01-7c7d-4b21-9504-6a60d447c3ad" />
  <img width="1351" height="620" alt="image" src="https://github.com/user-attachments/assets/54a7375c-d4b9-421c-83fb-60bda3844c39" />
  <img width="1366" height="631" alt="image" src="https://github.com/user-attachments/assets/ea48b73d-a2a2-49df-8927-1409bec44ae1" />
  <img width="1366" height="635" alt="image" src="https://github.com/user-attachments/assets/22f71f88-e598-44c1-b13f-92d7c124bf4a" />
  <img width="1364" height="634" alt="image" src="https://github.com/user-attachments/assets/68538827-d73e-40ce-99fe-61389cc23aab" />





## 🔐 Authentication

Dedicated authentication microservice responsible for:

* User authentication
* JWT token handling
* Session persistence
* Secure communication with protected services

## 📦 Product Service

The product microservice provides REST endpoints for:

* Product retrieval
* Product catalogue management
* Product information
* Frontend product rendering

## 🛒 Shopping Cart & Checkout

The frontend provides an interactive shopping workflow including:

* Add-to-cart functionality
* Slide-out cart drawer
* Cart quantity management
* Checkout workflow
* Order submission

## 📊 Real-Time Service Monitoring

The dashboard includes a service-health interface that monitors the availability of individual backend services.

This provides a visual representation of the distributed application's operational state.

## 💾 Persistent Storage

MySQL runs inside Docker with persistent volumes, ensuring that application data survives container restarts.

## 🔄 Independent Microservices

Each backend capability is isolated into its own service, providing:

* Separation of responsibilities
* Independent development
* Service isolation
* Easier maintenance
* Scalable architecture

---

# 📁 Project Structure

```text
microservices-portfolio/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   └── ...
│
├── auth-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── products-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── orders-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── database/
│   └── ...
│
├── docker-compose.yml
└── README.md
```

> The exact directory structure may vary depending on the current implementation.

---

# 🚀 Getting Started

## Prerequisites

Make sure you have the following installed:

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Git

Docker Desktop should be running before starting the application.

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Priya117K/microservices-portfolio.git
```

### 2. Navigate to the project

```bash
cd microservices-portfolio
```

### 3. Build and start all services

```bash
docker compose up --build -d
```

Docker Compose will:

1. Build the frontend container
2. Build each Flask microservice
3. Create the Docker network
4. Start the MySQL database
5. Create persistent database storage
6. Start all application services

---

# 🌐 Access the Application

Once all containers are running:

| Application                  | URL                   |
| ---------------------------- | --------------------- |
| 🛍️ **E-Commerce Dashboard** | http://localhost:8080 |
| 🔐 **Auth Service API**      | http://localhost:5001 |
| 📦 **Products Service API**  | http://localhost:5002 |
| 🧾 **Orders Service API**    | http://localhost:5003 |

Open the dashboard in your browser:

```text
http://localhost:8080
```

---

# 🐳 Docker Commands

### Start the application

```bash
docker compose up -d
```

### Rebuild containers

```bash
docker compose up --build -d
```

### View running containers

```bash
docker compose ps
```

### View application logs

```bash
docker compose logs
```

### View logs for a specific service

```bash
docker compose logs auth-service
```

### Stop the application

```bash
docker compose down
```

### Stop and remove persistent volumes

```bash
docker compose down -v
```

> ⚠️ Removing volumes can delete persisted database data.

---

# 🔌 API Architecture

The backend follows a service-oriented REST architecture.

```text
Frontend
   │
   ├── Authentication ──────► Auth Service
   │
   ├── Products ─────────────► Products Service
   │
   └── Checkout / Orders ────► Orders Service
                                  │
                                  ▼
                               MySQL
```

Each service exposes its own REST endpoints and communicates through the Docker network.

---

# 🧠 What This Project Demonstrates

This project was built to demonstrate practical understanding of:

* Microservices architecture
* RESTful API development
* Containerization
* Docker networking
* Docker Compose orchestration
* Service isolation
* Authentication with JWT
* Frontend-backend integration
* Database persistence
* Distributed application health monitoring
* Full-stack application development

---

# 🔮 Future Improvements

Potential extensions to the architecture include:

* API Gateway
* Redis caching
* Message broker integration
* Centralized logging
* Prometheus & Grafana monitoring
* CI/CD pipeline
* Kubernetes deployment
* Service-level authentication
* Automated testing
* Cloud deployment

---

# 👨‍💻 Author

### Priyadharshini K

**Computer Science & Engineering**

Built as a full-stack portfolio project exploring **microservices, containerization, backend engineering, and modern web application architecture**.

🔗 **GitHub:**
https://github.com/Priya117K

🔗 **Portfolio:**
https://portfolio-deployers7.vercel.app

---

## ⭐ If you found this project interesting

Feel free to explore the repository, experiment with the architecture, and build upon it.

**Built with React, Flask, MySQL & Docker. 🚀**
