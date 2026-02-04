from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/info")
def get_info():
    return {
        "app_name": settings.PROJECT_NAME,
        "default": settings.API_CURRENT
    }
def main():
    print("Hello from documind!")


if __name__ == "__main__":
    main()
