import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from src.models import *


app = FastAPI(title="sample project")

notes_db = [Note(id=1, created_by="admin", content="test"),
            Note(id=2, created_by="admin", content="test", tags=["kdfmkef"])]


@app.get("/")
async def root():
    # uvicorn main:app --reload --port 8080
    # http://127.0.0.1:8000/docs
    return FileResponse("src/index.html")


@app.get("/notes")
def get_all_notes(skip: int = 0, limit: int = 10) -> dict:
    data = {
        "items": notes_db[skip: skip + limit],
        "total": len(notes_db)
    }
    return data


@app.get("/notes/{note_id}")
def get_note(note_id: int) -> dict | Note:
    found = [x for x in notes_db if x.id == note_id]
    if len(found) == 0:
        return {"error": f"{note_id = } not found"}
    else:
        return found[0]


@app.post("/notes")
async def create_note(note: NoteCreate) -> Note:
    data = {
        "id": max(x.id for x in notes_db) + 1,
        "created_by": "default",
        "content": note.content,
        "tags": note.tags
    }
    new_note = Note(**data)
    notes_db.append(new_note)
    return new_note


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)
