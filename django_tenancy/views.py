import logging
from typing import Any

from django import http
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from graphql_jwt.exceptions import JSONWebTokenError
from graphql_jwt.shortcuts import get_token
from django.contrib.auth import authenticate, login
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




class BaseView(TemplateView):
    """
    Base View for other views
    """

   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tenant = getattr(self.request, 'current_tenant', None)
        dev_mode = getattr(settings, 'DEV_MODE', 0)
        context['tenant'] = tenant
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
    
    def get(self, request, *args, **kwargs):
        tenant = getattr(request, 'current_tenant', None)
        page = 'issues'
        
      
        if not tenant or not tenant.management_tenant: #change logic to do 
            logger.info(f"{request.get_host()} Attempting to access issues page from own domain. Redirecting to management domain")
            # Redirect to the management domain's issues page if tenant is not a management tenant
            return HttpResponseRedirect(f"https://{settings.MANAGEMENT_DOMAIN}/{page}")
        return super(IssuesView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
    
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
    
    def get(self, request, *args, **kwargs):
        tenant = getattr(request, 'current_tenant', None)
        page = 'support'
        
      
        if not tenant or not tenant.management_tenant:
            logger.info(f"{request.get_host()} Attempting to access issues page from own domain. Redirecting to management domain")
            # Redirect to the management domain's issues page if tenant is not a management tenant
            
            return HttpResponseRedirect(f"https://{settings.MANAGEMENT_DOMAIN}/{page}")
        
        return super().get(request, *args, **kwargs)

    
    
class SignUpView(TenantInQuestionMixin, BaseView):
    template_name = 'signup.html'
        
    def get_template_names(self):
        tenant = getattr(self.request, 'current_tenant', None)
        if tenant and tenant.management_tenant:
            return ['management/signup/index.html']
        return super().get_template_names()
    

    