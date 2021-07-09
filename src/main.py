import os
from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Depends
from mangum import Mangum

from src.serializers import ToDoInputSerializer, ToDoSerializer
from src.dbstate import StateDB, get_db


stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"
app = FastAPI(title='Databaseless ToDo API', openapi_prefix=openapi_prefix)


@app.get('/todos', response_model=List[ToDoSerializer])
def list_todo_api(db: StateDB = Depends(get_db)):
    return db.get_todos()


@app.post('/todos', response_model=ToDoSerializer)
def add_todo_api(todo: ToDoInputSerializer, db: StateDB = Depends(get_db)):
    todo = db.add_todo(todo.name)
    return todo


@app.get('/todos/{id}',  response_model=ToDoSerializer)
def retrieve_todo_api(id: str, db: StateDB = Depends(get_db)):
    todo = db.get_todo(id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='ToDo Not Found'
        )
    return todo


@app.post('/todos/{id}/finish', response_model=ToDoSerializer)
def finish_todo_api(id: str, db: StateDB = Depends(get_db)):
    todo = db.set_finish(id)
    if todo:
        return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='ToDo Not Found'
    )


handler = Mangum(app)
