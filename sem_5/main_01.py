'''Задание №1
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.'''

from fastapi import FastAPI, Request, HTTPException
from typing import Optional
from pydantic import BaseModel
import logging

# from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
# templates = Jinja2Templates(directory="sem_5/templates")



class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = None

task_1 = Task(id=1, title='string 1', description='Description for task 1', status='New')
task_2 = Task(id=2, title='string 2', description='Description for task 2', status='InProgress')

tasks = [task_1, task_2]
@app.get("/tasks/")
async def read_tasks():
    global tasks
    logger.info(f'Обработан запрос для tasks')
    return {"tasks": tasks}

@app.post("/tasks/")
async def create_tasks(task: Task):
    tasks.append(task)
    logger.info(f'Обработан POST запрос для создания задачи')
    return tasks

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
    logger.info(f'Обработан PUT запрос для task id {task}.')
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            return {"item_id": tasks.pop(i)}
    return HTTPException(status_code=404, detail='Task not found')