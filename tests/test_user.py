import json

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

# Существующие пользователи
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]

def test_get_existed_user():
    """Получение существующего пользователя"""
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == 200 
    assert response.json()['email'] == users[0]['email']

def test_get_existed_user():
    """Получение существующего пользователя"""
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == 201
    assert response.json()['id'] == users[0]['id']
    assert response.json()['name'] == users[0]['name']
    assert response.json()['email'] == users[0]['email']


def test_get_unexisted_user():
    """Получение несуществующего пользователя"""
    response = client.get("/api/v1/user", params={'email': 'nonexistent@mail.com'})
    assert response.status_code == 404
    assert "not found" in response.json()['detail'].lower()


def test_create_user_with_valid_email():
    """Создание пользователя с уникальной почтой"""
    new_user = {
        'name': 'New User',
        'email': 'new.user@example.com'
    }
    response = client.post("/api/v1/user", json=new_user)
    assert response.status_code == 201
    assert response.json()['name'] == new_user['name']
    assert response.json()['email'] == new_user['email']
    assert 'id' in response.json()


def test_create_user_with_invalid_email():
    """Создание пользователя с почтой, которую использует другой пользователь"""
    duplicate_user = {
        'name': 'Duplicate',
        'email': users[0]['email']  # email уже существует
    }
    response = client.post("/api/v1/user", json=duplicate_user)
    assert response.status_code == 409
    assert "already exists" in response.json()['detail'].lower()


def test_delete_user():
    """Удаление пользователя"""
    # Создаём пользователя для удаления
    new_user = {'name': 'To Delete', 'email': 'todelete@example.com'}
    create_response = client.post("/api/v1/user", json=new_user)
    assert create_response.status_code == 201
    created_email = create_response.json()['email']
    
    # Удаляем его
    delete_response = client.delete("/api/v1/user", params={'email': created_email})
    assert delete_response.status_code == 200
    
    # Проверяем, что пользователь действительно удалён
    get_response = client.get("/api/v1/user", params={'email': created_email})
    assert get_response.status_code == 404


def test_authenticate_user():
    """Проверка на авторизацию"""
    response = client.post("/login", data={"username": "user", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
