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
FASTAPI_TUTORIAL/
├── app/
│   ├── api/                     # Routers grouped by domain (e.g., auth, user)
│   │   ├── deps.py              # Common dependencies (auth, role check)
│   │   ├── v1/
│   │   │   ├── routes_auth.py
│   │   │   ├── routes_users.py
│   ├── core/                    # Core settings, security, JWT utils
│   │   ├── config.py
│   │   ├── security.py
│   ├── crud/                    # Business logic (e.g., DB queries)
│   │   ├── user.py
│   ├── database/
│   │   ├── session.py
│   │   ├── init_db.py
│   ├── models/
│   │   ├── user.py
│   ├── schemas/
│   │   ├── token.py
│   │   ├── user.py
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── conftest.py
│   ├── main.py                  # FastAPI entrypoint
├── .env                         # Env file for secrets (used by python-dotenv)
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── README.md

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
