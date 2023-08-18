from datetime import date

def tenant_file_upload_path(instance, filename):
    if instance.management_tenant:
        return f"management-tenant-files/{instance.name}/{filename}"
    return f"tenant-files/{instance.id}/{filename}"

def personal_upload_path(instance, filename):
    return f"tenant-files/{instance.realm.name}/{instance.get_personal_file_path}/profile_pictures/{filename}"

              
            
   



