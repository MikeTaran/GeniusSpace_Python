import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
load_dotenv()
# подключение базы данных PostgreSQL
SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRESQL_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = engine.connect()
print(conn.get_isolation_level())
#
