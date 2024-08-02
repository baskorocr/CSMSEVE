# manager/controllers/status.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": "OK"}


@router.get("/test")
async def get_test():
    return {"test": "OK"}

