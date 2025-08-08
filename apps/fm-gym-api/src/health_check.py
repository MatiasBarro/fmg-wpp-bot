

from fastapi import APIRouter

health_check_router = APIRouter(
    tags=["health"],
)

@health_check_router.get("/health")
def health():
    return {"status": "ok"}