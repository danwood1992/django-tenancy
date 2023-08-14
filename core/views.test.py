from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.conf import settings
from apps.management.tenancy_management.models.domain import Domain
from .views import HomeView, ContactView, NotPaidView, IssuesView, SupportView


class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.tenant = Domain.objects.create(name='example.com', is_active=True, is_primary=True)
        self.tenant2 = Domain.objects.create(name='example2.com', is_active=True, is_primary=False)
        self.tenant3 = Domain.objects.create(name='example3.com', is_active=False, is_primary=False)
        self.tenant4 = Domain.objects.create(name='example4.com', is_active=True, is_primary=False)
        self.tenant5 = Domain.objects.create(name='example5.com', is_active=True, is_primary=False)
        self.tenant6 = Domain.objects.create(name='example6.com', is_active=True, is_primary=False)
        self.tenant7 = Domain.objects.create(name='example7.com', is_active=True, is_primary=False)
        self.tenant8 = Domain.objects.create(name='example8.com', is_active=True, is_primary=False)
        self.tenant9 = Domain.objects.create(name='example9.com', is_active=True, is_primary=False)
        self.tenant10 = Domain.objects.create(name='example10.com', is_active=True, is_primary=False)
        self.tenant11 = Domain.objects.create(name='example11.com', is_active=True, is_primary=False)
        self.tenant12 = Domain.objects.create(name='example12.com', is_active=True, is_primary=False)
        self.tenant13 = Domain.objects.create(name='example13.com', is_active=True, is_primary=False)
        self.tenant14 = Domain.objects.create(name='example14.com', is_active=True, is_primary=False)
        self.tenant15 = Domain.objects.create(name='example15.com', is_active=True, is_primary=False)
        self.tenant16 = Domain.objects.create(name='example16.com', is_active=True, is_primary=False)
        self.tenant17 = Domain.objects.create(name='example17.com', is_active=True, is_primary=False)
        self.tenant18 = Domain.objects.create(name='example18.com', is_active=True, is_primary=False)
        self.tenant19 = Domain.objects.create(name='example19.com', is_active=True, is_primary=False)
        self.tenant20 = Domain.objects.create(name='example20.com', is_active=True, is_primary=False)
        self.tenant21 = Domain.objects.create(name='example21.com', is_active=True, is_primary=False)
        self.tenant22 = Domain.objects.create(name='example22.com', is_active=True, is_primary=False)
        self.tenant23 = Domain.objects.create(name='example23.com', is_active=True, is_primary=False)
        self.tenant24 = Domain.objects.create(name='example24.com', is_active=True, is_primary=False)
        self.tenant25 = Domain.objects.create(name='example25.com', is_active=True, is_primary=False)
        self.tenant26 = Domain.objects.create(name='example26.com', is_active=True, is_primary=False)
        self.tenant27 = Domain.objects.create(name='example27.com', is_active=True, is_primary=False)
        self.tenant28 = Domain.objects.create(name='example28.com', is_active=True, is_primary=False)
        self.tenant29 = Domain.objects.create(name='example29.com', is_active=True, is_primary=False)
        self.tenant30 = Domain.objects.create(name='example30.com', is_active=True, is_primary=False)
        self.tenant31 = Domain.objects.create(name='example31.com', is_active=True, is_primary=False)
        self.tenant32 = Domain.objects.create(name='example32.com', is_active=True, is_primary=False)
        self.tenant33 = Domain.objects.create(name='example33.com', is_active=True, is_primary=False)
        self.tenant34 = Domain.objects.create(name='example34.com', is_active=True, is_primary=False)
        self.tenant35 = Domain.objects.create(name='example35.com', is_active=True, is_primary=False)
        self.tenant36 = Domain.objects.create(name='example36.com', is_active=True, is_primary=False)
        self.tenant37 = Domain.objects.create(name='example37.com', is_active=True, is_primary=False)
        self.tenant38 = Domain.objects.create(name='example38.com', is_active=True, is_primary=False)
        self.tenant39 = Domain.objects.create(name='example39.com', is_active=True, is_primary=False)
        self.tenant40 = Domain.objects.create(name='example40.com', is_active=True, is_primary=False)
        self.tenant41 = Domain.objects.create(name='example41.com', is_active=True, is_primary=False)
        self.tenant42 = Domain.objects.create(name='example42.com', is_active=True, is_primary=False)
        self.tenant43 = Domain.objects.create(name='example43.com', is_active=True, is_primary=False)
        self.tenant44 = Domain.objects.create(name='example44.com', is_active=True, is_primary=False)
        self.tenant45 = Domain.objects.create(name='example45.com', is_active=True, is_primary=False)
        self.tenant46 = Domain.objects.create(name='example46.com', is_active=True, is_primary=False)
        self.tenant47 = Domain.objects.create(name='example47.com', is_active=True, is_primary=False)
        self.tenant48 = Domain.objects.create(name='example48.com', is_active=True, is_primary=False)
        self.tenant49 = Domain.objects.create(name='example49.com', is_active=True, is_primary=False)
        self.tenant50 = Domain.objects.create(name='example50.com', is_active=True, is_primary=False)

    def test_home_view(self):
        url = reverse('home')
        request = self.factory.get(url, HTTP_HOST=self.tenant.name)
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to the home page')
        self.assertContains(response, self.tenant.name)

    def test_contact_view(self):
        url = reverse('contact')
        request = self.factory.get(url, HTTP_HOST=self.tenant.name)
        response = ContactView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact Us')
        self.assertContains(response, self.tenant.name)

    def test_not_paid_view(self):
        url = reverse('not_paid', kwargs={'tenant_in_question': self.tenant3.name})
        request = self.factory.get(url, HTTP_HOST=settings.MANAGEMENT_DOMAIN)
        response = NotPaidView.as_view()(request, tenant_in_question=self.tenant3.name)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Not Paid')
        self.assertContains(response, self.tenant3.name)

    def test_issues_view(self):
        url = reverse('issues')
        request = self.factory.get(url, HTTP_HOST=self.tenant.name)
        response = IssuesView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"https://{settings.MANAGEMENT_DOMAIN}/issues")

    def test_support_view(self):
        url = reverse('support')
        request = self.factory.get(url, HTTP_HOST=settings.MANAGEMENT_DOMAIN)
        response = SupportView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Support')