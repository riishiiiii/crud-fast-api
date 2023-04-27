from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:1234@localhost:5433/crud"

engine = create_engine(DATABASE_URL)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()
