from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title : str
    completed : bool = False

class TodoResponse(BaseModel):
    id : int
    title : str
    completed : bool