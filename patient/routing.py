from django.urls import re_path, path

from . import consumers
websocket_urlpatterns  = [


    path("ws/socket-server/", consumers.chan.as_asgi())

   ]