from fastapi.testclient import TestClient
from app.main import app

import logging

client = TestClient(app)

def test_read_todos():
    response = client.get("/todos/")
    # Check if the endpoint returns status code 200
    assert response.status_code == 200
    # Verify that the response data is a list (even if empty)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_create_todo(todo_payload):
    response = client.post("/todos/", json=todo_payload)
    # Check if the POST request is successful
    assert response.status_code == 200
    data = response.json()
    # Verify that the response contains the same title and description
    assert data["title"] == todo_payload["title"]
    assert data["description"] == todo_payload["description"]
    # Optionally, check that an ID was created
    assert "id" in data
    assert data["id"] == 1

def test_read_todo_not_found():
    # Assuming a todo with id 9999 does not exist
    response = client.get("/todos/9999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Todo not found"

def test_select_todo_item(todo_payload):
    id = todo_payload["id"]
    response = client.get(f"/todos/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == todo_payload["title"]
    assert data["description"] == todo_payload["description"]
    assert "id" in data
    assert data["id"] == todo_payload["id"]

def test_update_todo_item(todo_payload):
    id = todo_payload["id"]
    update_value = {'title': 'Updated value'}
    response = client.put(f"/todos/{id}", json=update_value)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_value["title"]

def test_delete_todo_item(todo_payload):
    id = todo_payload["id"]
    response = client.delete(f"/todos/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == todo_payload["id"]


    
