from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.crud_user_api import create_user, get_user, get_users, update_user, delete_user
from app.models.m_user_api import User
from app.schemas.s_user_api import UserCreate, UserUpdate, UserResponse, ErrorResponse
from app.database.db_user_api import SessionLocal
from typing import Optional

router = APIRouter(
    prefix="/user_api", 
    tags=["User API"],
    responses={
        404: {"description": "User Not Found"},
        400: {"description": "Bad Request"},
        409: {"description": "Conflict: User already exists"},
        500: {"description": "Internal Server Error"},
    },
    )

def get_db():
    """
    Dependency to get a new database session.
    Ensures proper session handling.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UserResponse], summary="Retrieve all users")
def read_users(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    """
    Retrieve a list of users from the database.

    - **Query Parameters**:
        - `skip` (int, default=0): Number of users to skip.
        - `limit` (int, default=100): Maximum number of users to return.
    - **Response**:
        - A list of user objects.
    """
    return get_users(db, skip, limit)

@router.get("/{user_id}", response_model=UserResponse, summary="Retrieve single user")
def read_user(user_id: int, db: Session=Depends(get_db)):
    """
    Retrieve a single user information from database

    - **Query Parameters**:
        - `user_id` (int): The user's ID.
    - **Response**:
        - The specific user information
    - **404 Error**:
        - If the user does not exist.
    """
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Can't find the user.")
    return db_user

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,  
    summary="Create a new user",
    responses={
        201: {"description": "User created successfully"},
        400: {"model": ErrorResponse, "description": "Bad Request"},
        404: {"model": ErrorResponse, "description": "User Not Found"},
        409: {"model": ErrorResponse, "description": "User already exists"},
        422: {"description": "Validation Error"},  # Auto-generated
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
)
def new_user(u_create: UserCreate, db: Session=Depends(get_db)):
    """
    Create a new user in the database.

    - **Request Body**:
        - `UserCreate` schema with user details.
    - **Response**:
        - The created user object.
    - **409 Error**:
        - If the user already exists (handled within `create_user` function).
    """
    return create_user(db, u_create)

@router.put("/{user_id}", response_model=UserResponse)
def change_user_info(user_id: int, update_info: UserUpdate, db: Session=Depends(get_db)):
    """
    Update an existing user's information.

    - **Path Parameter**:
        - `user_id` (int): Unique identifier of the user to update.
    - **Request Body**:
        - `UserUpdate` schema with updated user details.
    - **Response**:
        - The updated user object.
    """
    updated_user = update_user(db, user_id, update_info)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="Can't find the user.")
    return updated_user

@router.delete('/{user_id}', response_model=UserResponse)
def remove_user_info(user_id: int, db: Session=Depends(get_db)):
    """
    Delete a user from the database.

    - **Path Parameter**:
        - `user_id` (int): Unique identifier of the user to delete.
    - **Response**:
        - The deleted user object.
    """
    user_info = delete_user(db, user_id)
    if user_info is None:
        raise HTTPException(status_code=404, detail="Can't find the user.")
    return user_info

