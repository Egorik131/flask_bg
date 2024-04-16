'''Задание №3,4,5,6
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
+4 - Создайте маршрут для обновления информации о пользователе (метод PUT).
+5 - Создайте маршрут для удаления информации о пользователе (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
+6 - Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
+6 - Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
+6 - Создайте маршрут для отображения списка пользователей (метод GET).
'''

from fastapi import FastAPI, HTTPException, Request
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./hw_5/templates")


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: str


user_1 = User(id=1, name='Egor', email='egor@egor.ru', password='123456')
user_2 = User(id=2, name='Ivan', email='ivan@ivan.ru', password='456789')

users = [user_1, user_2]


@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", {"request": request, 'title': 'Главная страница'})


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    global users
    return templates.TemplateResponse("users.html",
                                      {"request": request, 'users': users, 'title': 'Список пользователей'})


@app.post("/users/")
async def create_users(user: User):
    users.append(user)
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = user
    return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return {"user_id": users.pop(i)}
    return HTTPException(status_code=404, detail='Task not found')
