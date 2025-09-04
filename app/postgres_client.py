from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your Supabase connection string
DATABASE_URL = "postgresql://postgres:postgres%40123@db.wzupkbanrhcvznksmjoa.supabase.co:5432/postgres"
# DATABASE_URL = "postgresql://postgres:postgres%40123@localhost:5432/postgres"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()