from .models import Post


def response_serializer(posts: Post):
  response = []
  for post in posts:
    post_dict = {
      "id":post.id,
      "title":post.title,
      "description":post.description,
      "created_at": str(post.created_at),
      "reviewed":post.reviewed,
    }
    response.append(post_dict)
  return response
