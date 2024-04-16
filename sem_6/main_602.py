''' Задание №2
Создать веб-приложение на FastAPI, которое будет предоставлять API для
работы с базой данных пользователей. Пользователь должен иметь следующие поля:
○ ID (автоматически генерируется при создании пользователя)
○ Имя (строка, не менее 2 символов)
○ Фамилия (строка, не менее 2 символов)
○ Дата рождения (строка в формате "YYYY-MM-DD")
○ Email (строка, валидный email)
○ Адрес (строка, не менее 5 символов)

API должен поддерживать следующие операции:
○ Добавление пользователя в базу данных
○ Получение списка всех пользователей в базе данных
○ Получение пользователя по ID
○ Обновление пользователя по ID
○ Удаление пользователя по ID
Приложение должно использовать базу данных SQLite3 для хранения пользователей. '''
from typing import List
from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, PastDate
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///my_database_602.db"  # создаем базу данны=
database = databases.Database(DATABASE_URL)  # переменная из класса Database
metadata = sqlalchemy.MetaData()  # метаданные

app = FastAPI()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('firstname', sqlalchemy.String(30)),
    sqlalchemy.Column('lastname', sqlalchemy.String(30)),
    sqlalchemy.Column('birthday', sqlalchemy.Date()),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('address', sqlalchemy.String(20)),
)


class UserIn(BaseModel):
    firstname: str = Field(..., max_length=30)
    lastname: str = Field(..., max_length=30)
    birthday: PastDate
    email: EmailStr = Field(..., max_length=50)
    address: str = Field(..., max_length=20)


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
    # return {**user.model_dump(), "id": users_id}


@app.delete("/users/{user_id}")
async def delite_user(users_id: int):
    query = users.delete().where(users.c.id == users_id)
    await database.execute(query)
    return {'msg': 'Delete'}
