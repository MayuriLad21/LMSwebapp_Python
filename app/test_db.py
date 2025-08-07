from app.postgres_client import engine

try:
    # Try to connect
    conn = engine.connect()
    print("✅ Connected to Supabase successfully")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
