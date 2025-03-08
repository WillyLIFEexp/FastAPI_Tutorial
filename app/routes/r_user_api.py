from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.crud_user_api import create_user, get_user, get_users, update_user, delete_user
from app.models.m_user_api import User
from app.schemas.s_user_api import UserCreate, UserUpdate, UserResponse
from app.database.db_user_api import SessionLocal

router = APIRouter(prefix="/userapi", tags=["User API"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UserResponse])
def read_users(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return get_users(db, skip, limit)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session=Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Can't find the user.")
    return db_user

@router.post("/", response_model=UserResponse)
def new_user(u_create: UserCreate, db: Session=Depends(get_db)):
    return create_user(db, u_create)

@router.put("/{user_id}", response_model=UserResponse)
def change_user_info(user_id: int, update_info: UserUpdate, db: Session=Depends(get_db)):
    updated_user = update_user(db, user_id, update_info)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="Can't find the user.")
    return updated_user

@router.delete('/{user_id}', response_model=UserResponse)
def remove_user_info(user_id: int, db: Session=Depends(get_db)):
    user_info = delete_user(db, user_id)
    if user_info is None:
        raise HTTPException(status_code=404, detail="Can't find the user.")
    return user_info

