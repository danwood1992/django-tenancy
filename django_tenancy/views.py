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
from apps.admin.tenancy.models.domain import Domain

User = get_user_model()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TenantInQuestionMixin:
    """
    Mixin class for views that require tenant_in_question context variable.
    The tenant_in_question is in the url of an inactive, unpaid or nonexistent tenant but has its domain pointing to the server.. 
    Youc can remove this mixin if you don't need the tenant_in_question context variable. Remember to remove it from the urls.py as well.
    """
    
    def get_context_data(self, **kwargs):
        """
        Returns the context data for the view, including the tenant_in_question variable.
        """
        context = super().get_context_data(**kwargs)
        context['tenant_in_question'] = self.kwargs.get('tenant_in_question')
        logging.info(f"Tenant in question - {context['tenant_in_question']}")
        return context
    
    def logfunction(self, message):
        """
        Logs the given message to the logging system.
        """
        logging.info(message)
        




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
        tenant = getattr(self.request, 'current_tenant', None)
        dev_mode = getattr(settings, 'DEV_MODE', 0)
        context.update({
            'tenant': tenant,
            'staffseat': self.request.user.staffseat_related.filter(tenant=self.request.current_tenant).first(),
            'paid_until': tenant.paid_until if tenant else None,
            'dev_mode': dev_mode,
            'management_domain': settings.MANAGEMENT_DOMAIN,
            'user': self.request.user,
            'superuser': self.request.user if self.request.user.is_superuser else None
        })
        return context

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


class NotPaidView(TenantInQuestionMixin, BaseView):
    template_name = 'not_paid.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.logfunction(message = str("This view is - NotPaidView."))
        return context
    
class BaseView(TemplateView):
    """
    Base View for other views
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tenant = getattr(self.request, 'current_tenant', None)
        dev_mode = getattr(settings, 'DEV_MODE', 0)
        context['tenant'] = tenant
        context['staffseat'] = self.request.user.staffseat_related.filter(tenant=self.request.current_tenant).first()
        context['paid_until'] = tenant.paid_until if tenant else None
        context['dev_mode'] = dev_mode
        context['management_domain'] = settings.MANAGEMENT_DOMAIN
        context['user'] = self.request.user
        if self.request.user.is_superuser:
            context['superuser'] = self.request.user
        return context
    


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


class NotPaidView(TenantInQuestionMixin, BaseView):
    template_name = 'not_paid.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.logfunction(message = str("This view is - NotPaidView."))
        return context
    
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['teamName'] = self.kwargs['teamName']
        return context


    
    
class SignUpView(TenantInQuestionMixin, BaseView):
    template_name = 'signup.html'
    
    def get_context_data(self, **kwargs):
        
        return super().get_context_data(**kwargs)
        
    def get_template_names(self):
        tenant = getattr(self.request, 'current_tenant', None)
        if tenant and tenant.management_tenant:
            return ['management/signup/index.html']
        return super().get_template_names()
    

    