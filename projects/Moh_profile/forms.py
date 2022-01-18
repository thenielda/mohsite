from django import forms
from .models import Covid19, Health_Priorities, Mohevents,Contact,Documents


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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = '__all__'