from django.shortcuts import render
from .models import TechType, TechMeeting
from django.http import HttpResponse


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
        findameetingList = TechMeeting.objects.raw('SELECT * FROM TechMeeting WHERE ID = %s', request.GET.get('meetingid'))
        return render(request, 'club/meetingresult.html', {'findameetingList': findameetingList})
    except: 
        return HttpResponse("Sorry, there appears to be no record for " + "'" + request.GET.get('meetingid') + "'.")

def meetingdetail(request):
    meetingdetailList = TechMeeting.objects.raw('SELECT * FROM TechMeeting WHERE ID = %s', request.GET.get('meetingid'))
    return render(request, 'club/meetingdetail.html', {'meetingdetailList': meetingdetailList})