from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db_postgres import Base

# class NewUser(Base):
#     __tablename__ = 'new_user'

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, nullable=False)
#     user_name = Column(String, unique=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     first_name = Column(String)
#     last_name = Column(String)
#     is_active = Column(Boolean, default=True)
#     role = Column(String)

#     todos = relationship("NewToDo", back_populates="owner")


