from app.database.session import engine
from app.models.user import User  # ensure model is imported
from app.database.base_class import Base

def init_db():
    Base.metadata.create_all(bind=engine)