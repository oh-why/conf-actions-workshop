from pydantic import BaseModel


class Note(BaseModel):
    id: int
    created_by: str
    content: str | None = None
    tags: list[str] = []


class NoteCreate(BaseModel):
    content: str | None = ""
    tags: list[str] = []


class User(BaseModel):
    id: int
    name: str
