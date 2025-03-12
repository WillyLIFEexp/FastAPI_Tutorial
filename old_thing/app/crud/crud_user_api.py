from sqlalchemy.orm import Session
from app.models.m_user_api import User
from app.schemas.s_user_api import UserCreate, UserUpdate, UserResponse

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id==user_id).first()

def get_users(db: Session, skip: int=0, limit: int=100):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, update_info: UserCreate):
    current_user = get_user(db, user_id)
    if not current_user:
        return None
    for key, value in update_info.dict(exclude_unset=True).items():
        setattr(current_user, key, value)

    db.commit()
    db.refresh(current_user)
    return current_user

def delete_user(db: Session, user_id):
    current_user = get_user(db, user_id)
    if not current_user:
        return None
    db.delete(current_user)
    db.commit()
    return current_user

