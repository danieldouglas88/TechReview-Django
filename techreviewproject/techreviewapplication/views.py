from django.shortcuts import render
from .models import TechType, ProductTech, TechReview

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resource(request):
    typeList = TechType.objects.all()
    return render(request, 'club/resource.html', {'typeList': typeList})
