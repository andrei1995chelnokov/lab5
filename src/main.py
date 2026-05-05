from fastapi import FastAPI, HTTPException
from src.routers import user  # ← импортируем как user (то, что реально экспортируется)

app = FastAPI(title="User API", version="1.0")

# Подключаем роутер
app.include_router(user)

# Добавляем эндпоинт /login
@app.post("/login")
def login(username: str, password: str):
    """Авторизация (упрощённая версия для тестов)"""
    if username == "user" and password == "password":
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/")
def root():
    return {"message": "API is working"}
