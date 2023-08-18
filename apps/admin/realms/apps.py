from django.apps import AppConfig


class TenantManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admin.realms'
    
    # def ready(self):
    #     import apps.admin.realms.signals
