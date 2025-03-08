# FastAPI learning
This is the place to learn everything I need to know for FastAPI

## :hammer_and_pick: Technologies Used
- **Language**: Python
- **Backend Framework**: FastAPI
- **Testing Framework**: Pytest
- **Containerization**: Docker
- **Database**: PostgreSQL, MongoDB

## :gear: Prerequisites
- Python 3.8+
- [Docker](https://docs.docker.com/engine/install/) 

## :closed_book: Project Directory Structure
```bash
backend_web/
├─ app/
│ ├─ __init__.py          # (optional) marks this directory as a Python package
│ ├─ main.py              # Entry point for the FastAPI application
│ ├─ database_postgres.py # PostgreSQL connection using SQLAlchemy
│ ├─ database_mongo.py    # MongoDB connection using Motor
│ ├─ curd/                # All the CRUD for different API fun
│ │  ├─ todo.py           
│ │  └─ health.py        
│ ├─ models/              # All the models for different API fun
│ │  ├─ todo.py           
│ │  └─ health.py         
│ ├─ routes/              # All the API routes for different API fun
│ │  ├─ todo.py           
│ │  └─ health.py         
│ ├─ schemas/             # All the schemas for different API fun
│ │  ├─ todo.py           
│ │  └─ health.py         
│ ├─ tests/               # All the test cases  for different API fun
│ │  ├─ todo.py           
│ └─ └─ health.py         
├─ pyproject.toml         # Poetry configuration file (includes dependencies, scripts, etc.)
├─ poetry.lock            # Generated lock file for reproducible installs
├─ Dockerfile             # Dockerfile for containerizing your FastAPI app
├─ docker-compose.yml     # Docker Compose file to orchestrate FastAPI, PostgreSQL, and MongoDB
└─ README.md              # (Optional) Project overview and setup instructions
```

## :wrench: Setting up
* Clone the Repo
* Build the containers using the following command
    ```bash
    docker compose up
    ```

* Access to FastAPI env
    ```bash
    docker ps # Check the container name for the FastAPI
    docker exec -it <container_id or name> /bin/bash
    ```
