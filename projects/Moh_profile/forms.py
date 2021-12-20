from django import forms
from Moh_profile.models import Covid19, Health_Priorities, Mohevents


class Covid19Form(forms.ModelForm):
    class Meta:
        model = Covid19
        fields = ['new_cases',
        'active_cases', 
        'new_recovered',
         'currently_admitted',
          'new_tests_conducted',
          'new_discharges', 
          'new_deaths']

class Health_PrioritiesForm(forms.ModelForm):
    class Meta:
        model = Health_Priorities
        fields = ['disease', 'priority', 'content_url']

class EventsForm(forms.ModelForm):
    class Meta:
        model = Mohevents
        fields = '__all__'
        