import graphene
from .models.tenant import Tenant
from .models.domain import Domain
from .types import RealmtType, DomainType

class Query(graphene.ObjectType):
    realms = graphene.List(RealmtType)
    domains = graphene.List(DomainType)
    

    def resolve_all_realms(self, info, **kwargs):
        return RealmtType.objects.all()
    
    def resolve_all_tasks(self, info, **kwargs):
        return DomainType.objects.all()
