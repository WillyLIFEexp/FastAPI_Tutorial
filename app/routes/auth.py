from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserResponse, Token
from app.database.db_postgres import SessionLocal
from app.crud import create_new_user, authenticate_user, create_access_token, decode_access_token, SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta
from jose import JWTError, jwt


router = APIRouter(prefix='/auth', tags=['auth'])

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
form_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]
token_dependency = Annotated[str, Depends(oauth2_bearer)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user: UserCreate):
    new_user = create_new_user(db, user)
    return new_user

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: form_dependency,
                                 db: db_dependency):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')

    access_token = create_access_token(user.user_name, user.id, user.role, timedelta(minutes=15))
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: token_dependency):
    try:
        payload = decode_access_token(token)
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        role: str = payload.get('role')

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return {'username': username, "user_id": user_id, "role": role}

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

