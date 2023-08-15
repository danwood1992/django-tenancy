from django.apps import AppConfig


class TenantManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admin.tenancy'
    
    def ready(self):
        import apps.admin.tenancy.signals
