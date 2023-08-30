from django.shortcuts import render
from apps.models import TeamMembersModel,Projects

# Create your views here.
# def index(request):
#     return render(request,'index.html')

def projects(request):
    return render(request,'project.html')

def index(request):
    Team=TeamMembersModel.objects.all()
    projects=Projects.objects.all()
    return render(request,'index.html',{"Team":Team,'projects':projects})