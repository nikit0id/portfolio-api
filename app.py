"""Small task API shared by the deployment labs."""
from contextlib import asynccontextmanager
from typing import Annotated

import psycopg
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from psycopg.rows import dict_row
from pydantic import BaseModel, Field, StringConstraints


def connect():
    # libpq reads PGHOST, PGDATABASE, PGUSER and PGPASSWORD.
    return psycopg.connect(connect_timeout=3, row_factory=dict_row)


@asynccontextmanager
async def lifespan(app):
    with connect() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                title text NOT NULL,
                done boolean NOT NULL DEFAULT false
            )
        """)
    yield


app = FastAPI(title="Portfolio Tasks", lifespan=lifespan)
Instrumentator().instrument(app).expose(app, include_in_schema=False)


class TaskInput(BaseModel):
    title: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=200)]


class Task(TaskInput):
    id: int
    done: bool


class StatusUpdate(BaseModel):
    done: bool = Field(strict=True)


@app.get("/health")
def health():
    try:
        with connect() as db:
            db.execute("SELECT 1")
    except psycopg.OperationalError as exc:
        raise HTTPException(503, "Database unavailable") from exc
    return {"status": "ok"}


@app.post("/tasks", status_code=201, response_model=Task)
def create_task(task: TaskInput):
    with connect() as db:
        return db.execute(
            "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title, done", (task.title,)
        ).fetchone()


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    with connect() as db:
        return db.execute("SELECT id, title, done FROM tasks ORDER BY id LIMIT 100").fetchall()


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, update: StatusUpdate):
    with connect() as db:
        task = db.execute(
            "UPDATE tasks SET done = %s WHERE id = %s RETURNING id, title, done",
            (update.done, task_id),
        ).fetchone()
    if task is None:
        raise HTTPException(404, "Task not found")
    return task
