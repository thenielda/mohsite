from django.shortcuts import render,redirect
from .models import Covid19, Health_Priorities, Mohevents
from .forms import Covid19form

# Create your views here.
def get_index(request):
     covid19_data = Covid19.objects.all()
     health_priorities = Health_Priorities.objects.all()
     mohevents = Mohevents.objects.all()
     context = {'covid19_data':covid19_data,
                'health_priorities':health_priorities,
                'mohevents':mohevents}
    
     return render(request, 'Moh_profile/index.html',context)


def post_health_priorities(request):
    if request.method == 'POST':
        disease = request.POST['disease']
        priority = request.POST['priority']
        content_url = request.POST['content_url']

        return render(request, 'Moh_profile/index.html')

def post_covid19_data(request):
    if request.method == 'POST':
        date = request.POST['date']
        new_cases = request.POST['new_cases']
        active_cases = request.POST['active_cases']
        new_recovered = request.POST['new_recovered']
        currently_admitted = request.POST['Currently_admitted']
        new_discharges = request.POST['New_discharges']
        new_deaths = request.POST['new_deaths']
        
        return render(request, 'Moh_profile/index.html')

def post_mohevents(request):
    if request.method == 'POST':
        event_title = request.POST['event_title']
        event_image = request.POST['event_image']
        event_content = request.POST['event_content']
        event_date = request.POST['event_date']

        return render(request, 'Moh_profile/index.html')

def about(request):
    return render(request, 'Moh_profile/about.html')

def events(request):
    return render(request, 'Moh_profile/events.html')

def services(request):
    return render(request, 'Moh_profile/e-services.html')

def resources(request):
    return render(request, 'Moh_profile/resources.html')

def vacancies(request):
    return render(request, 'Moh_profile/vacancies.html')

def complaints(request):
    return render(request, 'Moh_profile/complaints.html')

def contacts(request):
    return render(request, 'Moh_profile/contacts.html')

def admin_panel(request):
    form = Covid19form()
    if request.method == 'POST':
        Covid19form(request.POST)
    return render(request, 'Moh_profile/admin-panel.html', {'form':form})