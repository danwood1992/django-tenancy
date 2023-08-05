import logging
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseNotFound
from ..models.tenant import Tenant
from ..models.domain import Domain
from ..utils import get_host_from_request , tenant_subscription_check
from datetime import date

# Get an instance of a logger
logger = logging.getLogger(__name__)

class DomainMiddleware:
    """
    Middleware that fetches the current tenant based on the domain of the request.
    
    This middleware is used to determine the current tenant based on the subdomain or domain 
    of the incoming request. If the tenant exists and is active, it sets the tenant 
    in the request. If the tenant does not exist, or a subscription isnt active then the tenant
    is redirected accordingly.

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
         
        host = get_host_from_request(request)
       
        tenant = None
           
        try:
            
            if not Tenant.objects.filter(management_tenant=True).exists(): # returns boolean 
                # if no management tenant exist redirect to the no management tenant redirect
                logger.info(f"no management tenant exists - redirecting to {settings.NO_MANAGEMENT_TENANT_REDIRECT}")
                return HttpResponseRedirect(self.get_redirect_url(request,tenant,settings.NO_MANAGEMENT_TENANT_REDIRECT))
           
            domain_queryset = Domain.objects.select_related('tenant')
            domain_obj = get_object_or_404(domain_queryset, domain_name=host)
            # get the domain object based on the host in the request
            tenant = domain_obj.tenant # tenant in memory here based off the host (*.domain, domain) in the request
            request.current_tenant = tenant
            print (f"tenant in memory from domain object - {tenant}")
            
            if tenant.management_tenant:
                
                response = self.get_response(request)
                return response # Return the response and continue processing the request without checks
            
            tenant_check_pass = tenant_subscription_check(tenant)
            
            if tenant_check_pass is False:
                context = {'tenant': tenant, 'management_domain': settings.MANAGEMENT_DOMAIN, 'dev_mode': settings.DEV_MODE}
                return HttpResponseNotFound(render(request, 'notfound/index.html', context))
           
        except Http404 as e:
            
            return HttpResponseRedirect(self.get_redirect_url(request,tenant, settings.NO_DOMAIN_REDIRECT))

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





