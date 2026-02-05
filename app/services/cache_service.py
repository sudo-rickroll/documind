import json
from typing import Optional, Dict
from app.core.database import RedisClient
from app.core.config import settings

class CacheService:
    def __init__(self):
        self.redis = RedisClient.get_instance()

    async def get_document(self, doc_id: str) -> Optional[Dict]:
        data = await self.redis.get(f"doc: {doc_id}")
        return json.loads(data) if data else None
    
    async def set_document(self, doc_id: str, data: Dict) -> None:
        await self.redis.set(
            f"doc:{doc_id}",
            json.dumps(data),
            ex=settings.REDIS_TTL
            )
