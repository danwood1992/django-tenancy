from django.contrib import admin
from .models import Realm, RealmAccess, RealmAccount

admin.site.register(Realm)
admin.site.register(RealmAccess)
admin.site.register(RealmAccount)
