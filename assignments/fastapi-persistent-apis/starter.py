from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel, Field
from typing import Optional, List
import sqlite3

DATABASE = 'items.db'
API_KEY = 'secret-teacher-key'

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0)


def get_db_conn():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_conn()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def require_api_key(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith('ApiKey '):
        raise HTTPException(status_code=401, detail='Missing API Key')
    key = authorization.split(' ', 1)[1]
    if key != API_KEY:
        raise HTTPException(status_code=401, detail='Invalid API Key')


@app.on_event('startup')
def startup():
    init_db()


@app.get('/items', response_model=List[Item])
def list_items():
    conn = get_db_conn()
    cur = conn.execute('SELECT * FROM items')
    rows = cur.fetchall()
    conn.close()
    return [Item(**dict(r)) for r in rows]


@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int):
    conn = get_db_conn()
    cur = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail='Item not found')
    return Item(**dict(row))


@app.post('/items', response_model=Item, status_code=201, dependencies=[Depends(require_api_key)])
def create_item(item: Item):
    conn = get_db_conn()
    cur = conn.execute('INSERT INTO items (name, description, price) VALUES (?, ?, ?)',
                       (item.name, item.description, item.price))
    conn.commit()
    item.id = cur.lastrowid
    conn.close()
    return item


@app.put('/items/{item_id}', response_model=Item, dependencies=[Depends(require_api_key)])
def update_item(item_id: int, item: Item):
    conn = get_db_conn()
    cur = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail='Item not found')
    conn.execute('UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?',
                 (item.name, item.description, item.price, item_id))
    conn.commit()
    conn.close()
    item.id = item_id
    return item


@app.delete('/items/{item_id}', status_code=204, dependencies=[Depends(require_api_key)])
def delete_item(item_id: int):
    conn = get_db_conn()
    cur = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail='Item not found')
    conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return None
