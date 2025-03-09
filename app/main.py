from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.todo import router as todo_router
from app.routes.products import router as prod_router
from app.routes.r_user_api import router as user_router
from app.database.database_postgres import engine, Base

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
# app.include_router(todo_router)
# app.include_router(prod_router)
app.include_router(user_router)

@app.get('/')
def read_root():
    return {"message": "Hello World!!!"}
