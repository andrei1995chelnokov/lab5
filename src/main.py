from fastapi import FastAPI, HTTPException
from src.routers import user_router

app = FastAPI(title="User API", version="1.0")

app.include_router(user_router)


# Добавляем эндпоинт /login прямо сюда
@app.post("/login")
def login(username: str, password: str):
    """Авторизация (упрощённая версия для тестов)"""
    if username == "user" and password == "password":
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/")
def root():
    return {"message": "API is working"}
