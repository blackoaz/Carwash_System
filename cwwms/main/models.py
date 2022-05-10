import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_tenants.models import TenantMixin, DomainMixin
  
    
class Client(TenantMixin):
    tenant_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    tenant_uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    
class Domain(DomainMixin):
    pass
