from django.urls import re_path
from . import consumers


websocket_urlpatterns =  [
    
    re_path(r"wss/issues/support/(?P<teamName>\w+)/(?P<user>[\w.%+-]*@[A-Za-z0-9.-]*\.[A-Za-z]{0,4}|AnonymousUser)/$", consumers.SupportConsumerASync.as_asgi()),
    
]