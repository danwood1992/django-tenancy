import graphene
from .models import StaffSeat
from .types import StaffType

class Query(graphene.ObjectType):
    
    staff = graphene.List(StaffType)
    
    
    def resolve_staff(root, info):
        
        assignments = StaffSeat.objects.all()
        
   