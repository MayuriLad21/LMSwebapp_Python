from app.models.student import Student
from sqlalchemy.orm import Session

def get_all_courses(db: Session):
    return db.query(Student).all()