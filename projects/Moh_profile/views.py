from django.shortcuts import render,redirect
from .models import Covid19, Health_Priorities, Mohevents

# Create your views here.
def get_index(request):
    covid19_data = Covid19.objects.all()
    context = {'covid19_data':covid19_data}
    
    return render(request, 'Moh_profile/index.html', context)

def post_covid19_data(request):
    if request.method == 'POST':
        new_cases = request.POST['new_cases']
        cumulative_confirmed_cases = request.POST['cumulative_confirmed_cases']
        active_cases = request.POST['active_cases']
        total_recovered = request.POST['total_recovered']
        currently_admitted_in_treatment_units = request.POST['Currently_admitted_in_treatment_units']
        new_discharges_from_treatment_units = request.POST['New_discharges_from_treatment_units']
        total_tests_conducted = request.POST['total_tests_conducted']
        total_deaths = request.POST['total_deaths']
        
        return render(request, 'Moh_profile/index.html')

def about(request):
    return render(request, 'Moh_profile/about.html')

def events(request):
    return render(request, 'Moh_profile/events.html')