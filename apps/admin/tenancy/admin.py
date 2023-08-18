from django.contrib import admin
from .models import Realm, RealmAccess, RealmProfile

admin.site.register(Realm)
admin.site.register(RealmAccess)
admin.site.register(RealmProfile)
