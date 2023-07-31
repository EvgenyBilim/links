from fastapi import APIRouter
from app.api import links


router = APIRouter()

router.include_router(links.router, tags=["Links"], prefix="/links")
