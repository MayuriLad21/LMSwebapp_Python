from sqlalchemy import Column, Integer, String
from app.pgdb import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    instructor = Column(String)
    duration = Column(String)
