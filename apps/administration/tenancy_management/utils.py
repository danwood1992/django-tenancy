from datetime import date
def tenant_file_upload_path(instance, filename):
    if instance.management_tenant:
        return f"management-tenant-files/{instance.name}/{filename}"
    return f"tenant-files/{instance.get_primary_domain}/{filename}"

def seat_personal_upload_path(instance, filename):
    return f"tenant-files/{instance.tenant.name}/{instance.get_personal_file_path}/profile_pictures/{filename}"



def get_host_from_request(request):
    """
    Returns the host from the request object.
    """
    host = request.get_host().split(':')[0]
    
    if host.startswith("www."):
        return host[4:]
    
    return host

def tenant_subscription_check(tenant):
    """
    This function checks if the tenant has a subscription and if the subscription is active
    """
    print (f"tenant in memory from domain object - {tenant}")
    print (f"tenant active status - {tenant.is_active}")
    print (f"tenant paid until - {tenant.paid_until}")
    if not tenant.is_active or tenant.paid_until and tenant.paid_until < date.today():
        return False
    return True
              
            
   



