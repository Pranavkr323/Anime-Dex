# 🎌 AnimeDex API

A beginner-friendly REST API built with **FastAPI** to explore anime data through clean and simple endpoints.

This project was created while learning FastAPI fundamentals and demonstrates API routing, path parameters, query parameters, filtering, sorting, and HTTP exception handling.

---

## 🚀 Features

- 📚 Get all anime
- 🔍 Get anime by ID
- 🎲 Get a random anime
- ⭐ Get Top 10 highest-rated anime
- 🎭 Filter anime by genre
- 📺 Filter anime by status
- 🏢 Filter anime by studio
- 📂 List all available genres
- 📋 List all available statuses
- 🎬 List all available studios
- ❌ Proper 404 error handling using `HTTPException`

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- Uvicorn

---

## 📁 Project Structure

```
AnimeDex-API/
│
├── main.py            # FastAPI application
├── data.py            # Anime dataset
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
| GET | `/anime/random` | Get a random anime |
| GET | `/anime/top10` | Get Top 10 highest-rated anime |
| GET | `/anime/genres` | Get all available genres |
| GET | `/anime/status` | Get all available statuses |
| GET | `/anime/studio` | Get all available studios |

---

## 🔎 Query Parameters

The `/anime` endpoint supports filtering.

### Filter by Genre

```
GET /anime?genre=Action
```

### Filter by Status

```
GET /anime?status=Completed
```

### Filter by Studio

```
GET /anime?studio=MAPPA
```

You can also combine filters:

```
GET /anime?genre=Action&status=Completed
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/animedex-api.git
```

### Navigate to the project

```bash
cd animedex-api
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

### Run the server

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

Once the server is running, visit:

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📸 Preview

FastAPI automatically generates interactive API documentation.
![AnimeDex API Swagger UI](screenshot/swagger-ui.png)

```
docs/images/swagger-ui.png
```

---

## 🎯 Learning Outcomes

This project helped me understand:

- FastAPI project structure
- API routing
- REST principles
- Path parameters
- Query parameters
- Filtering data
- Sorting responses
- HTTP status codes
- Exception handling
- Returning JSON responses

---

## 🚧 Future Improvements

- [ ] Add Pydantic models
- [ ] Implement POST endpoints
- [ ] Implement PUT endpoints
- [ ] Implement DELETE endpoints
- [ ] Add request validation
- [ ] Integrate SQLite
- [ ] Use SQLAlchemy ORM
- [ ] Add JWT Authentication
- [ ] Add pagination
- [ ] Deploy the API

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

Feel free to fork this repository and open a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pranav Kumar**

Backend Developer | Python Enthusiast | FastAPI Learner

GitHub: https://github.com/Pranavkr323