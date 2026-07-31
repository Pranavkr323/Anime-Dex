# 🎌 AnimeDex API

A beginner-friendly **REST API built with FastAPI** to explore and manage anime data.

AnimeDex started as a simple FastAPI project using in-memory data and gradually evolved into a backend application powered by **SQLAlchemy ORM** and **SQLite**. The project demonstrates how to design RESTful APIs, interact with databases, validate requests, and organize backend code using industry-standard practices.

---

## 🚀 Features

### 📖 Read Operations

* 📚 Get all anime
* 🔍 Get anime by ID
* 🎲 Get a random anime
* 🏆 Get the top 10 highest-rated anime
* 🏷️ Retrieve all available genres
* 🎬 Retrieve all available studios
* 📌 Retrieve all available anime statuses

### 🔎 Filtering

Filter anime using query parameters.

Examples:

```http
GET /anime?genre=Action
```

```http
GET /anime?studio=Madhouse
```

```http
GET /anime?status=Completed
```

```http
GET /anime?genre=Action&studio=MAPPA
```

Multiple filters can be combined in a single request.

### ✏️ Write Operations

* ➕ Create a new anime
* ♻️ Update an existing anime
* 🗑️ Delete an anime

### 🗄️ Database Integration

* Persistent storage using SQLite
* SQLAlchemy ORM
* SQLAlchemy 2.0 style models using `Mapped` and `mapped_column`
* Dependency-injected database sessions using FastAPI

### ✅ Validation & Error Handling

* Request validation using Pydantic
* Response serialization using Pydantic response models
* Enum validation for anime status
* Field validation using Pydantic `Field`
* Proper HTTP status codes
* Error handling using `HTTPException`

---

## 🛠️ Tech Stack

* Python 3
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* Uvicorn

---

## 📁 Project Structure

```text
Anime-Dex/
│
├── app/
│   ├── crud.py          # Database operations
│   ├── database.py      # Database configuration & session management
│   ├── enums.py         # Enum definitions
│   ├── main.py          # FastAPI application & API routes
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── __init__.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

## 📡 API Endpoints

| Method | Endpoint          | Description                        |
| ------ | ----------------- | ---------------------------------- |
| GET    | `/`               | API home                           |
| GET    | `/anime`          | Get all anime (supports filtering) |
| GET    | `/anime/{id}`     | Get anime by ID                    |
| GET    | `/anime/random`   | Get a random anime                 |
| GET    | `/anime/top10`    | Get the top 10 highest-rated anime |
| GET    | `/anime/genres`   | Get all unique genres              |
| GET    | `/anime/studios`  | Get all unique studios             |
| GET    | `/anime/statuses` | Get all unique anime statuses      |
| POST   | `/anime`          | Create a new anime                 |
| PUT    | `/anime/{id}`     | Update an existing anime           |
| DELETE | `/anime/{id}`     | Delete an anime                    |

---

## 📝 Sample Request Body

### Create / Update Anime

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

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 Interactive API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 📸 Preview

FastAPI automatically generates interactive API documentation.

screenshot/swagger_ui.png

```text
screenshot/swagger_ui.png
```

---

## 🎯 What I Learned

This project helped me learn:

* FastAPI fundamentals
* REST API design
* CRUD operations
* SQLAlchemy ORM
* SQLite integration
* SQLAlchemy 2.0 style models
* Database session management
* Dependency injection using `Depends()`
* Pydantic schemas
* Request & response validation
* Enum validation
* Query parameters
* Dynamic query building
* Filtering with SQLAlchemy
* Sorting using `order_by()`
* Limiting results using `limit()`
* Retrieving distinct values using `distinct()`
* Random database queries using SQL functions
* HTTP status codes
* Exception handling with `HTTPException`
* Separation of API, schema, and database layers
* Interactive API documentation with Swagger UI

---

## 🚧 Future Improvements

* [ ] Add PATCH endpoint for partial updates
* [ ] Modularize routes using `APIRouter`
* [ ] Database migrations using Alembic
* [ ] PostgreSQL support
* [ ] User authentication
* [ ] Anime watchlists & favorites
* [ ] Async SQLAlchemy
* [ ] Pagination
* [ ] Unit testing with Pytest
* [ ] Docker support
* [ ] Deploy to Render or Railway

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pranav Kumar**

Backend Developer • Python Enthusiast • FastAPI Learner

* GitHub: https://github.com/Pranavkr323
* LinkedIn: https://www.linkedin.com/in/pranavkr323/

If you found this project helpful or interesting, consider giving it a ⭐.
