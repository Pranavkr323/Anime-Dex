# 🎌 AnimeDex API

A beginner-friendly **REST API built with FastAPI** to explore and manage anime data.

AnimeDex API started as a simple FastAPI project with in-memory data and has evolved into a backend application using **SQLAlchemy ORM and SQLite database**.

The project demonstrates REST API development with FastAPI, including CRUD operations, database integration, request validation, response models, dependency injection, exception handling, and proper backend architecture.

---

## 🚀 Features

### 📖 Read Operations
- 📚 Get all anime
- 🔍 Get anime by ID

### ✏️ Write Operations
- ➕ Create a new anime
- ♻️ Update an existing anime
- 🗑️ Delete an anime

### 🗄️ Database Integration
- Persistent data storage using SQLite
- SQLAlchemy ORM for database operations
- SQLAlchemy 2.0 style models using `Mapped` and `mapped_column`
- Database session management using FastAPI dependency injection

### ✅ Validation & Error Handling
- Request validation using **Pydantic**
- Response validation using Pydantic models
- Enum validation for anime status
- Field validation using Pydantic `Field`
- Proper HTTP status codes
- 404 error handling using `HTTPException`

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn

---

## 📁 Project Structure

```
AnimeDex-API/
│
├── app/
│   ├── main.py          # FastAPI application and API routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   ├── database.py      # Database configuration and sessions
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/anime` | Get all anime |
| GET | `/anime/{id}` | Get anime by ID |
| POST | `/anime` | Create a new anime |
| PUT | `/anime/{id}` | Update an existing anime |
| DELETE | `/anime/{id}` | Delete an anime |

---

## 📝 Request Body

### Create Anime

```json
{
  "title": "Monster",
  "genre": "Thriller",
  "episodes": 74,
  "rating": 9.2,
  "studio": "Madhouse",
  "release_year": 2004,
  "status": "Completed"
}
```

The same schema is used for updating anime data.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Pranavkr323/Anime-Dex.git
```

### Navigate to the project

```bash
cd Anime-Dex
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the development server

```bash
uvicorn app.main:app --reload
```

---

## 📖 Interactive API Documentation

FastAPI automatically provides interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📸 Preview

FastAPI automatically generates interactive API documentation.

![Swagger UI](screenshot/swagger_ui.png)

---

## 🎯 Learning Outcomes

Through this project, I learned:

- FastAPI fundamentals
- REST API design
- CRUD operations
- SQLAlchemy ORM integration
- Database session management
- Dependency injection using `Depends()`
- Pydantic schemas and validation
- Response models
- Enum validation
- HTTP status codes
- Exception handling
- Separation of API, schema, and database layers
- Swagger UI documentation

---

## 🚧 Future Improvements

- [ ] Move API routes into separate routers
- [ ] PostgreSQL database integration
- [ ] Async database operations
- [ ] JWT Authentication
- [ ] User accounts
- [ ] Anime watchlist/favorites
- [ ] Pagination
- [ ] Unit testing with Pytest
- [ ] Docker support
- [ ] Deploy to Render or Railway

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pranav Kumar**

Backend Developer • Python Enthusiast • FastAPI Learner

GitHub: https://github.com/Pranavkr323  
LinkedIn: https://www.linkedin.com/in/pranav-kumar-4365b2324/

If you liked it, consider giving it a ⭐!