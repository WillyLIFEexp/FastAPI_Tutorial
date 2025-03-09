from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

DATABASE_URL = os.getenv("POSTGRES_URL")

# Connect to PostgreSQL database
engine = create_engine(DATABASE_URL)

# Creating DB session
# Autoflush is to prevent postgresql will auto push the changes to the database
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db # Passing the session to the API
    finally:
        db.close() # Close the connection after the request

# This is a most and also help enable ORM 
Base = declarative_base()