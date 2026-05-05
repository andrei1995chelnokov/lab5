from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/api/v1", tags=["users"])

# Хранилище пользователей (временно, в памяти)
users_db = [
    {"id": 1, "name": "Ivan Ivanov", "email": "i.i.ivanov@mail.com"},
    {"id": 2, "name": "Petr Petrov", "email": "p.p.petrov@mail.com"},
]
next_id = 3


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr


@router.get("/user", response_model=UserResponse)
def get_user(email: str = Query(..., description="Email пользователя")):
    """Получение пользователя по email"""
    for user in users_db:
        if user["email"] == email:
            return user
    raise HTTPException(status_code=404, detail=f"User with email '{email}' not found")


@router.post("/user", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    """Создание нового пользователя"""
    # Проверяем, существует ли пользователь с таким email
    for existing_user in users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=409,
                detail=f"User with email '{user.email}' already exists"
            )

    # Создаём нового пользователя
    global next_id
    new_user = {
        "id": next_id,
        "name": user.name,
        "email": user.email
    }
    users_db.append(new_user)
    next_id += 1
    return new_user


@router.delete("/user")
def delete_user(email: str = Query(..., description="Email пользователя")):
    """Удаление пользователя по email"""
    global users_db
    for i, user in enumerate(users_db):
        if user["email"] == email:
            del users_db[i]
            return {"message": f"User '{email}' deleted successfully"}

    raise HTTPException(status_code=404, detail=f"User with email '{email}' not found")


@router.post("/login")
def login(username: str, password: str):
    """Авторизация (упрощённая версия для тестов)"""
    if username == "user" and password == "password":
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
