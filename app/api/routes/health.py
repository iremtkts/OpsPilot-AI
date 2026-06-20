from fastapi import APIRouter

from app.dependencies import SettingsDependency
from app.schemas.health import HealthResponse, ReadinessResponse, VersionResponse

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
def health(settings: SettingsDependency) -> HealthResponse:
    """Report basic application liveness."""

    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.app_env,
    )


@router.get("/ready", response_model=ReadinessResponse)
def readiness() -> ReadinessResponse:
    """Report whether the application is ready to serve requests."""

    return ReadinessResponse(
        status="ready",
        checks={"application": "ok"},
    )


@router.get("/version", response_model=VersionResponse)
def version(settings: SettingsDependency) -> VersionResponse:
    """Report application version information."""

    return VersionResponse(
        service=settings.app_name,
        version=settings.app_version,
        environment=settings.app_env,
    )
