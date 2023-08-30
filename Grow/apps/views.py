from django.shortcuts import render
from apps.models import TeamMembersModel

# Create your views here.
def index(request):
    return render(request,'index.html')

def projects(request):
    return render(request,'project.html')

def index(request):
    qs=TeamMembersModel.objects.all()
    return render(request,'index.html',{"qs":qs})