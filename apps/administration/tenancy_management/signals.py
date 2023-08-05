from django.db.models.signals import post_save
from .models.domain import Domain
from django.dispatch import receiver
import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=Domain)
def set_primary_domain(sender, instance, **kwargs):
    logger.info("Setting primary domain for tenant: %s", instance.tenant.name)
    # If no primary domain exists for the tenant, set the current domain as primary
    if not instance.tenant.domains.filter(primary=True).exists():
        instance.primary = True
        instance.save()