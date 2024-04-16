''' Создать API для управления списком задач.
Каждая задача должна содержать поля "название",
"описание" и "статус" (выполнена/не выполнена).
API должен позволять выполнять CRUD операции с
задачами.
 '''
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///my_database_603.db"  # создаем базу данных
database = databases.Database(DATABASE_URL)  # переменная из класса Database
metadata = sqlalchemy.MetaData()  # метаданные

app = FastAPI()

tasks = sqlalchemy.Table(
    'tasks',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(30)),
    sqlalchemy.Column('describe', sqlalchemy.String(50)),
    sqlalchemy.Column('status', sqlalchemy.Boolean()),
)


class TaskIn(BaseModel):
    name: str = Field(..., max_length=30)
    describe: str = Field(..., max_length=50)
    status: bool = Field(False)


class Task(TaskIn):  # наследуюем
    id: int


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(tasks_id: int):
    query = tasks.select().where(tasks.c.id == tasks_id)
    return await database.fetch_one(query)


@app.post("/tasks/", response_model=TaskIn)
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.model_dump())
    create_id = await database.execute(query)
    return await get_task(create_id)


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(tasks_id: int, task: TaskIn):
    query = tasks.update().where(tasks.c.id == tasks_id).values(**task.model_dump())
    await database.execute(query)
    return await get_task(tasks_id)


@app.delete("/tasks/{task_id}")
async def delite_task(tasks_id: int):
    query = tasks.delete().where(tasks.c.id == tasks_id)
    await database.execute(query)
    return {'msg': 'Delete'}
