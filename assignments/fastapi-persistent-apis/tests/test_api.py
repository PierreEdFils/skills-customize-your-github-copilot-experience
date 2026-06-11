import os
import tempfile
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_crud_and_auth(monkeypatch, tmp_path):
    # run the app using the starter module
    from starter import app, DATABASE, API_KEY

    # use a temp database file
    db_file = tmp_path / 'test.db'
    monkeypatch.setattr('starter.DATABASE', str(db_file))

    async with AsyncClient(app=app, base_url='http://test') as ac:
        # no items initially
        r = await ac.get('/items')
        assert r.status_code == 200
        assert r.json() == []

        # unauthorized create should fail
        r = await ac.post('/items', json={'name':'Pen','description':'Blue','price':1.0})
        assert r.status_code == 401

        # create with API key
        headers = {'Authorization': f'ApiKey {API_KEY}'}
        r = await ac.post('/items', json={'name':'Pen','description':'Blue','price':1.0}, headers=headers)
        assert r.status_code == 201
        item = r.json()
        assert item['id'] == 1

        # read
        r = await ac.get('/items/1')
        assert r.status_code == 200

        # update
        r = await ac.put('/items/1', json={'name':'Pencil','description':'HB','price':0.5}, headers=headers)
        assert r.status_code == 200
        assert r.json()['name'] == 'Pencil'

        # delete
        r = await ac.delete('/items/1', headers=headers)
        assert r.status_code == 204
