from fastapi import FastAPI, HTTPException
import redis
import json

app = FastAPI()

try:
    REDIS_URL = "redis://default:4EcDK8lxlRoMQTVukUEJyjwcnA3NE2MH@redis-18767.c284.us-east1-2.gce.redns.redis-cloud.com:18767"
    r = redis.from_url(REDIS_URL, decode_responses=True)
    r.ping()
    print("✅ Connected to Redis Cloud via from_url()")
except Exception as e:
    r = None
    print("❌ Redis connection error:", e)

@app.get("/ping-redis")
def ping_redis():
    if r is None:
        return {"error": "Redis not connected."}
    try:
        return {"redis_ping": r.ping()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def get_dashboard_data():
    if r is None:
        raise HTTPException(status_code=500, detail="Redis not connected.")
    cache_key = "dashboard-data"
    cached_data = r.get(cache_key)
    if cached_data:
        return json.loads(cached_data)
    fresh_data = {
        "total_courses": 10,
        "total_students": 120,
        "active_users_today": 150
    }
    r.set(cache_key, json.dumps(fresh_data), ex=60)
    return fresh_data
