from django.urls import path
from .views import *

app_name='apps'

urlpatterns=[
    path('',index,name='index'),
    path('projects/',projects,name='projects'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('r/', request_callback, name='callback'),

]