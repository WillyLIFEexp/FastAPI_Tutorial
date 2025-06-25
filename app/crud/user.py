from sqlalchemy.orm import Session
from app.models import NewUser
from app.schemas import UserCreate, UserUpdate
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from passlib.context import CryptContext
from jose import jwt, JWTError


SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(NewUser).filter(NewUser.user_name == username).first()
    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return None
    return user

def create_access_token(user_name: str, user_id: int, role: str, expires_time: timedelta):
    to_encode = {'sub': user_name, 'id': user_id, 'role': role}
    expire_date = datetime.now() + expires_time
    to_encode.update({'exp': expire_date})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(raw_password: str, hashed_password: str):
    return bcrypt_context.verify(raw_password, hashed_password)

def create_hash_passwrod(raw_password: str):
    return bcrypt_context.hash(raw_password)

def create_new_user(db: Session, user_data: UserCreate):
    """Adding new user"""
    db_todo = NewUser(
        email=user_data.email,
        user_name=user_data.user_name,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        role=user_data.role,
        hashed_password=bcrypt_context.hash(user_data.password),
        is_active=True
    )

    try:
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="User with this email or username already exists."
        )

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )