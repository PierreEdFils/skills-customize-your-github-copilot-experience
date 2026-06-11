# 📘 Assignment: Persistent & Secure REST APIs with FastAPI

## 🎯 Objective

Build a FastAPI application that persists data in SQLite, validates requests with Pydantic, and secures endpoints using a simple API key authentication scheme. Add basic tests to verify core behavior.

## 📝 Tasks

### 🛠️	Implement a Persistent Item API with Auth

#### Description
Extend a FastAPI CRUD application to use SQLite for persistence and protect write endpoints with a simple API key provided in the `Authorization` header.

#### Requirements
Completed project should:

- Use SQLModel or `sqlite3` (your choice) to persist `Item` objects with fields: `id`, `name`, `description`, `price`.
- Provide endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Secure `POST`, `PUT`, and `DELETE` with an API key sent as `Authorization: ApiKey <key>`; return 401 on missing/invalid key
- Validate input using Pydantic models; `price` must be positive
- Include a small test suite using `pytest` and `httpx` to cover create, read, update, delete, and auth failure
- Provide run and test instructions in the README

Optional extensions: implement OAuth2 password flow, add pagination and filtering, or deploy using Docker.

## Starter Files

Starter app, tests, and requirements are provided in this folder. Run the app locally with:

```bash
pip install -r requirements.txt
python -m uvicorn starter:app --reload
```

Run tests with:

```bash
pip install -r requirements-dev.txt
pytest -q
```
