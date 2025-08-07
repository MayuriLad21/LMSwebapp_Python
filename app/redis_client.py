import redis

def get_redis_connection():
    try:
        r = redis.from_url(
            "redis://default:4EcDK8lxlRoMQTVukUEJyjwcnA3NE2MH@redis-18767.c284.us-east1-2.gce.redns.redis-cloud.com:18767",
            decode_responses=True
        )
        r.ping()
        print("✅ Redis connected")
        return r
    except Exception as e:
        print("❌ Redis connection failed:", e)
        return None
