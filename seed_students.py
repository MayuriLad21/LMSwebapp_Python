from app.pgdb import SessionLocal
from app.models.student import Student

db = SessionLocal()

students = [
    Student(first_name="Alice", last_name="Johnson", email="alice@example.com", age=22, gender="female"),
    Student(first_name="Bob", last_name="Smith", email="bob@example.com", age=25, gender="male"),
    Student(first_name="Carol", last_name="Lee", email="carol@example.com", age=20, gender="female"),
]

db.add_all(students)
db.commit()
db.close()
print("Sample students added.")
