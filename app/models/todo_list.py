from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db_postgres import Base

class NewToDo(Base):
    __tablename__ = 'new_to_do_lst'

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    description = Column(String, index=True)
    task_status = Column(String, default="ToDo")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("NewUser", back_populates="todos")
