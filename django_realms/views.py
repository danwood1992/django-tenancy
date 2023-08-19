import logging
from typing import Any
from django.urls import reverse
from django import http
from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from graphql_jwt.exceptions import JSONWebTokenError
from graphql_jwt.shortcuts import get_token
from apps.admin.realms.models import Realm, RealmAccess, RealmAccount

User = get_user_model()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Get the primary realm_id for this user
            try:
                primary_realm_access = RealmAccess.objects.get(user=user, is_primary=True)
                realm_id = primary_realm_access.realm.id
                dashboard_url = reverse('dashboard_view', args=[realm_id])
                return JsonResponse({'status': 'success', 'dashboard_url': dashboard_url})
            except RealmAccess.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'No primary realm assigned'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
    
    return JsonResponse({'status': 'error', 'message': 'Unsupported method'})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Unsupported method'})

class BaseView(TemplateView):
    """
    Base View for other views
    """
    pagetype = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['management_domain'] = settings.MANAGEMENT_DOMAIN
        
        pagetype = self.pagetype
        if  self.request.user.is_authenticated:
            print("User is authenticated")
            realms_can_access = RealmAccess.objects.filter(user=self.request.user)
            context['realms_can_access'] = realms_can_access
        if pagetype != 'public':
            # Get the UUID from the URL parameters
            realm_id = kwargs.get('realmid')
            
            if realm_id:
                try:
                    realm = Realm.objects.get(pk=realm_id)
                    context['current_realm'] = realm
                    realm_access = RealmAccess.objects.select_related('realm_account').get(realm=realm, user=self.request.user)
                    context['realm_access'] = realm_access
                    context['realm_account'] = realm_access.realm_account
                except (Realm.DoesNotExist, RealmAccess.DoesNotExist):
                    # Handle the error, maybe raise a 404 error or redirect to another view
                    pass

        return context
    
class HomeView(BaseView):
    pagetype = 'public'
    template_name = 'management/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['realms'] = Realm.objects.all()
        return context
        
class ContactView(BaseView):
    pagetype = 'public'
    template_name = 'contact/index.html'

class DashboardView(BaseView):
    template_name = 'dashboard/index.html'

class IssuesView(BaseView):
    """
    View only for management domain .
    If a request is for a non management tenant domain;
        They will be redirected to the management domain's issues page,
        A log will be made in the log file.
    """
    template_name = 'issues/index.html'
    
class SupportView(BaseView):
    """
    View only for management domain .
    If a request is for a non management tenant domain;
        They will be redirected to the management support page,
        A log will be made in the log file.
    """
    template_name = 'issues/support/index.html'

class SignUpView(BaseView):
    template_name = 'signup.html'
    
class UnpaidRealmView(BaseView):
    template_name = 'not_paid.html'
    
  