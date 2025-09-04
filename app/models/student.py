from sqlalchemy import Column, Integer, String
from app.pgdb import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
