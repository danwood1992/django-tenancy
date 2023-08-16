from django.shortcuts import render
from django_tenancy.views import BaseView
from apps.core.seats.models import StaffSeat
from .models import Category, Task, Assignment

class ToDoView(BaseView):
    """
    View for all tenants.
    View for to do application.

    Attributes:
    - template_name (str): The name of the template to be rendered.
    """

    template_name = 'todo/index.html'
    
    def get_context_data(self, **kwargs):
        """
        Returns the context data for the view.

        Returns:
        - context (dict): A dictionary containing the context data for the view.
        """
        context = super(ToDoView, self).get_context_data(**kwargs)
        try:
            context['staffseat'] = self.request.user.staffseat_related.filter(tenant=self.request.current_tenant).first()
        except:
            context['staffseat'] = None
        
        context['assignments'] = Assignment.objects.filter(assigned_to=context['staffseat']) # filters assignments by staffseat

        context['tenant'] = getattr(self.request, 'current_tenant', None)
        context['staff_choice'] = StaffSeat.objects.filter(tenant=self.request.current_tenant)
        context['category_choice'] = Category.objects.filter(tenant=self.request.current_tenant)
    
        context['staff_choice'] = StaffSeat.objects.filter(tenant=self.request.current_tenant)
        context['category_choice'] = Category.objects.filter(tenant=self.request.current_tenant)
    
        return context
    
    