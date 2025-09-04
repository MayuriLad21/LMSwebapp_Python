from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.student import Student
from app.dependencies import get_db  # shared DB session

router = APIRouter()

@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    try:
        students = db.query(Student).all()
        result = [
            {
                "id": s.id,
                "first_name": s.first_name,
                "last_name": s.last_name,
                "username": s.username,
                "email": s.email,
                "age": s.age,
                "gender": s.gender,
                "name": s.name  # uses the @property you defined in model
            } for s in students
        ]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
