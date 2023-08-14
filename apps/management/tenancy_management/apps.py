from django.apps import AppConfig


class TenantManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.management.tenancy_management'
    
    def ready(self):
        import apps.management.tenancy_management.signals
