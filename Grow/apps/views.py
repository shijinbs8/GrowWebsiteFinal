from django.shortcuts import render,redirect
from apps.models import TeamMembersModel,Projects,Tech,CallBackRequest
from .forms import CallBackForm
import csv
from django.http import HttpResponse
from django.utils import timezone
from .models import CallBackRequest

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

def download_csv(request):
    # Create the HttpResponse object with appropriate headers.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="callbacks_{timezone.now().strftime("%Y-%m-%d")}.csv"'

    writer = csv.writer(response)
    # Write the header
    writer.writerow(['Name', 'Email', 'Mobile', 'Subject', 'Message', 'Created At'])

    # Filter the records based on whether they have been exported
    callbacks = CallBackRequest.objects.filter(exported=False)

    for callback in callbacks:
        writer.writerow([callback.name, callback.email, callback.mobile, callback.subject, callback.message, callback.created_at])

        # Mark the record as exported
        callback.exported = True
        callback.save(update_fields=['exported'])

    return response
