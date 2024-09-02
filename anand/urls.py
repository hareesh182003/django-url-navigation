from django.urls import path

from anand.views import *

app_name = 'an_dude'

urlpatterns = [
    path('coder/',coder,name='coder'),
]