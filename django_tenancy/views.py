import logging
from typing import Any

from django import http
from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from graphql_jwt.exceptions import JSONWebTokenError
from graphql_jwt.shortcuts import get_token
from apps.admin.realms.models.domain import Domain

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
            return JsonResponse({'status': 'success'})
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['management_domain'] = settings.MANAGEMENT_DOMAIN
     
        return context
    
class HomeView(BaseView):
    template_name = 'management/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tenant_domains'] = Domain.objects.all()
        return context
        
class ContactView(BaseView):
    template_name = 'contact/index.html'

class HomeView(BaseView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tenant_domains'] = Domain.objects.all()
        return context
        
    def get_template_names(self):
        tenant = getattr(self.request, 'current_tenant', None)
        if tenant and tenant.management_tenant:
            return ['management/index.html']
        return super().get_template_names()
        
        
class ContactView(BaseView):
    template_name = 'contact/index.html'

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
    
  