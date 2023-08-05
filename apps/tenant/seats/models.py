from django.db import models
from django.db.models import Index
from apps.administration.tenancy_management.models.tenant import Tenant
from apps.administration.tenancy_management.utils import seat_personal_upload_path
from django.contrib.auth import get_user_model
import uuid
import logging
logger = logging.getLogger(__name__)

class AbstractSeat(models.Model):
    """
    Essential attributes of a seat.
    Abstract base class for all seat-related models.
    Intended to be subclassed by specific seat types.
    A seat is given to a tenant user to access the system.
    
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="%(class)s_related",
        null=True,
        blank=True,
    )
    tenancy_owner = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    can_pay_tenancy = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    @property
    def get_personal_file_path(self):
        try:
            return self.id
        except:
            logger.error("No id for tenant: %s", self.user)
            return None
    
    class Meta:
        abstract = True

class StaffSeat(AbstractSeat):
    class TenantManagementLevel(models.IntegerChoices):
        ONE = 1, '1'
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'

    tenant_management_level = models.IntegerField(choices=TenantManagementLevel.choices)
    profile_picture = models.ImageField(upload_to=seat_personal_upload_path, null=True, blank=True)
    class Meta:
        indexes = [
            Index(fields=['tenant'])
        ]

    def __str__(self) -> str:
        return getattr(self.user, 'username', 'No User')

    