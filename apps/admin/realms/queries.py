import graphene

from .models import Realm

from .types import RealmType, RealmAccessType, RealmAccountType, UserType

class UserQuery(graphene.ObjectType):
    viewer = graphene.Field(UserType)

    def resolve_viewer(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return user

class RealmQuery(graphene.ObjectType):
    realms = graphene.List(RealmType)

    def resolve_all_realms(self, info, **kwargs):
        return RealmType.objects.all()

class Query(UserQuery, RealmQuery, graphene.ObjectType):
    pass