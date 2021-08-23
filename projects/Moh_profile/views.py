from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Moh_profile/index.html')

def about(request):
    return render(request, 'Moh_profile/about.html')

def events(request):
    return render(request, 'Moh_profile/events.html')