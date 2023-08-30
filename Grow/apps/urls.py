from django.urls import path
from .views import *

app_name='apps'

urlpatterns=[
    path('',index,name='index'),
    path('projects/',projects,name='projects'),

]