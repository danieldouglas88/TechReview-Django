from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('resources', views.resource, name='resource'),
    path('meeting', views.meeting, name='meeting'),
    path('findameeting', views.findameeting, name='findameeting'),    
    path('meetingresult', views.meetingresult, name='meetingresult'),
    path('meetingdetail', views.meetingdetail, name='meetingdetail'),
    path('createmeeting', views.createmeeting, name='createmeeting'),
    path('createresource', views.createresource, name='createresource'),

]
