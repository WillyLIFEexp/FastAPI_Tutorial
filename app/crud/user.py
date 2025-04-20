from sqlalchemy.orm import Session
from app.models import NewUser
from app.schemas import UserCreate, UserUpdate
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError


SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(NewUser).filter(NewUser.username == username).first()
    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return None
    return user

def create_access_token(user_name: str, user_id: int, role: str, expires_time: timedelta):
    to_encode = {'sub': user_name, 'id': user_id, 'role': role}
    expire_date = datetime.now() + expires_time
    to_encode.update({'exp': expire_date})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(user_name: str):
    expire_date = datetime.now() + timedelta(days=7)
    to_encode = {'sub': user_name, 'exp': expire_date}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

