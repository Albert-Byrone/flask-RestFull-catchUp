import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

username = os.environ['DATABASE_USERNAME']
database = os.environ['DATABASE_NAME']
host = os.environ['DATABASE_HOST']
password = os.environ['DATABASE_PASSWORD']
database_type = os.environ['DATABASE_TYPE']
port = os.environ.get('DATABASE_PORT', 5432)

db_url = f"{database_type}:{username}:{password}@{host}:{port}/{database}"


engine = create_engine(db_url)
print("Created emgine", engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()