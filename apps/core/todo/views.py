from django.shortcuts import render
from django_tenancy.views import BaseView
from apps.core.seats.models import StaffSeat
from .models import Category
# Create your views here.
class ToDoView(BaseView):
    """
    View for all tenants.
    View for to do application.
    """
    template_name = 'todo/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['tasks_assigned'] = self.request.user.staffseat_related.tasks.all()
        except:
            context['tasks_assigned'] = None
        
        context['staff_choice'] = StaffSeat.objects.all()

        context['tenant'] = getattr(self.request, 'current_tenant', None)
        context['category_choice'] = Category.objects.all()
   
        
        return context
    
    