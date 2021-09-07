from django.shortcuts import render,redirect
from .models import Covid19, Health_Priorities, Mohevents

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
        content_url = request.POST['event_content']
        event_date = request.POST['event_date']

        return render(request, 'Moh_profile/index.html')

def about(request):
    return render(request, 'Moh_profile/about.html')

def events(request):
    return render(request, 'Moh_profile/events.html')