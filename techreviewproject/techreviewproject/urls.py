from django.contrib import admin
from django.urls import path, include
from techreviewapplication import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('techreviewapplication/', include('techreviewapplication.urls')),
    path('', views.index, name='index'),
    path('resources', views.resource, name='resource'),
]
