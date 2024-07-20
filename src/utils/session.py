import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg://app_user:app_password@0.0.0.0:5434/app_db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
