import os
from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime

from config.database_config import Base, engine, SessionLocal

db =SessionLocal()

print("session",db)
app = Flask(__name__)
Base.metadata.create_all(bind=engine)

class User(Base):

    __tablename__ ="users"

    id = Column(Integer, primary_key=True)
    name = Column(String(90))
    password = Column(String(90))
    admin = Column(Boolean)



class Post(Base):

  __tablename__ = "posts"

  id = Column(Integer, primary_key=True)
  title = Column(String(90))
  description = Column(String(90))
  reviewed = Column(Boolean, default=False, nullable=False)


  def __str__(self):
    return self.title


# from api import routes
@app.route('/user', methods=['POST'])
def create_user():
  # Get the data from the request
  data = request.json
  name = data["name"]
  password = data["password"]
  admin = data["admin"]

  # Create an instance of user from the received data
  new_user = User(name=name, password=password, admin=admin)
  # save the data
  db.add(new_user)
  db.commit()
  return  f' User {name} created successfully', 201




if __name__ == "__main__":
  app.run(debug=True)