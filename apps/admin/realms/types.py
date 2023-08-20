from graphene_django import DjangoObjectType
from .models import Realm, RealmAccess, RealmAccount
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"

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