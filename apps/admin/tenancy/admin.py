from django.contrib import admin
from .models.tenant import Tenant
from .models.domain import Domain

admin.site.register(Tenant)
admin.site.register(Domain)

