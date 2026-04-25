import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_api_message(client):
    response = client.get('/api/message')
    assert response.status_code == 200