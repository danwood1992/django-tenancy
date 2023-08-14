from django.urls import re_path
from . import consumers


prod_socket_urlpatterns =  [
    
    #re_path(r"ws/issues/support/(?P<teamName>\w+)/(?P<user>[\w.%+-]*@[A-Za-z0-9.-]*\.[A-Za-z]{0,4}|AnonymousUser)/$", consumers.SupportConsumerASync.as_asgi()),
    re_path(r"wss/issues/support/(?P<teamName>\w+)/(?P<user>[\w.%+-]*@[A-Za-z0-9.-]*\.[A-Za-z]{0,4}|AnonymousUser)/$", consumers.SupportConsumerASync.as_asgi()),
    
]

websocket_urlpatterns = prod_socket_urlpatterns