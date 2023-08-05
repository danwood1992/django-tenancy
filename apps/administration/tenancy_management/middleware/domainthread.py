import logging
from threading import local
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from ..models.tenant import Tenant
from ..models.domain import Domain
from datetime import date

_thread_local = local()

# Get an instance of a logger
logger = logging.getLogger(__name__)

class DomainMiddleware:
    """
    Middleware that fetches the current tenant based on the domain of the request.
    
    This middleware is used to determine the current tenant based on the subdomain or domain 
    of the incoming request. If the tenant exists and is active, it sets the tenant 
    into thread local storage. If the tenant does not exist, is inactive, or has not paid, 
    it redirects the user to appropriate URLs specified in settings.

    Methods
    -------
    __call__(request):
        Fetches the tenant based on the subdomain in the request, determines the 
        tenant's status and handles redirection if necessary.

    get_redirect_url(request, tenant, redirect_template):
        Constructs a redirect URL replacing the placeholder in the redirect template
        with the appropriate tenant slug.

    """
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        host = request.get_host().split(':')[0]
      
        
        tenant = None
        
        try:
            
            domain_obj =  get_object_or_404(Domain, domain_name=host)
        
            tenant = domain_obj.tenant

            if not Tenant.objects.filter(management_tenant=True).exists():
                return HttpResponseRedirect(self.get_redirect_url(request,tenant,settings.NO_MANAGEMENT_TENANT_REDIRECT))
            
            if tenant.management_tenant:
                _thread_local.tenant = tenant
                
                response = self.get_response(request)
                return response
            
            if not tenant.is_active: 
                return HttpResponseRedirect(self.get_redirect_url(request,tenant,settings.INACTIVE_TENANT_REDIRECT))
            
            if tenant.paid_until and tenant.paid_until < date.today():
                return HttpResponseRedirect(self.get_redirect_url(request,tenant, settings.UNPAID_TENANT_REDIRECT))

        except Http404 as e:
            
            return HttpResponseRedirect(self.get_redirect_url(request,tenant, settings.NO_DOMAIN_REDIRECT))

        _thread_local.tenant = tenant
        logger.info(f'Processing request for {tenant} - {host}')

        response = self.get_response(request)
        return response
    
    def get_redirect_url(self,request, tenant, redirect_template):
        """
        This function replaces the placeholder in redirect url with the tenant slug
        """
        if tenant is None:
            new_host_parts = request.get_host().split('.')
            new_domain = new_host_parts[0]
            return redirect_template.replace('<tenant_in_question>', new_domain) 
        if tenant.name:
            tenant_slug = tenant.name
        else: #grab the first part of the domain
            tenant_slug = 'newcustomer'
        
        return redirect_template.replace('<tenant_in_question>', tenant_slug)


def get_current_tenant():
    """
    Fetches the current tenant from thread local storage.

    Returns
    -------
    Tenant
        The tenant set in the thread local storage. If no tenant is set, returns None.

    """
    return getattr(_thread_local, "tenant", None)