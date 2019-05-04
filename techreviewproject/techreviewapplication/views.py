from django.shortcuts import render
from .models import TechType, TechMeeting
from django.http import HttpResponse
import datetime

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resource(request):
    typeList = TechType.objects.all()
    return render(request, 'club/resource.html', {'typeList': typeList})

def meeting(request):
    meetingList = TechMeeting.objects.all()
    return render(request, 'club/meeting.html', {'meetingList': meetingList})

def findameeting(request):
    return render(request, 'club/findameeting.html')

def meetingresult(request):
    try:
        findameetingList = TechMeeting.objects.raw("SELECT * FROM TechMeeting WHERE ID = '{0}'".format(request.GET.get('meetingid')))
        return render(request, 'club/meetingresult.html', {'findameetingList': findameetingList})
    except: 
        return HttpResponse("Sorry, there appears to be an issue")

def meetingdetail(request):
    try:
        meetingdetailList = TechMeeting.objects.raw("SELECT * FROM TechMeeting WHERE ID = '{0}'".format(request.GET.get('meetingid')))
        return render(request, 'club/meetingdetail.html', {'meetingdetailList': meetingdetailList})
    except:
        return HttpResponse("Sorry, there appears to be an issue")

def createmeeting(request):
    return render(request, 'club/createmeeting.html')
   
def createmeetingresult(request):
    try:
        createmeeting = TechMeeting(meetingtype = request.GET.get('meetingtype'), meetingtitle = request.GET.get('meetingtitle'), meetingdate = request.GET.get('meetingdate'), posteddate = datetime.datetime.now(), experiencelevel = request.GET.get('experiencelevel'))
        createmeeting.save()
        return render(request, 'club/createmeetingresult.html', {'createmeeting': createmeeting})
    except:
        return HttpResponse("Sorry, there appears to be an issue")

def createresource(request):
    return render(request, 'club/createresource.html')

def createresourceresult(request):
    try:
        createresource = TechType(techtypename = request.GET.get('resourcename'), techdescription = request.GET.get('resourcedescription'))
        createresource.save()
        return render(request, 'club/createresourceresult.html', {'createresource': createresource})
    except:
        return HttpResponse("Sorry, there appears to be an issue")
