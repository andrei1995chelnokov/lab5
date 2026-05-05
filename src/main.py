from fastapi import FastAPI
from src.routers import user  # импортируем роутер

app = FastAPI(title="User API", version="1.0")

# Подключаем роутер
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "API is working"}
    
    
@router.post("/login")
def login(username: str, password: str):
    """Авторизация (упрощённая версия для тестов)"""
    if username == "user" and password == "password":
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
