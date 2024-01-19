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


# postgresql:albertbyrone:Albert254@localhost:5432/testtest
# postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase
# db_url = f"{database_type}:{username}:{password}@{host}:{port}/{database}"
db_url = f"{database_type}://{username}:{password}@{host}:{port}/{database}"


engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()