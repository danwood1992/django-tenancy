from django.apps import AppConfig


class TenantManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.administration.tenancy_management'
    
    def ready(self):
        import apps.administration.tenancy_management.signals
