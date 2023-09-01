from django.shortcuts import render,redirect
from apps.models import TeamMembersModel,Projects,Tech,CallBackRequest
from .forms import CallBackForm

# Create your views here.
# def index(request):
#     return render(request,'index.html')

def projects(request):
    projects=Projects.objects.all()

    return render(request,'project.html',{'projects':projects})

def index(request):
    tech=Tech.objects.all()
    Team=TeamMembersModel.objects.all()
    projects=Projects.objects.all()
    return render(request,'index.html',{"Team":Team,'projects':projects,'tech':tech})

def about(request):
    tech=Tech.objects.all()
    Team=TeamMembersModel.objects.all()
    projects=Projects.objects.all()
    return render(request,'about.html',{"Team":Team,'projects':projects,'tech':tech})

def contact(request):
    if request.method == 'POST':
        form = CallBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps:contact')
    else:
        form = CallBackForm()

    return render(request,'contact.html', {'form': form})
    


def request_callback(request):
    if request.method == 'POST':
        form = CallBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps:index')
    else:
        form = CallBackForm()

    return render(request, 'index.html', {'form': form})