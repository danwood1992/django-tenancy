from django.db import models, transaction
from django.conf import settings
import uuid
from ..utils import tenant_file_upload_path
import logging
logger = logging.getLogger(__name__)

class BaseTenant(models.Model):
    """
    Essential attributes of a tenant.
    
    Change with caution.
    
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    on_trial = models.BooleanField(default=True)
    management_tenant = models.BooleanField(default=False)
    paid_until = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def is_tenant_active(self):
        return self.is_active
    
    @property
    def get_primary_domain(self):
        try:
            return self.domains.get(primary=True)
        except:
            logger.error("No primary domain found for tenant: %s", self.name)
            return None
    
    
    class Meta:
        abstract = True


# If you replace this make sure to replace throughout the project and ensure 
# that the new model inherits from BaseTenant 
class Tenant(BaseTenant):
    
    logo = models.ImageField(upload_to=tenant_file_upload_path, null=True, blank=True)# to test
        
    def __str__(self) -> str:
        return self.name