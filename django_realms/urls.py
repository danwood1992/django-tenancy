
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path


from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

from django.views.decorators.csrf import csrf_exempt


from apps.core.todo.views import ToDoView

from .views import (ContactView, DashboardView, HomeView, IssuesView,
                    SignUpView, SupportView, UnpaidRealmView, login_view,
                    logout_view)

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
    path('dashboard/<uuid:realmid>/', DashboardView.as_view(), name='dashboard_view'),

    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('unpaid', UnpaidRealmView.as_view(), name='unpaid'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('app/todo', ToDoView.as_view(), name='todo')
                   
    ]

api_patterns = [path("graphql/", jwt_cookie(GraphQLView.as_view(graphiql=True))),
    ]

if settings.USE_DJANGO_TEMPLATES:
    urlpatterns = admin_patterns + tenant_patterns + api_patterns
else:
    urlpatterns = api_patterns

