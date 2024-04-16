''' Задание №1
Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте модель User со следующими полями:
○ id: int (идентификатор пользователя, генерируется автоматически)
○ username: str (имя пользователя)
○ email: str (электронная почта пользователя)
○ password: str (пароль пользователя)

API должно поддерживать следующие операции:
○ Получение списка всех пользователей: GET /users/
○ Получение информации о конкретном пользователе: GET /users/{user_id}/
○ Создание нового пользователя: POST /users/
○ Обновление информации о пользователе: PUT /users/{user_id}/
○ Удаление пользователя: DELETE /users/{user_id}/
Для валидации данных используйте параметры Field модели User.
Для работы с базой данных используйте SQLAlchemy и модуль databases.'''
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///my_database.db"  # создаем базу данны=
database = databases.Database(DATABASE_URL)  # переменная из класса Database
metadata = sqlalchemy.MetaData()  # метаданные

app = FastAPI()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String(30)),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('password', sqlalchemy.String(6)),
)


class UserIn(BaseModel):
    username: str = Field(..., max_length=30)
    email: str = Field(..., max_length=50)
    password: str = Field(..., max_length=6)


class User(UserIn):  # наследуюем
    id: int


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


# @app.get("/create_table/{count}")
# async def create_table(count: int):
#     for i in range(count):
#         query = users.insert().values(username=f'user{i}', email=f'mail{i}@mail.ru', password=f'1111{i}')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}

@app.get("/users/", response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def get_user(users_id: int):
    query = users.select().where(users.c.id == users_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=UserIn)
async def create_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    create_id = await database.execute(query)
    return await get_user(create_id)


@app.put("/users/{user_id}", response_model=User)
async def update_user(users_id: int, user: UserIn):
    query = users.update().where(users.c.id == users_id).values(**user.model_dump())
    await database.execute(query)
    return await get_user(users_id)


@app.delete("/users/{user_id}")
async def delite_user(users_id: int):
    query = users.delete().where(users.c.id == users_id)
    await database.execute(query)
    return {'msg': 'Delete'}
