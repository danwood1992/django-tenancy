import graphene
from .types import PostType

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
 
    def resolve_all_posts(self, info, **kwargs):
        return PostType.objects.all()
    