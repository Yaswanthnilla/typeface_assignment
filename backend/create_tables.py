from sqlalchemy import create_engine
from backend.models import Base, DATABASE_URL

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
