from django.test import TestCase
from datetime import datetime, timedelta
from .models import Realm, RealmAccess, RealmProfile

class RealmModelTest(TestCase):

    def setUp(self):
        self.realm = Realm.objects.create(
            is_active=True,
            paid_until=datetime.now() + timedelta(days=30),
            name='Test Tenant',
            management_tenant=False
        )

    def test_tenant_creation(self):
        self.assertIsInstance(self.realm, Realm)
        self.assertEqual(self.realm.__str__(), 'Test Tenant')
