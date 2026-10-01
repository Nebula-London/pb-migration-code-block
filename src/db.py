from sqlalchemy import create_engine

DATABASE_URL = "postgresql://admin:admin@localhost:5432/library"

engine = create_engine(DATABASE_URL)
