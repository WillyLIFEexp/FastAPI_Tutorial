from sqlalchemy.orm import Session
from app.models import NewToDo
from app.schemas import ToDoUpdate, ToDoCreate
from datetime import datetime

def get_all_todos(db: Session, skip: int=0, limit: int=100):
    """Getting all to do tasks from database"""
    return db.query(NewToDo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    """Getting the task base on the id"""
    return db.query(NewToDo).filter(NewToDo.id == todo_id).first()

def create_todo(db: Session, todo: ToDoCreate):
    """Adding new task"""
    db_todo = NewToDo(**todo.model_dump())

    db.add(db_todo)
    db.commit()

def update_todo(db: Session, todo_id: int, todo: ToDoUpdate):
    """Update task with new information"""
    todo_data = get_todo(db, todo_id)

    todo_data.task_name = todo.task_name if todo.task_name else todo_data.task_name
    todo_data.description = todo.description if todo.description else todo_data.description
    todo_data.task_status = todo.task_status if todo.task_status else todo_data.task_status
    todo_data.updated_at = datetime.now()

    db.add(todo_data)
    db.commit()

def delete_todo(db: Session, todo_id: int):
    """Delete task """
    todo_data = get_todo(db, todo_id)

    db.delete()
    db.commit()
    







