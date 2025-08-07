from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.student import Student
from app.dependencies import get_db  # shared DB session

router = APIRouter()

@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    try:
        students = db.query(Student).all()
        # Format data for React
        result = [
            {
                "id": s.id,
                "name": s.name,
                "email": s.email,
                "age": s.age,
                "gender": s.gender
            } for s in students
        ]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
