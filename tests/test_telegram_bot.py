from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_random_number_endpoint():
    response = client.post('/telegram-bot/random-number/')
    assert response.status_code == 200
    assert 'Number inserted' in response.text


def test_random_string_endpoint():
    test_string = 'Hello, world!'
    response = client.post('/telegram-bot/string/', data={'string': test_string})
    assert response.status_code == 200
    assert f'String inserted: {test_string}' in response.text
