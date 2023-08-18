from graphene_django import DjangoObjectType
from .models import Realm, RealmAccess, RealmProfile


class RealmtType(DjangoObjectType):
    class Meta:
        model = Realm
        fields = "__all__"

class RealmAccessType(DjangoObjectType):
    class Meta:
        model = RealmAccess
        fields = "__all__"
class RealmProfileType(DjangoObjectType):
    class Meta:
        model = RealmProfile
        fields = "__all__"