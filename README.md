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
fastapi_project/
│── app/              # Main application directory
│   │── api/          # API routes (FastAPI routers)
│   │── core/         # Core settings and security
│   │── db/           # Database setup and interactions
│   │── models/       # SQLAlchemy models (database schema)
│   │── schemas/      # Pydantic schemas (request & response validation)
│   │── services/     # Business logic layer
│   │── dependencies/ # Dependency injection (e.g., database, auth)
│   │── main.py       # FastAPI app entry point
│── tests/            # Unit and integration tests
│── .env              # Environment variables
│── requirements.txt  # Project dependencies
│── Dockerfile        # Docker setup for deployment
│── README.md         # Project documentation

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
