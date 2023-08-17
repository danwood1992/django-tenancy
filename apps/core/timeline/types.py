from graphene_django import DjangoObjectType
from .models import Post, Comment, Like

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"
class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"
class LikeType(DjangoObjectType):
    class Meta:
        model = Like
        fields = "__all__"
