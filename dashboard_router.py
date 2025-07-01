from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
async def dashboard():
    return {"summary": "This is a dummy dashboard summary"}
