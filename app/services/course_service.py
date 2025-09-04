from app.models.course import Course
from sqlalchemy.orm import Session

def get_all_courses(db: Session):
    return db.query(Course).all()