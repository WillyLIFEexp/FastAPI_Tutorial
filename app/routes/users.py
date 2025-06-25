from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Annotated

from app.database.db_postgres import SessionLocal
from app.schemas import UserCreate, UserUpdate
from app.models import NewUser
from app.crud import verify_password, create_hash_passwrod
from .auth import get_current_user

router = APIRouter(prefix="/user", tags=["user"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/', status_code=200)
async def get_user(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return db.query(NewUser).filter(NewUser.id == user.get('id')).first()

@router.put('/password', status_code=204)
async def change_password(db: db_dependency, user: user_dependency, user_update_info: UserUpdate):
    user_model = db.query(NewUser).filter(NewUser.id == user.get('id')).first()
    if verify_password(user_update_info.password, user_model.hashed_password):
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    user_model.hashed_password = create_hash_passwrod(user_update_info.password)
    db.add(user_model)
    db.commit()

