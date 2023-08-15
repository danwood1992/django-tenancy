from typing import Union
from django.core.management.base import BaseCommand
from apps.management.tenancy_management.models.domain import Domain
from apps.management.tenancy_management.models.tenant import Tenant
from apps.core.seats.models import StaffSeat
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = 'Deletes the management tenant and admin user.'

    def handle(self, *args, **options) -> Union[int, str]:
        if not Tenant.objects.filter(management_tenant=True).exists():
            self.stdout.write(self.style.ERROR("Management tenant doesnt exist."))
            return
        
        print("Are you sure you want to delete the management tenant? (y/n)")
        choice = input().lower()
        if choice != 'y':
            return "Aborting deletion of management tenant"
        
        try:
            management_tenant = Tenant.objects.get(management_tenant=True)
            #deletes superusers
            superusers = User.objects.filter(is_superuser=True)
            for superuser in superusers:
                superuser.delete()
            management_tenant.delete()
            print("Tenant list after deletion")
            for tenant in Tenant.objects.all():
                print(tenant.name)
           
            return f'Successfully deleted management tenant and domain'
        except Exception as e:
            return str(e)

   
        