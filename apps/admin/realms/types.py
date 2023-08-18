from graphene_django import DjangoObjectType
from .models import Realm, RealmAccess, RealmAccount


class RealmType(DjangoObjectType):
    class Meta:
        model = Realm
        fields = "__all__"

class RealmAccessType(DjangoObjectType):
    class Meta:
        model = RealmAccess
        fields = "__all__"
class RealmAccountType(DjangoObjectType):
    class Meta:
        model = RealmAccount
        fields = "__all__"