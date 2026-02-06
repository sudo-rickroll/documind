from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from app.core.config import settings
from app.api.v1.endpoints import documents
from app.core.database import RedisClient

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    print("Application running")
    redis = RedisClient.get_instance()
    try:
        await redis.ping()
        print("Redis connection established successfully")
    except Exception as e:
        print(f"Could not establish connection to redis: {e}")

    yield

    print("Terminating the app")
    await redis.close()
    print("Redis connection closed successfully")

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    openapi_url=f"{settings.API_CURRENT}/openapi.json"
    )

app.include_router(
    router=documents.router,
    prefix=f"{settings.API_CURRENT}/documents",
    tags=["documents"]
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Documind",
        "version": settings.API_CURRENT,
        "docs": "/docs"
    }
