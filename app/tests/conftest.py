import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database_postgres import SessionLocal, Base, engine

# Create a new database for testing purposes
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    # You can override the get_db dependency here to use a test database session
    def override_get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[app.get_db] = override_get_db
    with TestClient(app) as c:
        yield c

@pytest.fixture
def todo_payload():
    return {
        "id": 1,
        "title": "Test Todo",
        "description": "Test description"
    }