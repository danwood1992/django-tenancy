import graphene
from .models import Realm

from .types import RealmType, RealmAccessType, RealmAccountType

class Query(graphene.ObjectType):
    realms = graphene.List(RealmType)

    def resolve_all_realms(self, info, **kwargs):
        return RealmType.objects.all()
