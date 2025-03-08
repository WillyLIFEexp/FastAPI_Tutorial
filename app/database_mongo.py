import os
from motor.motor_asyncio import AsyncIOMotorClient

# Get the MongoDB URL from environment variables; fallback to a local default.
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Create an asynchronous MongoDB client
client = AsyncIOMotorClient(MONGO_URL)

# Define your database (here, named "fastapi_db")
db = client.productdb
