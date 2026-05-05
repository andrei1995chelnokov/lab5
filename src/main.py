from fastapi import FastAPI
from src.routers import user

app = FastAPI(title="User API", version="1.0")

# Подключаем роутер
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "API is working"}
