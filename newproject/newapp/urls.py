from django.urls import path
from .views import newapp_list
from . import views

urlpatterns=[
    path('',newapp_list)
]