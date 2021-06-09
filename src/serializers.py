from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class ToDoInputSerializer(BaseModel):
    name: str


class ToDoSerializer(ToDoInputSerializer):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    finished_at: datetime = None
