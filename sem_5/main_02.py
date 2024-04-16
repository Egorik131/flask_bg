'''Задание №2
Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.'''

from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: str


movie_1 = Movie(id=1, title='Taxi', description='Description for task 1', genre='humor')
movie_2 = Movie(id=2, title='Matrix', description='Description for task 2', genre='fantast')

movies = [movie_1, movie_2]

@app.get("/movies/")
async def get_movies():
    global movies
    return movies
@app.get("/movies/{genre}")
async def get_movies_genre(genre: str):
    global movies
    list_movies = []
    for i in range(len(movies)):
        if movies[i].genre == genre:
            list_movies.append(movies[i])
    return list_movies

@app.post("/movies/")
async def create_movies(movie: Movie):
    movies.append(movie)
    return movie

@app.put("/movies/{movie_id}")
async def update_task(movie_id: int, movie: Movie):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            movies[i] = movie
    return movie

@app.delete("/movies/{movie_id}")
async def delete_task(movie_id: int):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            return {"item_id": movies.pop(i)}
    return HTTPException(status_code=404, detail='Task not found')
