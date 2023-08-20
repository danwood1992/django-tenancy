from django.db import models, transaction
from django.conf import settings
import uuid
from .utils import tenant_file_upload_path
import logging
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class Realm(models.Model):
  
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    on_trial = models.BooleanField(default=True)
    management_tenant = models.BooleanField(default=False)
    paid_until = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def is_tenant_active(self):
        return self.is_active

    def __str__(self) -> str:
        return self.name

class RealmAccess(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="realmaccess",null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_primary = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.user} | Access to {self.realm}'
    
class RealmAccount(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    realm_access = models.OneToOneField(RealmAccess, on_delete=models.CASCADE, related_name='realm_account')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    instagram_url = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.realm_access.user} - In {self.realm_access.realm.name}'