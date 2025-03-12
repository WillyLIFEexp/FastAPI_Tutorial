from fastapi import HTTPException
from redis.asyncio import Redis

async def rate_limit(redis: Redis, user_ip: str, limit: int=5, window: int=60):
    """
    Rate limits reqeusts per user IP.

    - redis: Redis client
    - user_ip: IP address of the user making the request
    - limit: The total number of the request the user can make within the window
    - window: Time window in seconds
    """
    key = f"rate_limit:{user_ip}"
    count = await redis.get(key)

    if count and int(count) >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceed, Please try again later")

    await redis.incr(key)
    await redis.expire(key, window)

