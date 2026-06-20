from fastapi import FastAPI

from app.api.router import api_router
from app.config import get_settings
from app.logging_config import configure_logging


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()
    configure_logging(settings.log_level)

    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.app_debug,
    )
    application.include_router(api_router)
    return application


app = create_app()
