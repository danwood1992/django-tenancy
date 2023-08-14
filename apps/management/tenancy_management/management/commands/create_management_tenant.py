from typing import Union
from django.core.management.base import BaseCommand
from apps.management.tenancy_management.models.domain import Domain
from apps.management.tenancy_management.models.tenant import Tenant
from apps.tenant.seats.models import StaffSeat
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates the management tenant and admin user.'

    def handle(self, *args, **options) -> Union[int, str]:
        if Tenant.objects.filter(management_tenant=True).exists():
            self.stdout.write(self.style.ERROR("Management tenant already exists."))
            return
        # Prompt for inputs
        full_domain = settings.MANAGEMENT_DOMAIN
        name = input("Enter the name of the management tenant: ")
        admin_email = input("Enter the admin email of the tenant: ")
        password = input("Enter the password of the tenant: ")

        if not name or not admin_email or not full_domain:
            self.stdout.write(self.style.ERROR("Please provide all the required information."))
            return

        # Create the management tenant and admin user
        try:
            tenant = Tenant.objects.create(name=name, management_tenant=True)
            
            user = User.objects.create_user(username=admin_email, email=admin_email, password=password, is_staff=True, is_superuser=True)

            Domain.objects.create(tenant=tenant, domain_name=full_domain)

            return f'Successfully created management tenant {name} with domain {full_domain} and admin email {admin_email}!'
        except Exception as e:
            return str(e)

   
        