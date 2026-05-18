<div align="center">

# 📚 Library Management API

**A modern, high-performance RESTful API for managing a digital book collection.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge)](https://docs.pydantic.dev/)

</div>

---

## 📌 About

This project is a RESTful API built to manage a digital book collection. It was developed to demonstrate best practices in Python backend development, including type hinting, asynchronous programming, data validation, and containerization with Docker.

The API provides full CRUD capabilities for book management and comes with interactive auto-generated documentation out of the box.

---

## ✨ Features

- 📖 **Full CRUD** — Create, Read, Update, and Delete book records
- 📝 **Auto Documentation** — Interactive Swagger UI and ReDoc available instantly
- ✅ **Data Validation** — Strict request/response validation using Pydantic v2
- 🗄️ **Database Integration** — SQLAlchemy ORM with SQLite backend
- 🐳 **Dockerized** — Fully containerized for consistent, easy deployment
- ⚡ **Async Ready** — Built on FastAPI for high-performance async endpoints

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Validation | Pydantic v2 |
| Database | SQLite |
| Containerization | Docker |
| Documentation | Swagger UI / ReDoc |

---

## 📁 Project Structure

```
library_api/
├── app/
│   ├── main.py          # API routes and application logic
│   ├── models.py        # Database models (SQLAlchemy)
│   ├── schemas.py       # Data validation schemas (Pydantic)
│   └── database.py      # Database connection configuration
├── assets/              # Screenshots and demo images
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Option 1: Docker (Recommended)

The fastest way to get started — no local Python installation required.

```bash
# 1. Clone the repository
git clone https://github.com/Ramon-Leandro/Library_Management_API.git
cd Library_Management_API

# 2. Build the Docker image
docker build -t library-api .

# 3. Run the container
docker run -p 8000:8000 library-api
```

### Option 2: Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/Ramon-Leandro/Library_Management_API.git
cd Library_Management_API

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the development server
uvicorn app.main:app --reload
```

The server will be available at `http://localhost:8000`.

---

## 📖 API Documentation

Once the server is running, explore the interactive documentation:

| Interface | URL |
|---|---|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/books` | List all books |
| `GET` | `/books/{id}` | Get a single book by ID |
| `POST` | `/books` | Create a new book |
| `PUT` | `/books/{id}` | Update a book by ID |
| `DELETE` | `/books/{id}` | Delete a book by ID |

### Example — Create a Book

**Request:**
```http
POST /books
Content-Type: application/json

{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008,
  "isbn": "9780132350884"
}
```

**Response `201 Created`:**
```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008,
  "isbn": "9780132350884"
}
```

---

## 🖼️ Screenshots

<details>
<summary>Click to expand</summary>

**Initial State**
![Library Initial](./assets/Library%20Initial.png)

**Creating a Book**
![Library Create](./assets/Library%20Create.png)
![Library Create Responses](./assets/Library%20Create%20responses.png)

**Testing Endpoints**
![Library Test](./assets/Library%20Test.png)

**Updating a Record**
![Library Update](./assets/Library%20Update.png)
![Library Update Responses](./assets/Library%20Update%20responses.png)

**Deleting a Record**
![Library Delete](./assets/Library%20Delete.png)

</details>

---

## 🎓 About This Project

This API was developed as a learning exercise to practice core Python backend concepts, including:

- Building RESTful APIs with **FastAPI**
- Implementing ORM-based persistence with **SQLAlchemy**
- Enforcing data contracts with **Pydantic v2**
- Containerizing applications with **Docker**

---

## 👤 Author

**Ramon Leandro**

[![GitHub](https://img.shields.io/badge/GitHub-Ramon--Leandro-181717?style=flat&logo=github)](https://github.com/Ramon-Leandro)
