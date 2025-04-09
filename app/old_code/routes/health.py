from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text  # Import text
from app.database.database_postgres import SessionLocal
from app.database.database_mongo import db as mongo_db

router = APIRouter(prefix='/todos', tags=['database'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/health/postgres")
def health_postgres(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "OK", "database": "PostgreSQL working"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PostgreSQL connection error: {e}")

@router.get("/health/mongo")
async def health_mongo(db):
    try:
        collections = await mongo_db.list_collection_names()
        return {"Status": "OK", "mongo_collections": collections}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PostgreSQL connection error: {e}")
