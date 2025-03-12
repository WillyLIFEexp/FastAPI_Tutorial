import uuid
from redis.asyncio import Redis
from app.schemas.s_redis_api import TaskCreateResponse, TaskListResponse, TaskStatusResponse

async def create_task(redis: Redis) -> TaskCreateResponse:
    task_id = str(uuid.uuid4())
    await redis.set(task_id, "pending")
    return TaskCreateResponse(task_id, status="pending")

async def get_task(redis: Redis, task_id: str) -> TaskStatusResponse:
    status = await redis.get(task_id)
    return TaskStatusResponse(task_id, status=status if status else None)

