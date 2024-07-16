import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from server import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_random_number():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.post('/telegram-bot/random-number/')
    assert response.status_code == 200
    assert 'Number inserted:' in response.text


@pytest.mark.asyncio
async def test_random_string():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.post('/telegram-bot/string/', data={'string': 'test string 1234'})
    assert response.status_code == 200
    assert response.text == 'String inserted: test string 1234'
