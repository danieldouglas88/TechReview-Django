from django.shortcuts import render
from .models import TechType, TechMeeting
from django.http import HttpResponse
import datetime
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
    
@login_required
def createmeeting(request):
    form = MeetingForm()
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'club/createmeeting.html', {'form': form})

@login_required
def createresource(request):
    form = ResourceForm()
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/createresource.html', {'form': form})

@login_required
def login(request):
    return render(request, 'club/loginmessage.html')

def loginmessage(request):
    user = request.user.username
    return render(request, 'club/loginmessage.html', {"user":user})

def logoutmessage(request):
    user = request.user.username
    logout(request)
    return render(request, 'club/logoutmessage.html',  {"user":user})

