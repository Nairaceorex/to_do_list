from fastapi import FastAPI
from app import models, database

app = FastAPI()

# Создание всех таблиц, если их еще нет
models.Base.metadata.create_all(bind=database.engine)


# Пример эндпоинта
@app.get("/")
def read_root():
    return {"Hello": "World"}
