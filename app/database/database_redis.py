import os
import redis.asyncio as redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

async def get_redis():
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_response=True)
    client = redis.Redis(connection_pool=pool)

    try:
        yield client
    finally:
        await client.close()