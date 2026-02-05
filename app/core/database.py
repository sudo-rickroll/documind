import redis.asyncio as redis
from app.core.config import settings
from typing import Optional

class RedisClient:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            # Not awaitable. Use ping() to test connection or get key to lazy load
            cls._instance = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                decode_responses=True
            )
        return cls._instance
    
    @classmethod
    async def close(cls):
        if cls._instance:
            await cls._instance.close()
            cls._instance = None

