from app.pgdb import SessionLocal
from app.models.course import Course

db = SessionLocal()

courses = [
    Course(title="Python Basics", description="Learn Python from scratch.", instructor="John Doe", duration="4 weeks"),
    Course(title="React Essentials", description="Intro to React.js.", instructor="Jane Smith", duration="3 weeks"),
    Course(title="ML 101", description="Intro to Machine Learning", instructor="Sam Lee", duration="6 weeks")
]

db.add_all(courses)
db.commit()
db.close()

print("Sample courses added.")
