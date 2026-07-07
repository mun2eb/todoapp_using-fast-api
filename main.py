from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todos=[]

class todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo :todo):
   todos.append(todo)
   return {"message":"todo created","data":todo}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def view_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
        
    return{"no todo found"}
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int , updated_todo:todo):
    for index,todo in enumerate(todos):
        if todo_id==todo.id:
            todos[index] = updated_todo
            return {"message":"data updated",
                    "data":updated_todo} 
    return{"no todo found"}
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if  todo.id == todo_id:
            todos.pop(index)
            return {"message":"todo deleted"}
    return{"no todo found"}



