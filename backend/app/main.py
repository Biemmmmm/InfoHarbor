from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.config import settings


app = FastAPI(title="InfoHarbor API", version="0.1.0")


@app.on_event("startup")
async def on_startup() -> None:
    # Placeholder for startup logic such as DB connection checks
    settings.configure_database()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    # Placeholder for graceful shutdown logic
    settings.dispose_database()


app.include_router(api_router)
