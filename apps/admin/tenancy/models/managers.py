from threading import local
from ..models.tenant import Tenant
from ..models.domain import Domain



def tenant_file_upload_path(self, subfolder ,filename):
        return f"tenant_files/{self.name}/{subfolder}/{filename}"

def get_management_tenant():
    management_tenant = Tenant.objects.filter(management_tenant=True).first()
    
    return management_tenant

def get_management_tenant_domain():
    management_tenant_domain = Domain.objects.filter(tenant=get_management_tenant()).first()
    
    return management_tenant_domain

def get_active_tenants():
    active_tenants = Tenant.objects.filter(is_active=True)
    
    return active_tenants