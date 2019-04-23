from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('resources', views.resource, name='resource'),
]
