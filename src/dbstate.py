from datetime import datetime
import uuid
from typing import List, Optional
from src.serializers import ToDoSerializer


class StateDB:
    todo: List = []

    def get_todos(self):
        return self.todo

    def add_todo(self, name):
        todo = ToDoSerializer(name=name)
        self.todo.append(todo)
        return todo

    def set_finish(self, id):
        todo = self.get_todo(id)
        if todo:
            todo.finished_at = datetime.utcnow()
            self.todo = list(map(lambda t: todo if t.id ==
                             todo.id else t, self.todo))
            return todo

    def get_todo(self, id) -> Optional[ToDoSerializer]:
        try:
            id = uuid.UUID(id)
            todo = list(filter(lambda x: x.id == id, self.todo))
            if todo:
                return todo[0]
        except:
            pass


db: StateDB = StateDB()


async def get_db() -> StateDB:
    return db
