# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('add_server/', views.add_server, name='add_server'),
]