from app.pgdb import Base, engine
from app.models.course import Course

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
