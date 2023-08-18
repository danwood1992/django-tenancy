import datetime

import graphene
import graphql_jwt

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction
from graphene import ObjectType

from .models import Realm, RealmAccess, RealmProfile

from .types import RealmtType, RealmAccessType, RealmProfileType

class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    

class CreateRealm(graphene.Mutation):
    realm = graphene.Field(RealmtType)
    success = graphene.Boolean()
    
    class Arguments:
        
        realm_name = graphene.String(required=True)
        email = graphene.String(required=True)
        newrealmpassword = graphene.String(required=True)

    @transaction.atomic
    def mutate(self, info, realm_name, email, newrealmpassword):
        # First, get the objects needed for ForeignKeys
        current_realms = Realm.objects.all()
       
        trial_end = datetime.date.today() + datetime.timedelta(days=settings.TRIAL_LENGTH)
        management_domain = settings.MANAGEMENT_DOMAIN
        # Create the realm
        if realm_name in [realm.name for realm in current_realms]:
            raise Exception('Realm name already exists')
        new_realm = Realm(name=realm_name,paid_until=trial_end)
        new_realm.save()
        # Assign email a staffseast in the new realm
        #get or create user with that email address
        user = User.objects.create(username=email)
        user.set_password(newrealmpassword)
        user.save()
 
        realm_access = RealmAccess(user=user, realm=new_realm,tenant_management_level=5)
        realm_access.save()

        return CreateRealm(success=True, realm=new_realm)
   

class Mutation(AuthMutation,CreateRealm, graphene.ObjectType):
    pass
