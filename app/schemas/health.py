from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str
    environment: str


class ReadinessResponse(BaseModel):
    status: str
    checks: dict[str, str]


class VersionResponse(BaseModel):
    service: str
    version: str
    environment: str
