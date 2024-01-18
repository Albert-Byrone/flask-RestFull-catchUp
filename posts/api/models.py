from api import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90))
    password = db.Column(db.String(90))
    admin = db.Column(db.Boolean)





class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(90))
  description = db.Column(db.String(90))
  created_at  = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  reviewed = db.Column(db.Boolean, default=False, nullable=False)

  # user_id = db.Column(db.Integer) # Addd foreign key

  def __str__(self):
    return self.title