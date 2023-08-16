import graphene
from graphene import ObjectType
from .models.domain import Domain
from .types import DomainType, RealmtType
from apps.core.seats.models import StaffSeat
from apps.core.seats.types import StaffType
from apps.admin.tenancy.models.tenant import Tenant
from django.db import transaction
import datetime
from django.conf import settings
from django.contrib.auth.models import User

class CreateRealm(graphene.Mutation):
    realm = graphene.Field(RealmtType)
    domain = graphene.Field(DomainType)
    success = graphene.Boolean()
    
    class Arguments:
        
        realm_name = graphene.String(required=True)
        email = graphene.String(required=True)
        newrealmpassword = graphene.String(required=True)

    @transaction.atomic
    def mutate(self, info, realm_name, email, newrealmpassword):
        # First, get the objects needed for ForeignKeys

        current_realms = Tenant.objects.all()
        current_domains = Domain.objects.all()
        trial_end = datetime.date.today() + datetime.timedelta(days=settings.TRIAL_LENGTH)
        management_domain = settings.MANAGEMENT_DOMAIN
        # Create the realm
        if realm_name in [realm.name for realm in current_realms] or f'{realm_name}.{management_domain}' in [domain.domain_name for domain in current_domains]:
            raise Exception('Realm name already exists')
        new_realm = Tenant(name=realm_name,paid_until=trial_end)
        new_realm.save()
        domain = Domain(domain_name=f'{realm_name}.{management_domain}', tenant=new_realm)
        domain.save()
        
        # Assign email a staffseast in the new realm
        #get or create user with that email address
        user = User.objects.create(username=email)
        user.set_password(newrealmpassword)
        user.save()
 
        new_staff = StaffSeat(user=user, tenant=new_realm,tenant_management_level=5)
        new_staff.save()

        return CreateRealm(success=True, realm=new_realm, domain=domain)
   

class Mutation(ObjectType):
    create_realm = CreateRealm.Field()

