from datetime import datetime
from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }