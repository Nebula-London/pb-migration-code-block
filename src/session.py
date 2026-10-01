from sqlalchemy.orm import sessionmaker
from db import engine

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Database connection generator."""
    db = session_local()
    try:
        yield db
    finally:
        db.close()
