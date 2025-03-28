from sqlalchemy import Column, Integer, String, DateTime
from app.database.database_postgres import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now())