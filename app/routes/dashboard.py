from fastapi import APIRouter, HTTPException
from app.redis_client import get_redis_connection
from app.services.dashboard_service import get_cached_dashboard_data

router = APIRouter()
r = get_redis_connection()

@router.get("/")
def dashboard():
    if not r:
        raise HTTPException(status_code=500, detail="Redis not connected")
    return get_cached_dashboard_data(r)

@router.get("/ping-redis")
def ping_redis():
    try:
        return {"redis_ping": r.ping()}
    except Exception as e:
        return {"error": str(e)}
