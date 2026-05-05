from fastapi import FastAPI, HTTPException, Form
from src.routers import user

app = FastAPI(title="User API", version="1.0")

app.include_router(user)


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    """Авторизация (упрощённая версия для тестов)"""
    if username == "user" and password == "password":
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/")
def root():
    return {"message": "API is working"}
