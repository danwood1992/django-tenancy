from django.shortcuts import render
from django_realms.views import BaseView
from apps.admin.realms.models import RealmAccount
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
            context['assignments'] = Assignment.objects.filter(assigned_to=context['realm_account']) # filters assignments by staffseat
            context['staff_choice'] = RealmAccount.objects.filter()
            context['category_choice'] = Category.objects.filter(tenant=self.request.current_tenant)
        except:
            pass
        return context
    
    