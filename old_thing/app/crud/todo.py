from sqlalchemy.orm import Session
from app.models.todo import ToDo
from app.schemas import todo

def get_todos(db: Session, skip: int=0, limit: int=100):
    return db.query(ToDo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    return db.query(ToDo).filter(ToDo.id == todo_id).first()

def create_todo(db: Session, todo: todo.TodoCreate):
    db_todo = ToDo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: todo.TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None 
    if todo.title is not None:
        db_todo.title = todo.title
    if todo.description is not None:
        db_todo.description = todo.description
    if todo.completed is not None:
        db_todo.completed = todo.completed

    db.commit()
    db.refresh(db_todo)
    return db_todo
        
def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None
        
    db.delete(db_todo)
    db.commit()
    return db_todo

