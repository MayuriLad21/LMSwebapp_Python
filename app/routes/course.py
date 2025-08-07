from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.course import Course
from app.dependencies import get_db  # shared DB session

router = APIRouter()

@router.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    try:
        courses = db.query(Course).all()
        # Format data for React (if needed)
        result = [
            {
                "id": c.id,
                "title": c.title,
                "description": c.description,
                "instructor": c.instructor,
                "duration": c.duration
            } for c in courses
        ]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
