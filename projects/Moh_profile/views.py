from django.shortcuts import render, redirect
from .models import Covid19, Health_Priorities,Mohevents
from .forms import Covid19Form,Health_PrioritiesForm,EventsForm


# Create your views here.


def index_page(request):
       covid19_data = Covid19.objects.all()

       health = Health_Priorities.objects.all()

       mohevents = Mohevents.objects.all()

       context = {'covid19_data':covid19_data, 'health_priorities':health, 'mohevents':mohevents}

       return render(request, 'Moh_profile/index.html', context )



def post_forms(request):
    covid19form = Covid19Form()
    health_prioritiesform = Health_PrioritiesForm()
    eventsform = EventsForm()
    if request.method == 'POST':
        if 'send_data' in request.POST:
            covid19form = Covid19Form(request.POST)
            if covid19form.is_valid():
                covid19form.save()

                return redirect('index')

        elif 'save_health' in request.POST:
            health_prioritiesform = Health_PrioritiesForm(request.POST)
            if health_prioritiesform.is_valid():
                health_prioritiesform.save()

            return redirect('index')


        elif 'save_event' in request.POST:
            eventsform = EventsForm(request.POST, request.FILES)
            if eventsform.is_valid():
                eventsform.save()

                return redirect('index')

    context = {'covid19form':covid19form, 'health_prioritiesform':health_prioritiesform, 'eventsform':eventsform}

    return render(request, 'Moh_profile/admin-panel.html', context)






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

def dashboards(request):
    return render(request, 'Moh_profile/dashboards.html')


def contacts(request):
    return render(request, 'Moh_profile/contacts.html')


