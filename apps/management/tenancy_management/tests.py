from django.test import TestCase
from datetime import datetime, timedelta
from .models.tenant import Tenant
from .models.domain import Domain

class TenantModelTest(TestCase):

    def setUp(self):
        self.tenant = Tenant.objects.create(
            is_active=True,
            paid_until=datetime.now() + timedelta(days=30),
            name='Test Tenant',
            management_tenant=False
        )

    def test_tenant_creation(self):
        self.assertIsInstance(self.tenant, Tenant)
        self.assertEqual(self.tenant.__str__(), 'Test Tenant')

class DomainModelTest(TestCase):

    def setUp(self):
        self.tenant = Tenant.objects.create(
            is_active=True,
            paid_until=datetime.now() + timedelta(days=30),
            name='Test Tenant',
            management_tenant=False
        )
        self.domain = Domain.objects.create(
            domain_name='www.test.com',
            tenant=self.tenant
        )

    def test_domain_creation(self):
        self.assertIsInstance(self.domain, Domain)
        self.assertEqual(self.domain.__str__(), 'www.test.com')

