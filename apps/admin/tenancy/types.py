from graphene_django import DjangoObjectType
from .models.tenant import Tenant
from .models.domain import Domain

class RealmtType(DjangoObjectType):
    class Meta:
        model = Tenant
        fields = "__all__"
class DomainType(DjangoObjectType):
    class Meta:
        model = Domain
        fields = "__all__"
