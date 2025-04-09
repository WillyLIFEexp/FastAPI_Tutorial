import os

from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base


# Get the PostgreSQL URL from the env variables;
POSTGRES_URL = os.getenv("POSTGRES_URL")

# Create the SQLAlchemy engine 
engine = create_engine(POSTGRES_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()