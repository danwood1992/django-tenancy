
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from .views import HomeView, NotPaidView, SignUpView, IssuesView, ContactView, SupportView
from django.conf import settings
# Django docs have a guide on how to use csrf exempt with graphene - https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax
# Django tenancy will use csrf exempt for now,this may be changed in the future
from django.views.decorators.csrf import csrf_exempt

# the graphql path is the endpoint for the graphql api, 
# change to false if you don't want the graphiql browser interface
# urls are split into admin, tenant and shared urls --- logic not yet in place

admin_patterns = [
    path('admin/', admin.site.urls),
    path('issues/', IssuesView.as_view(), name='issues'),   
    path('issues/support/<str:teamName>/<str:user>/', SupportView.as_view(), name='support')            
                  ] 

tenant_patterns = [
    path('', HomeView.as_view(), name='home'),
    path('<tenant_in_question>/unpaid', NotPaidView.as_view(), name='unpaid'),
    path('<tenant_in_question>/signup', SignUpView.as_view(), name='signup'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('contact/', ContactView.as_view(), name='contact')
                   
    ]

api_patterns = [path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    ]

if settings.USE_DJANGO_TEMPLATES:
    urlpatterns = admin_patterns + tenant_patterns + api_patterns
else:
    urlpatterns = api_patterns

