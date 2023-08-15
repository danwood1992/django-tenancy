from graphene_django import DjangoObjectType
from .models import StaffSeat


class StaffType(DjangoObjectType):
    class Meta:
        model = StaffSeat
        fields = "__all__"