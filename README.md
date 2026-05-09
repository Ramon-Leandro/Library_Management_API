# 📚 Library Management System (API)

A modern, high-performance RESTful API for managing a digital book collection. This project was developed to demonstrate best practices in Python development, including Type Hinting, Asynchronous Programming, and Containerization.

## 🚀 Key Features

* **Full CRUD Operations:** Create, Read, Update, and Delete book records.
* **Automatic Documentation:** Interactive API documentation powered by Swagger UI.
* **Data Validation:** Strict data validation and serialization using Pydantic v2.
* **Database Integration:** Robust ORM implementation using SQLAlchemy with a SQLite backend.
* **Dockerized:** Fully containerized environment for seamless deployment.

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Containerization** Docker
* **Validation:** Pydantic

### 🖼️ Project Gallery

<details>
<summary>
Gallery
</summary>

* **Library initial**
![](./assets/Library%20Initial.png)

* **Library create and responses**
![](./assets/Library%20Create.png)
![](./assets/Library%20Create%20responses.png)

* **Library test**
![](./assets/Library%20Test.png)

* **Library update and responses**
![](./assets/Library%20Update.png)
![](./assets/Library%20Update%20responses.png)

* **Library delete**
![](./assets/Library%20Delete.png)
    
</details>

## 📦 Installation & Setup

### Option 1: Running with Docker (Recommended)

This is the easiest way to run the project. No local Python installation is required.

Build the Image:
*    `docker build -t library-api .`

Run the Container:
*    `docker run -p 8000:8000 library-api`

### Option 2: Local Manual Setup

Create a Virtual Environment:
*    `python -m venv venv`

Activate & Install Dependencies:
*    `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
*    `pip install -r requirements.txt`

Start the Server:
*    `uvicorn app.main:app --reload`

## 📖 API Documentation

Once the server is running, you can access the interactive documentation at:

* **Swagger UI:** http://localhost:8000/docs
* **ReDoc:** http://localhost:8000/redoc

## 📁 Project Structure

    library_api/
    ├── app/
    ├── main.py              # API Routes & Logic
    │   ├── models.py        # Database Models (SQLAlchemy)
    │   ├── schemas.py       # Data Validation (Pydantic)
    │   └── database.py      # Connection Configuration
    ├── Dockerfile           # Container Configuration
    ├── requirements.txt     # Dependency List
    └── README.md            # Documentation


## 🎓 Final Considerations (Academic Purpose)

This project was developed strictly for academic and learning purposes. It serves as a practical exercise to explore the FastAPI ecosystem, SQLAlchemy ORM, and Docker containerization.
