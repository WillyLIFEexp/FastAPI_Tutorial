from fastapi import FastAPI
from app.database.db_postgres import engine, Base
from app.routes import todo_router

app = FastAPI(
    title="My FastAPI Tutorial",
    description="A place for me to practice my API.",
    version="1.0.0",
    contact={
        "name": "William",
        "email": "nevergiveupop02@gmail.com",
    },)

# Create all database tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# app.include_router(health_router)
app.include_router(todo_router)
# app.include_router(prod_router)
# app.include_router(user_router)

@app.get('/')
def read_root():
    return {"message": "Hello World!!!"}
