import graphene
from .models import Realm

from .types import RealmtType, DomainType

class Query(graphene.ObjectType):
    realms = graphene.List(RealmtType)

    def resolve_all_realms(self, info, **kwargs):
        return RealmtType.objects.all()
