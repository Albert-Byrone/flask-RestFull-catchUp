from api import app
from .config.database_config import Base, engine


Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
  app.run(debug=True)