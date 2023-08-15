from django.shortcuts import render
from django_tenancy.views import BaseView

# Create your views here.
class ToDoView(BaseView):
    """
    View for all tenants.
    View for to do application.
    """
    template_name = 'todo/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks_assigned'] = self.request.user.staffseat_related.tasks.all()
        
        return context