from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
async def health():
    """Check if the application is up."""
    return {"message": "ok"}
