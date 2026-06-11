# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a small RESTful API using the FastAPI framework and Pydantic models.

## 📝 Tasks

### 🛠️	Create a CRUD API for "items"

#### Description
Implement a simple REST API that manages a collection of `Item` resources. Each `Item` should include an `id`, `name`, `description`, and `price`.

#### Requirements
Completed project should:

- Provide endpoints for: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, and `DELETE /items/{id}`
- Use Pydantic models for request validation and response models
- Store data in-memory (a Python dict or list) — no database required
- Return appropriate HTTP status codes (201 for create, 404 for not found, etc.)
- Validate input (e.g., `price` must be a positive number)
- Include clear run instructions and examples for testing with `curl` or HTTP client

Optional extensions (not required): add query parameters for filtering, pagination, or integrate a small SQLite persistence layer.

## Starter Code

A starter FastAPI app is provided in `starter-code.py`. Run it locally with Uvicorn:

```bash
pip install -r requirements.txt
python -m uvicorn starter-code:app --reload
```

Example curl requests:

```bash
# List items
curl http://127.0.0.1:8000/items

# Create an item
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name":"Pen","description":"Blue ink","price":1.5}'

# Get item with id 1
curl http://127.0.0.1:8000/items/1
```

## Resources

- FastAPI docs: https://fastapi.tiangolo.com/
- Pydantic docs: https://pydantic-docs.helpmanual.io/
