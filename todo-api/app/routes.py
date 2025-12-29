from fastapi import APIRouter
from app.schemes import ToDoCreate
from typing import List
from app.schemes import TodoResponse
from fastapi import HTTPException

router = APIRouter()

todos = []
todo_id_counter = 1

@router.post("/todos", response_model=TodoResponse)
def create_todo(todo: ToDoCreate):
    global todo_id_counter
    
    new_todo = {
        "id": todo_id_counter,
        "title" : todo.title,
        "completed" : todo.completed
    }
    todos.append(new_todo)
    todo_id_counter += 1
    return new_todo

@router.get("/todos/{todos_id}", response_model=TodoResponse)
def get_todos(todo_id:int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
        
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{todos_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(index)
            return {"message" : "Todo deleted"}
    
    raise HTTPException(status_code=404, detail="Todo not found")
