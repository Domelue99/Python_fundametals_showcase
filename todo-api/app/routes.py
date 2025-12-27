from fastapi import APIRouter
from app.schemes import ToDoCreate
router = APIRouter()

@router.get("/health")
def health():
    return{"status" : "bien"}


todos = []

@router.post("/todos", status_code=201)
def create_todo(todo: ToDoCreate):
    todos.append(todo)
    return todo
