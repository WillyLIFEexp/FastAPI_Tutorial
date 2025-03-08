from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.todo import router as todo_router
from app.routes.products import router as prod_router
from app.database_postgres import engine, Base

app = FastAPI()

# Create all database tables (if they don't exist)
Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(todo_router)
app.include_router(prod_router)

@app.get('/')
def read_root():
    return {"message": "Hello World!!!"}
