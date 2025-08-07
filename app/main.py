from fastapi import FastAPI
from app.config import add_cors
from app.routes import dashboard,course,student

app = FastAPI()

# ...existing code...

@app.get("/")
def root():
    return {"message": "API is running!"}

add_cors(app)

# Register routes
# app.include_router(dashboard.router)
app.include_router(dashboard.router, prefix="/api/dashboard")
app.include_router(course.router, prefix="/api")
app.include_router(student.router, prefix="/api")