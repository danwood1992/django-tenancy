from typing import List, Optional
from django.db import models, transaction
import uuid
from .tenant import Tenant
import logging
logger = logging.getLogger(__name__)
class Domain(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    domain_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='domains')
    created = models.DateTimeField(auto_now_add=True)
    primary = models.BooleanField(default=False)       
    
    def save (self, *args, **kwargs):
        #if first domain set primary to true
       
        if not self.tenant.domains.filter(primary=True).exists():

            self.primary = True
            
       
        
        with transaction.atomic():
            # If this domain is marked as primary, unset other primary domains for this tenant
            if self.primary:
                Domain.objects.filter(tenant=self.tenant, primary=True).exclude(pk=self.pk).update(primary=False)
            
            super(Domain, self).save(*args, **kwargs)
        
        
    def __str__(self):
        return self.domain_name
    