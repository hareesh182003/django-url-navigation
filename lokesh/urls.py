from django.urls import path
from lokesh.views import *

app_name = 'lok_dude'

urlpatterns = [
    path('saviour/',saviour,name='saviour'),
]