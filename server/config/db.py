from sqlite3 import connect
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+pymysql://root:password@localhost:3306/fastapi')
POSTGRESQL_DATABASE_URL = "postgresql://postgres:password@localhost:5432/mtickets"
engine = create_engine(POSTGRESQL_DATABASE_URL)
meta = MetaData()
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()