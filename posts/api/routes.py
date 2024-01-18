from api import db, api
from flask_restful import Resource, reqparse
from .models import Post
from .serializer import response_serializer

from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('description')
parser.add_argument('created_at')
parser.add_argument('reviewed')


class PostList(Resource):
  def get(self):
    posts = Post.query.all()
    response = response_serializer(posts)
    return response, 200


  def post(self):
    data = parser.parse_args()
    print("=====", data)
    date = datetime.strptime(data['created_at'], "%d/%m/%y") # DateTime Object
    data['created_at'] = date


    if data['reviewed'] == "True":
      data['reviewed']=True
    else:
      data['reviewed']=False

    new_data = Post(**data)
    print("===new__value==", new_data)
    db.session.add(new_data)
    db.session.commit()
    data['created_at'] = str(date)
    return data, 201


class PostData(Resource):
  def get(self, id):
    post = Post.query.get(int(id))

    if post:
      response = response_serializer([post])
      return response, 200
    else:
      return { "message": "Not found"}

  def put(self, id):
    data = parser.parse_args()
    print("=====", data)
    date = datetime.strptime(data['created_at'], "%d/%m/%y") # DateTime Object
    data['created_at'] = date
    if data['reviewed'] == "True":
      data['reviewed']=True
    else:
      data['reviewed']=False

    try:
      post = Post.query.get(int(id))
      if post:
        return self._update_data_(data,post)
      else:
        return { "message": "Post Not found"}
    except:
      return { "message": "Post Not found"}


  def _update_data_(self, data, post):
    post.title = data["title"]
    post.description = data["description"]
    post.created_at = data["created_at"]
    post.reviewed = data["reviewed"]

    db.session.add(post)
    db.session.commit()

    response = response_serializer([post])
    return response, 200


api.add_resource(PostList, "/posts")
api.add_resource(PostData, "/posts/<int:id>")


